/* ============================================================
   FREE MIND ML — app.js
   Master Application Controller: Router, State, Views, UI Logic
   Redesigned: Card-grid landing + Blog-style (colah) lessons
   ============================================================ */
window.FML = window.FML || {};

(function() {
  'use strict';
  const U = FML.utils;

  /* ─── STATE MANAGEMENT (LOCALSTORAGE) ─────────────────────── */
  const state = {
    progress: U.load('fml_progress', {}),       // { [lessonId]: { completed: bool, quizScore: int, updatedAt: ts } }
    bookmarks: U.load('fml_bookmarks', []),     // [ lessonId, ... ]
    currentLessonId: null,
    activeTab: 'overview',
    theme: U.load('fml_theme', 'light')
  };

  function saveProgress(id, isCompleted = true, quizScore = null) {
    state.progress[id] = state.progress[id] || {};
    state.progress[id].completed = isCompleted;
    if (quizScore !== null) state.progress[id].quizScore = quizScore;
    state.progress[id].updatedAt = Date.now();
    U.save('fml_progress', state.progress);
    updateSidebarProgress();
  }

  function isCompleted(id) {
    return !!(state.progress[id] && state.progress[id].completed);
  }

  function toggleBookmark(id) {
    const idx = state.bookmarks.indexOf(id);
    if (idx >= 0) {
      state.bookmarks.splice(idx, 1);
      U.toast('Bookmark removed', 'info');
    } else {
      state.bookmarks.push(id);
      U.toast('Lesson bookmarked', 'success');
    }
    U.save('fml_bookmarks', state.bookmarks);
    updateBookmarkButton(id);
  }

  function isBookmarked(id) {
    return state.bookmarks.includes(id);
  }

  /* ─── THEME CONTROLLER ────────────────────────────────────── */
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    U.save('fml_theme', theme);
  }

  function initTheme() {
    applyTheme(state.theme);
    const toggles = [
      document.getElementById('theme-toggle'),
      document.getElementById('theme-toggle-sidebar')
    ];
    toggles.forEach(btn => {
      if (btn) {
        btn.addEventListener('click', () => {
          const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
          applyTheme(next);
        });
      }
    });
  }

  /* ─── SIDEBAR & PROGRESS SUMMARY ──────────────────────────── */
  function updateSidebarProgress() {
    const total = (FML.catalog || []).length || 52;
    const completedCount = Object.values(state.progress).filter(p => p.completed).length;
    const pct = Math.round((completedCount / total) * 100);

    const ring = document.getElementById('prog-ring');
    const pctEl = document.getElementById('prog-pct');
    const labelEl = document.getElementById('prog-label');

    if (pctEl) pctEl.textContent = `${pct}%`;
    if (labelEl) labelEl.textContent = `${completedCount} / ${total} lessons`;

    if (ring) {
      const circ = 2 * Math.PI * 22; // ~138.2
      const offset = circ - (pct / 100) * circ;
      ring.style.strokeDashoffset = offset;
    }

    // Mark links in sidebar
    document.querySelectorAll('.nav-lesson').forEach(link => {
      const id = link.getAttribute('data-id');
      link.classList.toggle('completed', isCompleted(id));
      if (id === state.currentLessonId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  function initSidebarAccordions() {
    document.querySelectorAll('.nav-section').forEach(sec => {
      const hdr = sec.querySelector('.nav-section-hdr');
      const items = sec.querySelector('.nav-section-items');
      if (hdr && items) {
        hdr.addEventListener('click', () => {
          const isOpen = hdr.getAttribute('aria-expanded') === 'true';
          hdr.setAttribute('aria-expanded', !isOpen);
          items.hidden = isOpen;
        });
      }
    });

    // Hamburger + Sidebar + Backdrop
    const burger = document.getElementById('hamburger');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('sidebar-close');
    const backdrop = document.getElementById('sidebar-backdrop');

    function openSidebar() {
      if (sidebar) sidebar.classList.add('open');
      if (backdrop) backdrop.classList.add('active');
      if (burger) burger.setAttribute('aria-expanded', 'true');
    }

    function closeSidebar() {
      if (sidebar) sidebar.classList.remove('open');
      if (backdrop) backdrop.classList.remove('active');
      if (burger) burger.setAttribute('aria-expanded', 'false');
    }

    if (burger) burger.addEventListener('click', openSidebar);
    if (closeBtn) closeBtn.addEventListener('click', closeSidebar);
    if (backdrop) backdrop.addEventListener('click', closeSidebar);

    // Close sidebar on link click
    document.querySelectorAll('.sidebar-nav a').forEach(a => {
      a.addEventListener('click', () => {
        closeSidebar();
      });
    });
  }

  /* ─── GLOBAL SEARCH & KEYBINDINGS (⌘K / Ctrl+K) ────────────── */
  function initSearch() {
    const input = document.getElementById('global-search');
    const results = document.getElementById('search-results');

    if (!input || !results) return;

    // Shortcut
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        // Open sidebar first if closed
        const sidebar = document.getElementById('sidebar');
        if (sidebar && !sidebar.classList.contains('open')) {
          sidebar.classList.add('open');
          document.getElementById('sidebar-backdrop').classList.add('active');
        }
        input.focus();
        input.select();
      }
      if (e.key === 'Escape' && document.activeElement === input) {
        results.hidden = true;
        input.blur();
      }
    });

    input.addEventListener('input', U.debounce((e) => {
      const q = e.target.value.trim().toLowerCase();
      if (!q) {
        results.hidden = true;
        results.innerHTML = '';
        return;
      }

      // Search catalog & glossary
      const matches = [];

      (FML.catalog || []).forEach(l => {
        let score = 0;
        if (l.title.toLowerCase().includes(q)) score += 10;
        if (l.id.toLowerCase() === q) score += 20;
        if (l.tags && l.tags.some(t => t.toLowerCase().includes(q))) score += 5;
        if (l.shortDesc && l.shortDesc.toLowerCase().includes(q)) score += 3;

        if (score > 0) {
          matches.push({ type: 'lesson', item: l, score });
        }
      });

      (FML.glossaryTerms || []).forEach(g => {
        let score = 0;
        if (g.term.toLowerCase().includes(q)) score += 8;
        if (g.definition.toLowerCase().includes(q)) score += 2;
        if (score > 0) {
          matches.push({ type: 'glossary', item: g, score });
        }
      });

      matches.sort((a, b) => b.score - a.score);

      if (matches.length === 0) {
        results.innerHTML = '';
        const emptyEl = document.createElement('div');
        emptyEl.className = 'p-3 text-xs text-muted';
        emptyEl.textContent = `No matching topics found for "${q}"`;
        results.appendChild(emptyEl);
        results.hidden = false;
        return;
      }

      results.innerHTML = matches.slice(0, 8).map(m => {
        if (m.type === 'lesson') {
          return `
            <a class="search-result-item" href="#/lesson/${m.item.id}">
              <div class="search-result-title">
                <span class="badge badge-subtle mr-1">${m.item.id}</span>
                ${m.item.title}
              </div>
              <div class="search-result-desc">${m.item.shortDesc}</div>
            </a>
          `;
        } else {
          return `
            <a class="search-result-item" href="#/glossary?term=${encodeURIComponent(m.item.term)}">
              <div class="search-result-title">
                <span class="badge badge-accent mr-1">Glossary</span>
                ${m.item.term}
              </div>
              <div class="search-result-desc">${m.item.definition}</div>
            </a>
          `;
        }
      }).join('');

      results.hidden = false;
    }, 150));

    // Hide search results on outside click
    document.addEventListener('click', (e) => {
      if (!input.contains(e.target) && !results.contains(e.target)) {
        results.hidden = true;
      }
    });
  }

  function updateBookmarkButton(id) {
    const btn = document.getElementById('bookmark-toggle');
    if (!btn) return;
    if (!id) {
      btn.style.display = 'none';
      return;
    }
    btn.style.display = 'inline-flex';
    const bookmarked = isBookmarked(id);
    btn.setAttribute('aria-label', bookmarked ? 'Remove bookmark' : 'Bookmark lesson');
    btn.classList.toggle('active', bookmarked);
    btn.innerHTML = bookmarked
      ? `<svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" style="color:var(--accent-gold)"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>`
      : `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>`;
  }

  function updateBreadcrumb(items) {
    const bc = document.getElementById('breadcrumb');
    if (!bc) return;
    bc.innerHTML = items.map((item, idx) => {
      if (idx === items.length - 1) {
        return `<span aria-current="page">${item.label}</span>`;
      }
      return `<a href="${item.href}">${item.label}</a>`;
    }).join(' <span class="bc-sep">/</span> ');
  }

  /* ─── HELPER: Module metadata ──────────────────────────────── */
  const MODULE_META = {
    foundations:   { label: 'Foundations',           color: 'var(--mod-f)', bg: '#8B5CF6', icon: 'F' },
    supervised:    { label: 'Classical Supervised',  color: 'var(--mod-s)', bg: '#3B82F6', icon: 'S' },
    unsupervised:  { label: 'Unsupervised',          color: 'var(--mod-u)', bg: '#0D9488', icon: 'U' },
    deeplearning:  { label: 'Deep Learning',         color: 'var(--mod-d)', bg: '#E11D48', icon: 'D' },
    advanced:      { label: 'Advanced & MLOps',      color: 'var(--mod-a)', bg: '#D97706', icon: 'A' }
  };

  function getModuleKey(lesson) {
    // Map from catalog module field to our key
    const mod = lesson.module;
    if (mod === 'deep' || mod === 'deeplearning') return 'deeplearning';
    return mod;
  }

  /* ═══════════════════════════════════════════════════════════════
     VIEW RENDERERS
     ═══════════════════════════════════════════════════════════════ */

  /* 1. HOME DASHBOARD — Card Grid */
  function renderHome(container) {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const catalog = FML.catalog || [];
    const completedCount = Object.values(state.progress).filter(p => p.completed).length;
    const nextLesson = catalog.find(l => !isCompleted(l.id)) || catalog[0];

    // Group by module
    const modules = {};
    catalog.forEach(l => {
      const key = getModuleKey(l);
      if (!modules[key]) modules[key] = [];
      modules[key].push(l);
    });

    const moduleOrder = ['foundations', 'supervised', 'unsupervised', 'deeplearning', 'advanced'];

    container.innerHTML = `
      <div style="max-width: var(--landing-max); margin: 0 auto;">

        <!-- Hero Banner -->
        <div class="landing-hero">
          <div class="landing-hero-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            Interactive Learning Lab
          </div>
          <h1>Master Machine Learning from Zero to State of the Art</h1>
          <p>
            An interactive curriculum with 52 rigorous lessons across foundations, classical supervised models, 
            representation learning, deep architectures, and production MLOps. Each lesson includes rich explanations, 
            inline interactive demos, and knowledge quizzes.
          </p>
          <div class="landing-hero-actions">
            ${nextLesson ? `
              <a href="#/lesson/${nextLesson.id}" class="btn-primary">
                <span>${completedCount === 0 ? 'Start Learning' : 'Continue Learning'}</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:16px;height:16px"><polyline points="9 18 15 12 9 6"/></svg>
              </a>
              <span class="landing-hero-meta">Next: <strong>${nextLesson.id} · ${nextLesson.title}</strong></span>
            ` : ''}
          </div>
        </div>

        <!-- Stats Bar -->
        <div class="stats-bar">
          <div class="stat-card">
            <div class="stat-value" style="color: var(--accent-indigo)">52</div>
            <div class="stat-label">Lessons</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" style="color: var(--accent-emerald)">${completedCount}</div>
            <div class="stat-label">Completed</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" style="color: var(--accent-gold)">Live</div>
            <div class="stat-label">Interactive Lab</div>
            <a href="#/lab" class="stat-link">Launch →</a>
          </div>
          <div class="stat-card">
            <div class="stat-value" style="color: var(--accent-rose)">${(FML.glossaryTerms || []).length}</div>
            <div class="stat-label">Glossary Terms</div>
            <a href="#/glossary" class="stat-link">Explore →</a>
          </div>
        </div>

        <!-- Module Sections with Topic Cards -->
        ${moduleOrder.map(modKey => {
          const meta = MODULE_META[modKey];
          const lessons = modules[modKey] || [];
          if (lessons.length === 0) return '';
          return `
            <div class="module-section">
              <div class="module-header">
                <div class="module-icon" style="background: ${meta.bg}">${meta.icon}</div>
                <h2>${meta.label}</h2>
                <span class="module-count">${lessons.length} lessons</span>
              </div>
              <div class="topic-cards">
                ${lessons.map(l => {
                  const done = isCompleted(l.id);
                  return `
                    <a class="topic-card" href="#/lesson/${l.id}" data-module="${modKey}">
                      <div class="topic-card-head">
                        <span class="topic-card-id">${l.id}</span>
                        <span class="topic-card-level ${l.level}">${l.level}</span>
                      </div>
                      <h3>${l.title}</h3>
                      <div class="topic-card-desc">${l.shortDesc}</div>
                      <div class="topic-card-footer">
                        ${done
                          ? `<span class="topic-card-status completed">✓ Completed</span>`
                          : `<span class="topic-card-time">⏱ ${l.estimatedMinutes} min</span>`
                        }
                        <span class="topic-card-arrow">Learn →</span>
                      </div>
                    </a>
                  `;
                }).join('')}
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }


  /* ═══════════════════════════════════════════════════════════════
     2. BLOG-STYLE LESSON PAGE (colah's blog inspired)
     ═══════════════════════════════════════════════════════════════ */
  function renderLesson(container, lessonId) {
    const lesson = (FML.catalog || []).find(l => l.id === lessonId);
    if (!lesson) {
      container.innerHTML = `
        <div class="card p-6 text-center" style="max-width:500px;margin:80px auto;">
          <h2 class="text-lg font-bold mb-2">Lesson Not Found</h2>
          <p class="text-secondary text-sm mb-4">Lesson "${lessonId}" does not exist in the curriculum catalog.</p>
          <a href="#/catalog" class="btn-primary">Browse All Lessons</a>
        </div>
      `;
      return;
    }

    state.currentLessonId = lesson.id;
    updateBookmarkButton(lesson.id);

    const modKey = getModuleKey(lesson);
    const meta = MODULE_META[modKey] || MODULE_META.foundations;

    updateBreadcrumb([
      { label: 'Home', href: '#/' },
      { label: meta.label, href: `#/catalog?module=${lesson.module}` },
      { label: `${lesson.id}: ${lesson.title}`, href: `#/lesson/${lesson.id}` }
    ]);

    const completed = isCompleted(lesson.id);
    const sec = lesson.sections;

    // Build the blog-style HTML
    let blogHTML = `<div class="blog-lesson">`;

    // ─── HEADER ───
    blogHTML += `
      <div class="blog-header">
        <div class="blog-meta">
          <span class="blog-module-badge" style="background: ${meta.bg}">${meta.icon} ${meta.label}</span>
          <span class="badge badge-subtle uppercase">${lesson.level}</span>
          <span class="reading-time">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            ~${lesson.estimatedMinutes} min read
          </span>
          ${completed ? '<span class="badge badge-teal">✓ Completed</span>' : ''}
        </div>
        <h1>${lesson.title}</h1>
        <p class="blog-subtitle">${lesson.shortDesc}</p>
        <div class="blog-tags">
          ${(lesson.tags || []).map(t => `<span class="blog-tag">#${t}</span>`).join('')}
        </div>
        ${lesson.prerequisites && lesson.prerequisites.length > 0 ? `
          <div class="prereq-chips">
            <span class="text-xs text-muted font-semibold">Prerequisites:</span>
            ${lesson.prerequisites.map(pid => {
              const prereq = (FML.catalog || []).find(l => l.id === pid);
              return `<a class="prereq-chip" href="#/lesson/${pid}">${pid}${prereq ? ': ' + prereq.title : ''}</a>`;
            }).join('')}
          </div>
        ` : ''}
      </div>
    `;

    // ─── ARTICLE BODY (blog-prose) ───
    blogHTML += `<article class="blog-prose">`;

    // Section: What It Is
    if (sec.whatItIs) {
      blogHTML += `<h2>What It Is</h2>`;
      blogHTML += `<p>${sec.whatItIs}</p>`;
    }

    // Section: Problem It Solves
    if (sec.problemItSolves) {
      blogHTML += `<h2>The Problem It Solves</h2>`;
      blogHTML += `<p>${sec.problemItSolves}</p>`;
    }

    // Section: Intuition (callout)
    if (sec.intuition) {
      blogHTML += `
        <div class="blog-callout intuition">
          <div class="blog-callout-title">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a7 7 0 0 0-3 13.33V18h6v-2.67A7 7 0 0 0 12 2z"/><path d="M9 21h6"/><path d="M10 18h4"/></svg>
            Conceptual Intuition
          </div>
          <p>${sec.intuition}</p>
        </div>
      `;
    }

    // Section: How It Works (step-by-step)
    if (sec.howItWorks) {
      blogHTML += `<h2>How It Works</h2>`;
      blogHTML += `<div>${sec.howItWorks}</div>`;
    }

    // Section: Mathematics
    if (sec.mathematics) {
      blogHTML += `<h2>Mathematical Formulation</h2>`;
      blogHTML += `<div class="math-content">${sec.mathematics}</div>`;
    }

    // ─── INLINE INTERACTIVE DEMO ───
    blogHTML += `
      <div class="blog-demo-section">
        <div class="blog-demo-header">
          <div class="blog-demo-title">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            Interactive Playground
          </div>
          <span class="blog-demo-badge">Live Demo</span>
        </div>
        <div class="blog-demo-body" id="lesson-demo-container">
          <div class="demo-panel" id="active-demo-panel"></div>
        </div>
        <div class="blog-demo-caption" id="demo-caption">
          <strong>🧪 Experiment:</strong> Use the controls above to adjust parameters and see how the model's behavior changes in real time.
        </div>
      </div>
    `;

    // Section: Data Requirements
    if (sec.dataRequirements) {
      blogHTML += `<h2>Data Requirements</h2>`;
      blogHTML += `<p>${sec.dataRequirements}</p>`;
    }

    // Section: Hyperparameters (table)
    if (sec.hyperparameters && sec.hyperparameters.length > 0) {
      blogHTML += `<h2>Key Hyperparameters</h2>`;
      blogHTML += `
        <div class="blog-table-wrap">
          <table class="blog-table">
            <thead>
              <tr><th>Hyperparameter</th><th>Description</th><th>Effect</th></tr>
            </thead>
            <tbody>
              ${sec.hyperparameters.map(h => `
                <tr>
                  <td><strong>${h.name}</strong></td>
                  <td>${h.description}</td>
                  <td>${h.effect}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    // Section: Strengths & Limitations (pros/cons grid)
    if ((sec.strengths && sec.strengths.length > 0) || (sec.limitations && sec.limitations.length > 0)) {
      blogHTML += `<h2>Strengths & Limitations</h2>`;
      blogHTML += `<div class="pros-cons-grid">`;
      if (sec.strengths && sec.strengths.length > 0) {
        blogHTML += `
          <div class="pros-card">
            <h4>✓ Strengths</h4>
            <ul>${sec.strengths.map(s => `<li>${s}</li>`).join('')}</ul>
          </div>
        `;
      }
      if (sec.limitations && sec.limitations.length > 0) {
        blogHTML += `
          <div class="cons-card">
            <h4>✗ Limitations</h4>
            <ul>${sec.limitations.map(l => `<li>${l}</li>`).join('')}</ul>
          </div>
        `;
      }
      blogHTML += `</div>`;
    }

    // Section: When To Use
    if (sec.whenToUse) {
      blogHTML += `<h2>When To Use</h2>`;
      blogHTML += `<p>${sec.whenToUse}</p>`;
    }

    // Section: Evaluation
    if (sec.evaluation) {
      blogHTML += `<h2>Evaluation & Validation</h2>`;
      blogHTML += `<p>${sec.evaluation}</p>`;
    }

    // Section: Worked Example
    if (sec.workedExample) {
      blogHTML += `
        <div class="blog-callout info">
          <div class="blog-callout-title">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            Real-World Worked Example
          </div>
          <p>${sec.workedExample}</p>
        </div>
      `;
    }

    // Section: Common Mistakes (warning callout)
    if (sec.commonMistakes && sec.commonMistakes.length > 0) {
      blogHTML += `
        <div class="blog-callout warning">
          <div class="blog-callout-title">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            Common Pitfalls to Avoid
          </div>
          <ul style="padding-left:18px;">
            ${sec.commonMistakes.map(m => `<li>${m}</li>`).join('')}
          </ul>
        </div>
      `;
    }

    // Section: Further Learning
    if (sec.furtherLearning && sec.furtherLearning.length > 0) {
      blogHTML += `
        <div class="blog-further">
          <h3>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;color:var(--accent-indigo)"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
            Further Reading
          </h3>
          <ul>
            ${sec.furtherLearning.map(fl => `
              <li>
                <a href="${fl.url}" target="_blank" rel="noopener noreferrer">
                  📖 ${fl.title}
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:12px;height:12px"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    blogHTML += `</article>`; // close blog-prose

    // ─── QUIZ SECTION ───
    blogHTML += `
      <div class="blog-quiz" id="blog-quiz-section">
        <div class="blog-quiz-header">
          <h3>Knowledge Check</h3>
          <span class="badge badge-accent">${(lesson.quiz || []).length} Questions</span>
        </div>
        <div class="blog-quiz-body" id="quiz-container"></div>
        <div class="quiz-summary" id="quiz-summary-bar">
          <button class="btn-primary" id="submit-quiz-btn">Submit Answers</button>
          <div class="text-sm font-semibold" id="quiz-score-badge" style="display:none"></div>
        </div>
      </div>
    `;

    // ─── COMPLETION BANNER ───
    blogHTML += `
      <div class="blog-completion" id="completion-banner">
        <div>
          <h4>${completed ? '✓ Lesson Completed!' : 'Ready to finish this lesson?'}</h4>
          <p>${completed ? 'Your progress has been recorded in your local browser.' : 'Mark this lesson as complete to track your progress.'}</p>
        </div>
        <button class="btn-primary" id="toggle-complete-btn">
          ${completed ? 'Completed ✓' : 'Mark as Complete'}
        </button>
      </div>
    `;

    blogHTML += `</div>`; // close blog-lesson

    container.innerHTML = blogHTML;

    // Render KaTeX Math
    U.renderMath(container);

    // Initialize Demo
    const demoPanel = container.querySelector('#active-demo-panel');
    if (demoPanel && FML.initDemoForLesson) {
      FML.initDemoForLesson(lesson.id, demoPanel);
    }

    // Render Quiz
    renderQuiz(container.querySelector('#quiz-container'), lesson);

    // Complete Button
    const compBtn = container.querySelector('#toggle-complete-btn');
    if (compBtn) {
      compBtn.addEventListener('click', () => {
        const nextState = !isCompleted(lesson.id);
        saveProgress(lesson.id, nextState);
        renderLesson(container, lesson.id);
        U.toast(nextState ? `Completed ${lesson.id}!` : `Marked ${lesson.id} incomplete`, 'success');
      });
    }

    // Configure Prev / Next Navigation Footer
    setupLessonNavFooter(lesson);
  }

  function setupLessonNavFooter(lesson) {
    const catalog = FML.catalog || [];
    const idx = catalog.findIndex(l => l.id === lesson.id);
    const footer = document.getElementById('lesson-nav-footer');
    const prevBtn = document.getElementById('prev-lesson');
    const nextBtn = document.getElementById('next-lesson');
    const prevLbl = document.getElementById('prev-lesson-label');
    const nextLbl = document.getElementById('next-lesson-label');

    if (!footer) return;
    footer.hidden = false;

    if (idx > 0) {
      prevBtn.style.display = 'inline-flex';
      const prevL = catalog[idx - 1];
      prevLbl.textContent = `${prevL.id}: ${prevL.title}`;
      prevBtn.onclick = () => { window.location.hash = `#/lesson/${prevL.id}`; };
    } else {
      prevBtn.style.display = 'none';
    }

    if (idx < catalog.length - 1) {
      nextBtn.style.display = 'inline-flex';
      const nextL = catalog[idx + 1];
      nextLbl.textContent = `${nextL.id}: ${nextL.title}`;
      nextBtn.onclick = () => { window.location.hash = `#/lesson/${nextL.id}`; };
    } else {
      nextBtn.style.display = 'none';
    }
  }

  /* 3. Quiz Component */
  function renderQuiz(container, lesson) {
    const quiz = lesson.quiz || [];
    if (quiz.length === 0) {
      container.innerHTML = `<div class="p-4 text-xs text-muted">No quiz questions available.</div>`;
      return;
    }

    let answers = {};
    container.innerHTML = `
      <div class="quiz-questions">
        ${quiz.map((q, qIdx) => `
          <div class="quiz-q" data-qidx="${qIdx}">
            <p>${qIdx + 1}. ${q.question}</p>
            <div class="quiz-options">
              ${q.options.map((opt, oIdx) => `
                <div class="quiz-opt" data-oidx="${oIdx}">
                  <span class="quiz-opt-marker font-mono">${String.fromCharCode(65 + oIdx)}</span>
                  <span class="quiz-opt-text">${opt}</span>
                </div>
              `).join('')}
            </div>
            <div class="quiz-feedback" style="display:none"></div>
          </div>
        `).join('')}
      </div>
    `;

    // Handle Option Selection
    container.querySelectorAll('.quiz-q').forEach(qEl => {
      const qIdx = parseInt(qEl.getAttribute('data-qidx'));
      qEl.querySelectorAll('.quiz-opt').forEach(optEl => {
        optEl.addEventListener('click', () => {
          qEl.querySelectorAll('.quiz-opt').forEach(o => o.classList.remove('selected'));
          optEl.classList.add('selected');
          answers[qIdx] = parseInt(optEl.getAttribute('data-oidx'));
        });
      });
    });

    // Handle Submit
    const submitBtn = document.getElementById('submit-quiz-btn');
    const scoreBadge = document.getElementById('quiz-score-badge');

    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        let score = 0;
        quiz.forEach((q, qIdx) => {
          const qEl = container.querySelector(`[data-qidx="${qIdx}"]`);
          const userChoice = answers[qIdx];
          const fbEl = qEl.querySelector('.quiz-feedback');

          qEl.querySelectorAll('.quiz-opt').forEach(optEl => {
            const oIdx = parseInt(optEl.getAttribute('data-oidx'));
            if (oIdx === q.correct) optEl.classList.add('correct');
            if (userChoice === oIdx && userChoice !== q.correct) optEl.classList.add('incorrect');
          });

          fbEl.style.display = 'block';
          if (userChoice === q.correct) {
            score++;
            fbEl.innerHTML = `<span style="color:var(--accent-emerald)">✓ Correct!</span> ${q.explanation}`;
          } else {
            fbEl.innerHTML = `<span style="color:var(--accent-rose)">✗ Incorrect.</span> ${q.explanation}`;
          }
        });

        if (scoreBadge) {
          scoreBadge.style.display = 'block';
          scoreBadge.innerHTML = `Score: <strong>${score} / ${quiz.length}</strong> (${Math.round((score/quiz.length)*100)}%)`;
        }

        if (score === quiz.length) {
          saveProgress(lesson.id, true, score);
          U.toast('Perfect Score! Lesson completed.', 'success');
        }
      });
    }

    U.renderMath(container);
  }

  /* 4. Full Catalog Grid View */
  function renderCatalog(container, queryParams = {}) {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }, { label: 'Full Catalog', href: '#/catalog' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const catalog = FML.catalog || [];
    let selectedModule = queryParams.module || 'all';

    container.innerHTML = `
      <div style="max-width: var(--landing-max); margin: 0 auto;">
        <div class="mb-6">
          <h1 class="text-2xl font-bold mb-2" style="color:var(--text-heading)">Curriculum Catalog</h1>
          <p class="text-sm text-secondary">Browse all 52 topics across 5 modules.</p>
        </div>

        <!-- Filter Chips -->
        <div class="demo-presets mb-6" id="catalog-filters">
          <button class="preset-btn ${selectedModule === 'all' ? 'active' : ''}" data-mod="all">All (52)</button>
          <button class="preset-btn ${selectedModule === 'foundations' ? 'active' : ''}" data-mod="foundations">Foundations (7)</button>
          <button class="preset-btn ${selectedModule === 'supervised' ? 'active' : ''}" data-mod="supervised">Supervised (13)</button>
          <button class="preset-btn ${selectedModule === 'unsupervised' ? 'active' : ''}" data-mod="unsupervised">Unsupervised (8)</button>
          <button class="preset-btn ${selectedModule === 'deeplearning' ? 'active' : ''}" data-mod="deeplearning">Deep Learning (16)</button>
          <button class="preset-btn ${selectedModule === 'advanced' ? 'active' : ''}" data-mod="advanced">Advanced (8)</button>
        </div>

        <div class="topic-cards" id="catalog-grid"></div>
      </div>
    `;

    const grid = container.querySelector('#catalog-grid');
    function renderGrid(mod) {
      const filtered = mod === 'all' ? catalog : catalog.filter(l => getModuleKey(l) === mod);
      grid.innerHTML = filtered.map(l => {
        const done = isCompleted(l.id);
        const modKey = getModuleKey(l);
        return `
          <a class="topic-card" href="#/lesson/${l.id}" data-module="${modKey}">
            <div class="topic-card-head">
              <span class="topic-card-id">${l.id}</span>
              <span class="topic-card-level ${l.level}">${l.level}</span>
            </div>
            <h3>${l.title}</h3>
            <div class="topic-card-desc">${l.shortDesc}</div>
            <div class="topic-card-footer">
              ${done
                ? `<span class="topic-card-status completed">✓ Completed</span>`
                : `<span class="topic-card-time">⏱ ${l.estimatedMinutes} min</span>`
              }
              <span class="topic-card-arrow">Learn →</span>
            </div>
          </a>
        `;
      }).join('');
    }

    renderGrid(selectedModule);

    container.querySelectorAll('#catalog-filters .preset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        container.querySelectorAll('#catalog-filters .preset-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderGrid(btn.getAttribute('data-mod'));
      });
    });
  }

  /* 5. Learning Paths View */
  function renderLearningPath(container, pathLevel = 'beginner') {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }, { label: 'Learning Paths', href: '#/path/beginner' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const catalog = FML.catalog || [];

    const paths = {
      beginner: {
        title: "Beginner Track: Fundamentals to Tabular Mastery",
        desc: "Build a rock-solid mathematical intuition for datasets, classification, regression, decision trees, and validation.",
        ids: ["F01", "F02", "F03", "F04", "F05", "F06", "S01", "S02", "S03", "S04", "S05", "U01"]
      },
      intermediate: {
        title: "Intermediate Track: Ensembles, Deep Learning & Representation",
        desc: "Master state-of-the-art gradient boosted trees (XGBoost), Support Vector Machines, neural activations, CNNs, and embeddings.",
        ids: ["S06", "S08", "S09", "S10", "S11", "S13", "U03", "U05", "D01", "D02", "D03", "D06", "D12"]
      },
      advanced: {
        title: "Advanced Track: Modern Foundation Models & Systems",
        desc: "Explore Transformers, Large Language Models, Diffusion models, Reinforcement Learning, and Production MLOps.",
        ids: ["D11", "D13", "D14", "D15", "D16", "A01", "A02", "A05", "A06", "A07", "A08"]
      }
    };

    const current = paths[pathLevel] || paths.beginner;

    container.innerHTML = `
      <div style="max-width: var(--content-max); margin: 0 auto;">
        <div class="mb-6">
          <h1 class="text-2xl font-bold mb-2" style="color:var(--text-heading)">Structured Learning Paths</h1>
          <p class="text-sm text-secondary">Follow a sequential, curated track designed for your current experience level.</p>
        </div>

        <div class="demo-presets mb-6">
          <a href="#/path/beginner" class="preset-btn ${pathLevel === 'beginner' ? 'active' : ''}">Beginner Track</a>
          <a href="#/path/intermediate" class="preset-btn ${pathLevel === 'intermediate' ? 'active' : ''}">Intermediate Track</a>
          <a href="#/path/advanced" class="preset-btn ${pathLevel === 'advanced' ? 'active' : ''}">Advanced Track</a>
        </div>

        <div class="card p-5 mb-6" style="border-left: 3px solid var(--accent-indigo)">
          <h2 class="text-lg font-bold mb-1" style="color:var(--text-heading)">${current.title}</h2>
          <p class="text-sm text-secondary leading-relaxed">${current.desc}</p>
        </div>

        <div class="space-y-3">
          ${current.ids.map((id, stepIdx) => {
            const l = catalog.find(x => x.id === id);
            if (!l) return '';
            const done = isCompleted(id);
            return `
              <div class="card p-4 flex items-center justify-between flex-wrap gap-3 ${done ? 'border-teal' : ''}">
                <div class="flex items-center gap-3">
                  <span class="w-7 h-7 flex items-center justify-center" style="border-radius:50%; background:${done ? 'rgba(52,211,153,0.15)' : 'var(--bg-elevated)'}; color:${done ? '#34d399' : 'var(--text-muted)'}; font-size:0.75rem; font-weight:700; font-family:var(--font-mono)">
                    ${stepIdx + 1}
                  </span>
                  <div>
                    <div class="flex items-center gap-2">
                      <span class="badge badge-subtle font-mono text-xs">${l.id}</span>
                      <h3 class="font-bold text-sm" style="color:var(--text-primary)">${l.title}</h3>
                    </div>
                    <p class="text-xs text-secondary mt-1">${l.shortDesc}</p>
                  </div>
                </div>
                <div class="flex items-center gap-3">
                  <span class="text-xs text-muted">~${l.estimatedMinutes}m</span>
                  <a href="#/lesson/${l.id}" class="btn-outline text-xs">${done ? 'Review' : 'Start'} →</a>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    `;
  }

  /* 6. Glossary View */
  function renderGlossary(container, queryParams = {}) {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }, { label: 'Glossary', href: '#/glossary' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const terms = FML.glossaryTerms || [];
    const filterTerm = queryParams.term || '';

    container.innerHTML = `
      <div style="max-width: var(--landing-max); margin: 0 auto;">
        <div class="mb-6">
          <h1 class="text-2xl font-bold mb-2" style="color:var(--text-heading)">ML Technical Glossary</h1>
          <p class="text-sm text-secondary">${terms.length} verified terms with rigorous definitions.</p>
        </div>

        <div class="mb-4">
          <input type="search" id="glossary-search-input" class="search-input" placeholder="Filter terms…" value="${filterTerm}" style="width:100%;padding:10px 14px;border:1px solid var(--border-color);border-radius:var(--radius);background:var(--bg-surface);color:var(--text-primary);font-size:0.875rem;">
        </div>

        <div class="grid grid-2 gap-3" id="glossary-grid"></div>
      </div>
    `;

    const gGrid = container.querySelector('#glossary-grid');
    const gInput = container.querySelector('#glossary-search-input');

    function filterAndRender(q) {
      const qLow = q.trim().toLowerCase();
      const matched = terms.filter(t => t.term.toLowerCase().includes(qLow) || t.definition.toLowerCase().includes(qLow) || t.category.toLowerCase().includes(qLow));

      if (matched.length === 0) {
        gGrid.innerHTML = `<div class="p-6 text-xs text-muted" style="grid-column: 1 / -1; text-align:center">No glossary terms match "${q}"</div>`;
        return;
      }

      gGrid.innerHTML = matched.map(t => `
        <div class="card p-4 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-2">
              <h3 class="font-bold text-sm" style="color:var(--text-primary)">${t.term}</h3>
              <span class="badge badge-subtle text-xs">${t.category}</span>
            </div>
            <p class="text-xs text-secondary leading-relaxed mb-3">${t.definition}</p>
          </div>
          ${t.lessonId ? `
            <div class="pt-2 border-t border-subtle">
              <a href="#/lesson/${t.lessonId}" class="text-xs" style="color:var(--accent-indigo)">View in Lesson ${t.lessonId} →</a>
            </div>
          ` : ''}
        </div>
      `).join('');

      U.renderMath(gGrid);
    }

    filterAndRender(filterTerm);
    gInput.addEventListener('input', (e) => filterAndRender(e.target.value));
  }

  /* 7. Progress Dashboard */
  function renderProgress(container) {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }, { label: 'My Progress', href: '#/progress' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const catalog = FML.catalog || [];
    const completed = catalog.filter(l => isCompleted(l.id));
    const pct = Math.round((completed.length / catalog.length) * 100);

    container.innerHTML = `
      <div style="max-width: var(--content-max); margin: 0 auto;">
        <div class="mb-6">
          <h1 class="text-2xl font-bold mb-2" style="color:var(--text-heading)">My Learning Progress</h1>
          <p class="text-sm text-secondary">All progress is stored in your private browser localStorage.</p>
        </div>

        <div class="card p-6 mb-6 flex items-center justify-between flex-wrap gap-4" style="background: linear-gradient(135deg, rgba(52,211,153,0.06), rgba(99,102,241,0.06))">
          <div>
            <div class="text-3xl font-bold font-mono mb-1" style="color:var(--accent-emerald)">${completed.length} / ${catalog.length}</div>
            <div class="text-xs text-secondary">Lessons Completed (${pct}%)</div>
          </div>
          <button class="btn-outline text-xs" id="reset-progress-btn" style="color:var(--accent-rose)">Reset All Progress</button>
        </div>

        <h3 class="font-bold text-sm mb-3" style="color:var(--text-heading)">Completed Lessons</h3>
        ${completed.length === 0 ? `
          <div class="card p-6 text-center text-xs text-muted">
            You haven't completed any lessons yet. Start with <a href="#/lesson/F01" style="color:var(--accent-indigo)">F01: AI, ML & Deep Learning</a>!
          </div>
        ` : `
          <div class="grid grid-2 gap-3 mb-6">
            ${completed.map(l => `
              <div class="card p-4 flex items-center justify-between">
                <div>
                  <span class="badge badge-subtle font-mono text-xs mr-1">${l.id}</span>
                  <span class="font-semibold text-xs" style="color:var(--text-primary)">${l.title}</span>
                </div>
                <a href="#/lesson/${l.id}" class="text-xs" style="color:var(--accent-indigo)">Review →</a>
              </div>
            `).join('')}
          </div>
        `}
      </div>
    `;

    const resetBtn = container.querySelector('#reset-progress-btn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        if (confirm('Are you sure you want to reset all your curriculum progress?')) {
          state.progress = {};
          U.save('fml_progress', {});
          updateSidebarProgress();
          renderProgress(container);
          U.toast('Progress reset', 'info');
        }
      });
    }
  }

  /* 8. Bookmarks View */
  function renderBookmarks(container) {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }, { label: 'Bookmarks', href: '#/bookmarks' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const catalog = FML.catalog || [];
    const bookmarked = catalog.filter(l => isBookmarked(l.id));

    container.innerHTML = `
      <div style="max-width: var(--content-max); margin: 0 auto;">
        <div class="mb-6">
          <h1 class="text-2xl font-bold mb-2" style="color:var(--text-heading)">Bookmarked Lessons</h1>
          <p class="text-sm text-secondary">Quick access to lessons you have pinned for revision.</p>
        </div>

        ${bookmarked.length === 0 ? `
          <div class="card p-8 text-center text-xs text-muted">
            No lessons bookmarked yet. Click the bookmark icon at the top of any lesson page to save it here.
          </div>
        ` : `
          <div class="grid grid-2 gap-3">
            ${bookmarked.map(l => `
              <div class="card p-4 flex items-center justify-between">
                <div>
                  <span class="badge badge-subtle font-mono text-xs mr-1">${l.id}</span>
                  <span class="font-semibold text-xs" style="color:var(--text-primary)">${l.title}</span>
                  <div class="text-xs text-muted mt-1">~${l.estimatedMinutes} min · ${l.level}</div>
                </div>
                <div class="flex items-center gap-2">
                  <a href="#/lesson/${l.id}" class="btn-outline text-xs">Open →</a>
                </div>
              </div>
            `).join('')}
          </div>
        `}
      </div>
    `;
  }

  /* ─── SPA ROUTER ─────────────────────────────────────────── */
  function route() {
    const rawHash = window.location.hash.slice(1) || '/';
    const [path, queryString] = rawHash.split('?');
    const params = new URLSearchParams(queryString || '');
    const queryObj = Object.fromEntries(params.entries());

    const pageContent = document.getElementById('page-content');
    if (!pageContent) return;

    window.scrollTo(0, 0);

    // Active route highlighting in sidebar
    document.querySelectorAll('.sidebar-nav .nav-item').forEach(el => {
      el.classList.remove('active');
    });

    if (path === '/' || path === '') {
      const homeLink = document.querySelector('.nav-item[data-route="home"]');
      if (homeLink) homeLink.classList.add('active');
      renderHome(pageContent);
    } else if (path.startsWith('/lesson/')) {
      const lessonId = path.split('/')[2];
      renderLesson(pageContent, lessonId);
    } else if (path.startsWith('/path/')) {
      const level = path.split('/')[2] || 'beginner';
      const pathLink = document.querySelector('.nav-item[data-route="path"]');
      if (pathLink) pathLink.classList.add('active');
      renderLearningPath(pageContent, level);
    } else if (path === '/lab') {
      const labLink = document.querySelector('.nav-item[data-route="lab"]');
      if (labLink) labLink.classList.add('active');
      state.currentLessonId = null;
      updateBookmarkButton(null);
      updateBreadcrumb([{ label: 'Home', href: '#/' }, { label: 'Learning Lab', href: '#/lab' }]);
      document.getElementById('lesson-nav-footer').hidden = true;
      FML.lab.initLab(pageContent);
    } else if (path === '/catalog') {
      const catLink = document.querySelector('.nav-item[data-route="catalog"]');
      if (catLink) catLink.classList.add('active');
      renderCatalog(pageContent, queryObj);
    } else if (path === '/glossary') {
      const gloLink = document.querySelector('.nav-item[data-route="glossary"]');
      if (gloLink) gloLink.classList.add('active');
      renderGlossary(pageContent, queryObj);
    } else if (path === '/progress') {
      const progLink = document.querySelector('.nav-item[data-route="progress"]');
      if (progLink) progLink.classList.add('active');
      renderProgress(pageContent);
    } else if (path === '/bookmarks') {
      const bmkLink = document.querySelector('.nav-item[data-route="bookmarks"]');
      if (bmkLink) bmkLink.classList.add('active');
      renderBookmarks(pageContent);
    } else {
      renderHome(pageContent);
    }

    updateSidebarProgress();
  }

  /* ─── INITIALIZATION ──────────────────────────────────────── */
  function init() {
    initTheme();
    initSidebarAccordions();
    initSearch();

    const bmkBtn = document.getElementById('bookmark-toggle');
    if (bmkBtn) {
      bmkBtn.addEventListener('click', () => {
        if (state.currentLessonId) toggleBookmark(state.currentLessonId);
      });
    }

    window.addEventListener('hashchange', route);
    route();

    document.body.classList.add('ready');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Exports
  return {
    saveProgress,
    isCompleted,
    toggleBookmark,
    isBookmarked,
    route
  };
})();
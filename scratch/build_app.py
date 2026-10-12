# -*- coding: utf-8 -*-
"""
App Builder for Free Mind ML
Generates js/app.js containing the full Single Page Application logic:
- Hash Router
- Lesson View Renderer (15 sections, tabs, KaTeX math, quizzes, progress)
- Home Dashboard
- Learning Paths
- Full Catalog View with Filters
- Glossary View with Search
- Progress View
- Bookmarks View
- Search Modal & Ctrl+K Shortcut
- Theme Switcher
- Responsive Sidebar & Hamburger
"""
import os

script_content = r'''/* ============================================================
   FREE MIND ML — app.js
   Master Application Controller: Router, State, Views, UI Logic
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
    theme: U.load('fml_theme', 'dark')
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

    // Mobile Hamburger
    const burger = document.getElementById('hamburger');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('sidebar-close');

    if (burger && sidebar) {
      burger.addEventListener('click', () => {
        const open = sidebar.classList.toggle('open');
        burger.setAttribute('aria-expanded', open);
      });
    }
    if (closeBtn && sidebar) {
      closeBtn.addEventListener('click', () => {
        sidebar.classList.remove('open');
        if (burger) burger.setAttribute('aria-expanded', 'false');
      });
    }

    // Close sidebar on link click on small screen
    document.querySelectorAll('.sidebar-nav a').forEach(a => {
      a.addEventListener('click', () => {
        if (window.innerWidth <= 1024 && sidebar) {
          sidebar.classList.remove('open');
          if (burger) burger.setAttribute('aria-expanded', 'false');
        }
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
        results.innerHTML = `<div class="p-3 text-xs text-muted">No matching topics found for "${q}"</div>`;
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

  /* ─── VIEW RENDERERS ──────────────────────────────────────── */

  /* 1. Home Dashboard */
  function renderHome(container) {
    state.currentLessonId = null;
    updateBookmarkButton(null);
    updateBreadcrumb([{ label: 'Home', href: '#/' }]);
    document.getElementById('lesson-nav-footer').hidden = true;

    const catalog = FML.catalog || [];
    const completedCount = Object.values(state.progress).filter(p => p.completed).length;

    // Pick next uncompleted lesson
    const nextLesson = catalog.find(l => !isCompleted(l.id)) || catalog[0];

    container.innerHTML = `
      <div class="home-view">
        <!-- Hero Banner -->
        <div class="card p-6 mb-6" style="background: linear-gradient(135deg, rgba(99,102,241,0.08) 0%, rgba(240,192,64,0.04) 100%);">
          <div class="flex items-center justify-between flex-wrap gap-4">
            <div>
              <div class="badge badge-accent mb-2">Curated Machine Learning Lab</div>
              <h1 class="page-title text-3xl mb-2" style="font-family:var(--font-serif)">Master Machine Learning from Zero to State of the Art</h1>
              <p class="text-secondary max-w-2xl text-sm leading-relaxed">
                An interactive paired curriculum: 52 rigorous lessons across foundations, classical supervised models, representation learning, deep architectures, and production MLOps. No account required.
              </p>
            </div>
            ${nextLesson ? `
              <div class="flex flex-col gap-2">
                <a href="#/lesson/${nextLesson.id}" class="btn-primary">
                  <span>${completedCount === 0 ? 'Start Curriculum' : 'Resume Learning'}</span>
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px"><polyline points="9 18 15 12 9 6"/></svg>
                </a>
                <span class="text-xs text-muted text-center">Next: <strong>${nextLesson.id} · ${nextLesson.title}</strong></span>
              </div>
            ` : ''}
          </div>
        </div>

        <!-- Metric Strips -->
        <div class="grid grid-4 gap-4 mb-6">
          <div class="card p-4">
            <div class="text-xs uppercase font-semibold text-muted mb-1">Total Curriculum</div>
            <div class="text-2xl font-bold" style="font-family:var(--font-mono); color:var(--text-primary)">52 Lessons</div>
            <div class="text-xs text-secondary mt-1">Across 5 structured modules</div>
          </div>
          <div class="card p-4">
            <div class="text-xs uppercase font-semibold text-muted mb-1">Completed</div>
            <div class="text-2xl font-bold" style="font-family:var(--font-mono); color:var(--accent-teal)">${completedCount} / 52</div>
            <div class="text-xs text-secondary mt-1">${Math.round((completedCount/52)*100)}% progress saved locally</div>
          </div>
          <div class="card p-4">
            <div class="text-xs uppercase font-semibold text-muted mb-1">Interactive Sandbox</div>
            <div class="text-2xl font-bold" style="font-family:var(--font-mono); color:var(--accent-gold)">Live Lab</div>
            <div class="text-xs text-secondary mt-1"><a href="#/lab" style="color:var(--accent-indigo)">Launch sandbox →</a></div>
          </div>
          <div class="card p-4">
            <div class="text-xs uppercase font-semibold text-muted mb-1">Technical Terms</div>
            <div class="text-2xl font-bold" style="font-family:var(--font-mono); color:var(--accent-rose)">${(FML.glossaryTerms || []).length} Terms</div>
            <div class="text-xs text-secondary mt-1"><a href="#/glossary" style="color:var(--accent-indigo)">Explore glossary →</a></div>
          </div>
        </div>

        <!-- 5 Modules Showcase -->
        <h2 class="text-lg font-bold mb-4" style="color:var(--text-primary)">Curriculum Modules</h2>
        <div class="grid grid-2 gap-4 mb-8">
          ${renderModuleCard('foundations', 'Module 0: Foundations', '7 Lessons', 'Core taxonomy, datasets, loss formulation, data splits, and the bias-variance tradeoff.', 'F01', 'var(--mod-f)')}
          ${renderModuleCard('supervised', 'Module 1: Classical Supervised', '13 Lessons', 'Regression, decision trees, random forests, gradient boosting (XGBoost/LightGBM), and SVMs.', 'S01', 'var(--mod-s)')}
          ${renderModuleCard('unsupervised', 'Module 2: Unsupervised Learning', '8 Lessons', 'k-Means, DBSCAN, Gaussian Mixtures, PCA, t-SNE, UMAP, and Isolation Forests.', 'U01', 'var(--mod-u)')}
          ${renderModuleCard('deeplearning', 'Module 3: Deep Learning', '16 Lessons', 'Backpropagation, modern optimizers, CNNs, LSTMs, Transformers, Diffusion, and GNNs.', 'D01', 'var(--mod-d)')}
          ${renderModuleCard('advanced', 'Module 4: Advanced & MLOps', '8 Lessons', 'Reinforcement learning, Recommenders, Ensembles, Explainability (SHAP), and MLOps.', 'A01', 'var(--mod-a)')}
        </div>
      </div>
    `;
  }

  function renderModuleCard(modKey, title, count, desc, startId, color) {
    return `
      <div class="card p-5 flex flex-col justify-between" style="border-left: 3px solid ${color}">
        <div>
          <div class="flex items-center justify-between mb-2">
            <h3 class="font-bold text-base" style="color:var(--text-primary)">${title}</h3>
            <span class="badge badge-subtle">${count}</span>
          </div>
          <p class="text-xs text-secondary leading-relaxed mb-4">${desc}</p>
        </div>
        <div class="flex items-center justify-between pt-3 border-t border-subtle">
          <a href="#/lesson/${startId}" class="btn-outline text-xs">
            Start Module
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:12px;height:12px"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
          <a href="#/catalog?module=${modKey}" class="text-xs text-muted hover:text-primary">View all ${count}</a>
        </div>
      </div>
    `;
  }

  /* 2. Lesson Page Renderer */
  function renderLesson(container, lessonId) {
    const lesson = (FML.catalog || []).find(l => l.id === lessonId);
    if (!lesson) {
      container.innerHTML = `
        <div class="card p-6 text-center">
          <h2 class="text-lg font-bold mb-2">Lesson Not Found</h2>
          <p class="text-secondary text-sm mb-4">Lesson "${lessonId}" does not exist in the curriculum catalog.</p>
          <a href="#/catalog" class="btn-primary">Browse All Lessons</a>
        </div>
      `;
      return;
    }

    state.currentLessonId = lesson.id;
    updateBookmarkButton(lesson.id);
    updateBreadcrumb([
      { label: 'Home', href: '#/' },
      { label: lesson.module.toUpperCase(), href: `#/catalog?module=${lesson.module}` },
      { label: `${lesson.id}: ${lesson.title}`, href: `#/lesson/${lesson.id}` }
    ]);

    const completed = isCompleted(lesson.id);
    const sec = lesson.sections;

    container.innerHTML = `
      <div class="lesson-view">
        <!-- Hero Section -->
        <div class="lesson-hero mb-6">
          <div class="flex items-center gap-2 mb-2 flex-wrap">
            <span class="badge badge-subtle uppercase" style="color:${U.moduleColor(lesson.id)}">${lesson.module}</span>
            <span class="badge badge-accent uppercase">${lesson.level}</span>
            <span class="text-xs text-muted">⏱ ~${lesson.estimatedMinutes} min</span>
            ${completed ? '<span class="badge badge-teal">✓ Completed</span>' : ''}
          </div>
          <h1 class="lesson-title" style="font-family:var(--font-serif); font-size: 2.2rem; color: var(--text-primary); margin-bottom: 8px;">
            ${lesson.title}
          </h1>
          <p class="lesson-desc text-secondary text-sm max-w-3xl leading-relaxed">
            ${lesson.shortDesc}
          </p>

          <!-- Tags -->
          <div class="flex items-center gap-1 mt-3 flex-wrap">
            ${(lesson.tags || []).map(t => `<span class="badge badge-subtle text-xs">#${t}</span>`).join('')}
          </div>
        </div>

        <!-- Section Navigation Tabs -->
        <div class="lesson-tabs demo-presets mb-4" id="lesson-tab-bar">
          <button class="preset-btn active" data-tab="overview">1. Overview &amp; Intuition</button>
          <button class="preset-btn" data-tab="mechanics">2. Mechanics &amp; Mathematics</button>
          <button class="preset-btn" data-tab="demo">3. Interactive Demo</button>
          <button class="preset-btn" data-tab="tradeoffs">4. Tradeoffs &amp; Pitfalls</button>
          <button class="preset-btn" data-tab="quiz">5. Quiz &amp; Practice</button>
        </div>

        <!-- TAB 1: OVERVIEW & INTUITION -->
        <div class="lesson-tab-pane" id="pane-overview">
          <div class="card p-5 mb-4">
            <h3 class="text-base font-bold mb-2" style="color:var(--text-primary)">What It Is</h3>
            <p class="text-sm leading-relaxed text-secondary">${sec.whatItIs}</p>
          </div>

          <div class="card p-5 mb-4">
            <h3 class="text-base font-bold mb-2" style="color:var(--text-primary)">The Core Problem It Solves</h3>
            <p class="text-sm leading-relaxed text-secondary">${sec.problemItSolves}</p>
          </div>

          <div class="card p-5 mb-4" style="background: rgba(240,192,64,0.03); border-left: 3px solid var(--accent-gold)">
            <h3 class="text-base font-bold mb-2 flex items-center gap-2" style="color:var(--accent-gold)">
              <span>💡</span> Conceptual Intuition
            </h3>
            <p class="text-sm leading-relaxed text-secondary">${sec.intuition}</p>
          </div>

          ${sec.workedExample ? `
            <div class="card p-5 mb-4">
              <h3 class="text-base font-bold mb-2" style="color:var(--text-primary)">Real-World Worked Example</h3>
              <p class="text-sm leading-relaxed text-secondary">${sec.workedExample}</p>
            </div>
          ` : ''}
        </div>

        <!-- TAB 2: MECHANICS & MATHEMATICS -->
        <div class="lesson-tab-pane" id="pane-mechanics" style="display:none">
          <div class="card p-5 mb-4">
            <h3 class="text-base font-bold mb-3" style="color:var(--text-primary)">Algorithmic Mechanics (Step-by-Step)</h3>
            <div class="text-sm leading-relaxed text-secondary">${sec.howItWorks}</div>
          </div>

          <div class="card p-5 mb-4 math-section">
            <h3 class="text-base font-bold mb-3" style="color:var(--text-primary)">Mathematical Formulation</h3>
            <div class="math-content text-sm leading-relaxed" style="overflow-x:auto;">${sec.mathematics}</div>
          </div>

          <div class="card p-5 mb-4">
            <h3 class="text-base font-bold mb-2" style="color:var(--text-primary)">Data Requirements &amp; Preprocessing</h3>
            <p class="text-sm leading-relaxed text-secondary">${sec.dataRequirements}</p>
          </div>

          ${sec.hyperparameters && sec.hyperparameters.length > 0 ? `
            <div class="card p-5 mb-4">
              <h3 class="text-base font-bold mb-3" style="color:var(--text-primary)">Key Hyperparameters</h3>
              <div class="table-wrap">
                <table class="data-table">
                  <thead>
                    <tr><th>Hyperparameter</th><th>Description</th><th>Operational Effect</th></tr>
                  </thead>
                  <tbody>
                    ${sec.hyperparameters.map(h => `
                      <tr>
                        <td><strong>${h.name}</strong></td>
                        <td class="text-secondary">${h.description}</td>
                        <td class="text-muted">${h.effect}</td>
                      </tr>
                    `).join('')}
                  </tbody>
                </table>
              </div>
            </div>
          ` : ''}
        </div>

        <!-- TAB 3: INTERACTIVE DEMO -->
        <div class="lesson-tab-pane" id="pane-demo" style="display:none">
          <div id="lesson-demo-container"></div>
        </div>

        <!-- TAB 4: TRADEOFFS & PITFALLS -->
        <div class="lesson-tab-pane" id="pane-tradeoffs" style="display:none">
          <div class="grid grid-2 gap-4 mb-4">
            <div class="card p-5" style="border-top: 3px solid var(--accent-teal)">
              <h3 class="text-sm font-bold uppercase tracking-wider mb-3 flex items-center gap-2" style="color:var(--accent-teal)">
                <span>✓</span> Strengths &amp; Advantages
              </h3>
              <ul class="text-xs text-secondary space-y-2">
                ${(sec.strengths || []).map(s => `<li>• ${s}</li>`).join('')}
              </ul>
            </div>

            <div class="card p-5" style="border-top: 3px solid var(--accent-rose)">
              <h3 class="text-sm font-bold uppercase tracking-wider mb-3 flex items-center gap-2" style="color:var(--accent-rose)">
                <span>✗</span> Limitations &amp; Blindspots
              </h3>
              <ul class="text-xs text-secondary space-y-2">
                ${(sec.limitations || []).map(l => `<li>• ${l}</li>`).join('')}
              </ul>
            </div>
          </div>

          <div class="card p-5 mb-4">
            <h3 class="text-base font-bold mb-2" style="color:var(--text-primary)">When To Use</h3>
            <p class="text-sm leading-relaxed text-secondary">${sec.whenToUse}</p>
          </div>

          <div class="card p-5 mb-4">
            <h3 class="text-base font-bold mb-2" style="color:var(--text-primary)">Evaluation Metrics &amp; Validation</h3>
            <p class="text-sm leading-relaxed text-secondary">${sec.evaluation}</p>
          </div>

          ${sec.commonMistakes && sec.commonMistakes.length > 0 ? `
            <div class="card p-5 mb-4" style="background: rgba(244,63,94,0.03); border-left: 3px solid var(--accent-rose)">
              <h3 class="text-base font-bold mb-3 text-rose flex items-center gap-2">
                <span>⚠️</span> Common Implementation Pitfalls
              </h3>
              <ul class="text-xs text-secondary space-y-2">
                ${sec.commonMistakes.map(m => `<li>• ${m}</li>`).join('')}
              </ul>
            </div>
          ` : ''}

          ${sec.furtherLearning && sec.furtherLearning.length > 0 ? `
            <div class="card p-5 mb-4">
              <h3 class="text-base font-bold mb-3" style="color:var(--text-primary)">Primary Sources &amp; Further Reading</h3>
              <ul class="text-xs text-secondary space-y-2">
                ${sec.furtherLearning.map(fl => `<li>📖 <a href="${fl.url}" target="_blank" rel="noopener noreferrer" style="color:var(--accent-indigo)">${fl.title}</a></li>`).join('')}
              </ul>
            </div>
          ` : ''}
        </div>

        <!-- TAB 5: QUIZ & PRACTICE -->
        <div class="lesson-tab-pane" id="pane-quiz" style="display:none">
          <div id="quiz-container"></div>
        </div>

        <!-- Completion Banner -->
        <div class="card p-5 mt-6 flex items-center justify-between flex-wrap gap-4" id="completion-banner">
          <div>
            <h4 class="font-bold text-sm mb-1" style="color:var(--text-primary)">
              ${completed ? '✓ Lesson Completed!' : 'Ready to finish this lesson?'}
            </h4>
            <p class="text-xs text-secondary">
              ${completed ? 'Your progress has been recorded in your local browser storage.' : 'Mark this lesson as complete to advance your curriculum progress ring.'}
            </p>
          </div>
          <button class="btn-primary" id="toggle-complete-btn">
            ${completed ? 'Completed ✓' : 'Mark as Complete'}
          </button>
        </div>
      </div>
    `;

    // Render KaTeX Math
    U.renderMath(container);

    // Setup Tabs
    const tabBtns = container.querySelectorAll('#lesson-tab-bar .preset-btn');
    const panes = {
      overview: container.querySelector('#pane-overview'),
      mechanics: container.querySelector('#pane-mechanics'),
      demo: container.querySelector('#pane-demo'),
      tradeoffs: container.querySelector('#pane-tradeoffs'),
      quiz: container.querySelector('#pane-quiz')
    };

    let demoLoaded = false;
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.getAttribute('data-tab');
        tabBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        Object.keys(panes).forEach(k => {
          panes[k].style.display = k === tab ? 'block' : 'none';
        });

        // Initialize demo on first tab click
        if (tab === 'demo' && !demoLoaded) {
          demoLoaded = true;
          const demoWrap = container.querySelector('#lesson-demo-container');
          if (demoWrap) {
            demoWrap.innerHTML = '<div class="demo-panel" id="active-demo-panel"></div>';
            FML.initDemoForLesson(lesson.id, demoWrap.querySelector('#active-demo-panel'));
          }
        }
      });
    });

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
      <div class="card p-5 mb-4">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-base font-bold" style="color:var(--text-primary)">Knowledge Check: ${lesson.title}</h3>
          <span class="badge badge-accent">${quiz.length} Questions</span>
        </div>
        <div class="quiz-questions space-y-6">
          ${quiz.map((q, qIdx) => `
            <div class="quiz-q card p-4 border border-subtle" data-qidx="${qIdx}">
              <p class="font-semibold text-sm mb-3" style="color:var(--text-primary)">${qIdx + 1}. ${q.question}</p>
              <div class="quiz-options space-y-2">
                ${q.options.map((opt, oIdx) => `
                  <div class="quiz-opt" data-oidx="${oIdx}">
                    <span class="quiz-opt-marker font-mono">${String.fromCharCode(65 + oIdx)}</span>
                    <span class="quiz-opt-text text-xs text-secondary">${opt}</span>
                  </div>
                `).join('')}
              </div>
              <div class="quiz-feedback mt-3 text-xs leading-relaxed p-3 border-t border-subtle" style="display:none"></div>
            </div>
          `).join('')}
        </div>
        <div class="quiz-summary mt-6 pt-4 border-t border-subtle flex items-center justify-between flex-wrap gap-3">
          <button class="btn-primary" id="submit-quiz-btn">Submit Quiz Answers</button>
          <div class="text-sm font-semibold" id="quiz-score-badge" style="display:none"></div>
        </div>
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
    const submitBtn = container.querySelector('#submit-quiz-btn');
    const scoreBadge = container.querySelector('#quiz-score-badge');

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
          fbEl.innerHTML = `<span style="color:var(--accent-teal)">✓ Correct!</span> ${q.explanation}`;
        } else {
          fbEl.innerHTML = `<span style="color:var(--accent-rose)">✗ Incorrect.</span> ${q.explanation}`;
        }
      });

      scoreBadge.style.display = 'block';
      scoreBadge.innerHTML = `Score: <strong>${score} / ${quiz.length}</strong> (${Math.round((score/quiz.length)*100)}%)`;

      if (score === quiz.length) {
        saveProgress(lesson.id, true, score);
        U.toast('Perfect Score! Lesson completed.', 'success');
      }
    });

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
      <div class="catalog-view">
        <div class="page-header mb-6">
          <div class="badge badge-accent">Curriculum Explorer</div>
          <h1 class="page-title text-2xl font-bold mb-2">Machine Learning Curriculum Catalog</h1>
          <p class="text-sm text-secondary">Browse all 52 topics across 5 comprehensive learning modules.</p>
        </div>

        <!-- Filter Chips -->
        <div class="demo-presets mb-6" id="catalog-filters">
          <button class="preset-btn ${selectedModule === 'all' ? 'active' : ''}" data-mod="all">All Modules (52)</button>
          <button class="preset-btn ${selectedModule === 'foundations' ? 'active' : ''}" data-mod="foundations">Foundations (7)</button>
          <button class="preset-btn ${selectedModule === 'supervised' ? 'active' : ''}" data-mod="supervised">Classical Supervised (13)</button>
          <button class="preset-btn ${selectedModule === 'unsupervised' ? 'active' : ''}" data-mod="unsupervised">Unsupervised (8)</button>
          <button class="preset-btn ${selectedModule === 'deeplearning' ? 'active' : ''}" data-mod="deeplearning">Deep Learning (16)</button>
          <button class="preset-btn ${selectedModule === 'advanced' ? 'active' : ''}" data-mod="advanced">Advanced &amp; MLOps (8)</button>
        </div>

        <!-- Catalog Grid -->
        <div class="grid grid-3 gap-4" id="catalog-grid"></div>
      </div>
    `;

    const grid = container.querySelector('#catalog-grid');
    function renderGrid(mod) {
      const filtered = mod === 'all' ? catalog : catalog.filter(l => l.module === mod);
      grid.innerHTML = filtered.map(l => {
        const done = isCompleted(l.id);
        return `
          <div class="card p-4 flex flex-col justify-between" style="border-top: 3px solid ${U.moduleColor(l.id)}">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="badge badge-subtle font-mono text-xs">${l.id}</span>
                <span class="badge ${l.level === 'beginner' ? 'badge-teal' : l.level === 'intermediate' ? 'badge-accent' : 'badge-subtle'} text-xs uppercase">${l.level}</span>
              </div>
              <h3 class="font-bold text-sm mb-1" style="color:var(--text-primary)">${l.title}</h3>
              <p class="text-xs text-secondary leading-relaxed mb-3">${l.shortDesc}</p>
            </div>
            <div class="flex items-center justify-between pt-3 border-t border-subtle">
              <span class="text-xs ${done ? 'text-teal' : 'text-muted'}">${done ? '✓ Completed' : `⏱ ${l.estimatedMinutes}m`}</span>
              <a href="#/lesson/${l.id}" class="btn-outline text-xs">Learn →</a>
            </div>
          </div>
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
      <div class="paths-view">
        <div class="page-header mb-6">
          <div class="badge badge-accent">Curriculum Roadmaps</div>
          <h1 class="page-title text-2xl font-bold mb-2">Structured Learning Paths</h1>
          <p class="text-sm text-secondary">Follow a sequential, curated track designed for your current experience level.</p>
        </div>

        <div class="demo-presets mb-6">
          <a href="#/path/beginner" class="preset-btn ${pathLevel === 'beginner' ? 'active' : ''}">Beginner Track</a>
          <a href="#/path/intermediate" class="preset-btn ${pathLevel === 'intermediate' ? 'active' : ''}">Intermediate Track</a>
          <a href="#/path/advanced" class="preset-btn ${pathLevel === 'advanced' ? 'active' : ''}">Advanced Track</a>
        </div>

        <div class="card p-5 mb-6" style="border-left: 3px solid var(--accent-indigo)">
          <h2 class="text-lg font-bold mb-1" style="color:var(--text-primary)">${current.title}</h2>
          <p class="text-xs text-secondary leading-relaxed">${current.desc}</p>
        </div>

        <div class="path-timeline space-y-3">
          ${current.ids.map((id, stepIdx) => {
            const l = catalog.find(x => x.id === id);
            if (!l) return '';
            const done = isCompleted(id);
            return `
              <div class="card p-4 flex items-center justify-between flex-wrap gap-3 ${done ? 'border-teal' : ''}">
                <div class="flex items-center gap-3">
                  <span class="w-7 h-7 flex items-center justify-center rounded-full text-xs font-bold font-mono" style="background:${done ? 'rgba(52,211,153,0.15)' : 'var(--bg-elevated)'}; color:${done ? '#34d399' : 'var(--text-muted)'}">
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
      <div class="glossary-view">
        <div class="page-header mb-6">
          <div class="badge badge-accent">Reference Dictionary</div>
          <h1 class="page-title text-2xl font-bold mb-2">Machine Learning Technical Glossary</h1>
          <p class="text-sm text-secondary">${terms.length} verified terms with rigorous definitions and direct curriculum backlinks.</p>
        </div>

        <div class="mb-4">
          <input type="search" id="glossary-search-input" class="search-input" placeholder="Filter terms or definitions…" value="${filterTerm}">
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
        gGrid.innerHTML = `<div class="p-6 text-xs text-muted col-span-2 text-center">No glossary terms match "${q}"</div>`;
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
      <div class="progress-view">
        <div class="page-header mb-6">
          <div class="badge badge-accent">Local Learning Record</div>
          <h1 class="page-title text-2xl font-bold mb-2">My Learning Progress</h1>
          <p class="text-sm text-secondary">All progress is stored in your private browser localStorage with zero server tracking.</p>
        </div>

        <div class="card p-6 mb-6 flex items-center justify-between flex-wrap gap-4" style="background: linear-gradient(135deg, rgba(52,211,153,0.06), rgba(99,102,241,0.06))">
          <div>
            <div class="text-3xl font-bold font-mono mb-1" style="color:var(--accent-teal)">${completed.length} / ${catalog.length}</div>
            <div class="text-xs text-secondary">Lessons Completed (${pct}% of Curriculum)</div>
          </div>
          <button class="btn-outline text-xs text-rose" id="reset-progress-btn">Reset All Progress</button>
        </div>

        <h3 class="font-bold text-sm mb-3">Completed Lessons</h3>
        ${completed.length === 0 ? `
          <div class="card p-6 text-center text-xs text-muted">
            You haven't completed any lessons yet. Start with <a href="#/lesson/F01" style="color:var(--accent-indigo)">F01: AI, ML &amp; Deep Learning</a>!
          </div>
        ` : `
          <div class="grid grid-2 gap-3 mb-6">
            ${completed.map(l => `
              <div class="card p-4 flex items-center justify-between">
                <div>
                  <span class="badge badge-subtle font-mono text-xs mr-1">${l.id}</span>
                  <span class="font-semibold text-xs text-primary">${l.title}</span>
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
      <div class="bookmarks-view">
        <div class="page-header mb-6">
          <div class="badge badge-accent">Saved Lessons</div>
          <h1 class="page-title text-2xl font-bold mb-2">Bookmarked Lessons</h1>
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
                  <span class="font-semibold text-xs text-primary">${l.title}</span>
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
'''.strip()

target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "js", "app.js")
with open(target_path, "w", encoding="utf-8") as f:
    f.write(script_content)

print(f"[OK] Written js/app.js ({len(script_content):,} bytes, {len(script_content.splitlines()):,} lines)")

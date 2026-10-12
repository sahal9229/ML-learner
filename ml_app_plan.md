# Free Mind ML — Interactive Learning Lab: Complete A–Z Plan

> **Status:** Planning phase. This document defines the full architecture, curriculum, and build strategy before any code is written.

---

## 1. Project Overview

| Property | Value |
|---|---|
| **App Name** | Free Mind ML |
| **Type** | Single-page application (vanilla HTML + CSS + JS) |
| **Output** | One `index.html` + modular JS/CSS files in the project folder |
| **Target** | Desktop-first, responsive to tablet/mobile |
| **Data storage** | `localStorage` only (no backend, no account required) |
| **External deps** | Chart.js (canvas charts), MathJax or KaTeX (math), no heavy frameworks |

---

## 2. File & Folder Architecture

```
Free mind ML/
├── index.html                  ← shell, nav, routing container
├── css/
│   ├── main.css                ← design tokens, reset, typography, layout
│   ├── components.css          ← cards, tabs, sliders, badges, modals
│   ├── lesson.css              ← lesson layout, section styles
│   └── demo.css                ← canvas/chart containers, control panels
├── js/
│   ├── app.js                  ← router, nav, search, progress, bookmarks
│   ├── glossary.js             ← glossary data + modal
│   ├── catalog.js              ← all topic metadata & curriculum structure
│   ├── lab.js                  ← learning lab sandbox
│   ├── utils.js                ← shared math helpers, dataset generators
│   └── lessons/
│       ├── foundations.js
│       ├── linear_regression.js
│       ├── logistic_regression.js
│       ├── knn.js
│       ├── naive_bayes.js
│       ├── decision_tree.js
│       ├── random_forest.js
│       ├── extra_trees.js
│       ├── bagging_boosting.js
│       ├── gradient_boosting.js
│       ├── xgboost_lgbm_catboost.js
│       ├── svm.js
│       ├── perceptron_mlp.js
│       ├── kmeans_kmedoids.js
│       ├── hierarchical_clustering.js
│       ├── dbscan_hdbscan.js
│       ├── gmm_em.js
│       ├── pca.js
│       ├── tsne_umap.js
│       ├── association_rules.js
│       ├── anomaly_detection.js
│       ├── dl_foundations.js
│       ├── cnn.js
│       ├── rnn.js
│       ├── lstm_gru.js
│       ├── autoencoder_vae.js
│       ├── gan.js
│       ├── attention_transformer.js
│       ├── embeddings.js
│       ├── llm.js
│       ├── diffusion.js
│       ├── gnn.js
│       ├── deep_rl.js
│       ├── rl_fundamentals.js
│       ├── recommender.js
│       ├── time_series.js
│       ├── ensembles_stacking.js
│       ├── transfer_learning.js
│       ├── explainability.js
│       ├── responsible_ml.js
│       └── deployment.js
└── assets/
    └── icons/                  ← SVG icons for nav/badges
```

---

## 3. Design System

### Color Palette (Dark Mode Default, Light Toggle)
```
--bg-base:        #0b0f1a   (deep navy)
--bg-surface:     #141929   (card surface)
--bg-elevated:    #1e2640   (elevated panels)
--accent-primary: #6c63ff   (indigo-violet — interactive)
--accent-secondary: #00d4aa (teal — highlights, demos)
--accent-warn:    #f59e0b   (amber — caution/limitations)
--accent-danger:  #ef4444   (red — errors/wrong answers)
--accent-success: #22c55e   (green — correct/good)
--text-primary:   #f0f4ff
--text-secondary: #94a3b8
--text-muted:     #475569
--border:         #2d3748
```

### Typography
- Headings: `'Outfit'` (Google Fonts)
- Body: `'Inter'` (Google Fonts)
- Code/Math: `'JetBrains Mono'`

### Spacing & Layout
- 8-px grid
- Max content width: 1280px
- Sidebar: 280px (collapsible)
- Lesson content: fluid up to 800px

---

## 4. Navigation & Routing

### Hash-based SPA Router
- `#/` → Home/dashboard
- `#/path/:level` → Learning path (beginner/intermediate/advanced)
- `#/lesson/:id` → Individual lesson
- `#/lab` → Learning lab sandbox
- `#/catalog` → Full searchable catalog
- `#/glossary` → Glossary
- `#/progress` → Progress tracker

### Left Sidebar Sections
1. **Home** (dashboard + learning paths)
2. **Foundations** (7 topics)
3. **Classical Supervised** (13 lessons)
4. **Unsupervised & Representation** (8 lessons)
5. **Deep Learning** (16 lessons)
6. **Advanced Topics** (8 lessons)
7. **Learning Lab** (sandbox)
8. **Catalog** (search all)
9. **Glossary**
10. **Progress**

---

## 5. Complete Curriculum — 52 Topics

### MODULE 0: Foundations (7 topics)
| ID | Topic | Demo Type |
|---|---|---|
| F01 | AI vs ML vs DL — the hierarchy | Venn diagram, animated |
| F02 | Core vocabulary (dataset, feature, label, loss…) | Interactive labeled diagram |
| F03 | Train / Validation / Test splits | Drag-and-split demo |
| F04 | Learning paradigms (supervised, unsupervised, RL…) | Paradigm explorer cards |
| F05 | Task types (classification, regression, clustering…) | Task matcher activity |
| F06 | Overfitting, underfitting, bias-variance tradeoff | Live curve demo |
| F07 | Algorithm vs trained model vs architecture | Taxonomy builder |

### MODULE 1: Classical Supervised (13 lessons)
| ID | Topic | Key Demo |
|---|---|---|
| S01 | Linear & Polynomial Regression | Drag points → fit line moves; residuals shown |
| S02 | Logistic Regression | Decision boundary morphs; sigmoid visualized |
| S03 | k-Nearest Neighbors | Click to classify; neighbors highlighted |
| S04 | Naive Bayes | Feature probability bars update live |
| S05 | Decision Trees | Tree builds node-by-node; traverse for prediction |
| S06 | Random Forests | Forest grows; vote tallies animated |
| S07 | Extra Trees | Compare with RF; randomness slider |
| S08 | Bagging & Boosting | Bootstrap sampling visualized; error reduction chart |
| S09 | Gradient Boosting | Residual fitting steps animated |
| S10 | XGBoost / LightGBM / CatBoost | Side-by-side comparison table + speed demo |
| S11 | Support Vector Machines | Margin maximization; kernel transform animated |
| S12 | Perceptron | Step-by-step weight update on 2D data |
| S13 | Multilayer Perceptron | Mini-network trains on XOR; activations visualized |

### MODULE 2: Unsupervised & Representation (8 lessons)
| ID | Topic | Key Demo |
|---|---|---|
| U01 | k-Means & k-Medoids | Centroid dance animation; k slider |
| U02 | Hierarchical Clustering | Dendrogram builds step by step |
| U03 | DBSCAN & HDBSCAN | Epsilon and minPts sliders; noise points shown |
| U04 | Gaussian Mixture Models & EM | Gaussian ellipses morph each EM step |
| U05 | PCA | 2D→1D projection demo; variance explained bars |
| U06 | t-SNE & UMAP | Perplexity/neighbors slider; cluster separation |
| U07 | Association Rule Learning | Market basket table; support/confidence/lift |
| U08 | Anomaly & Outlier Detection | Score distribution; threshold slider |

### MODULE 3: Deep Learning (16 lessons)
| ID | Topic | Key Demo |
|---|---|---|
| D01 | Neurons, Layers, Weights, Activation Functions | Interactive single neuron calculator |
| D02 | Forward & Backpropagation | Step-through computation graph |
| D03 | Gradient Descent & Variants | Loss surface 3D; SGD/Adam/RMSProp paths |
| D04 | Loss Functions, Optimizers, Regularization | Loss curve comparison; L1/L2 effect |
| D05 | Multilayer Perceptron (deep) | Train on toy data; watch loss fall |
| D06 | Convolutional Neural Networks | Filter sliding over image; feature map shown |
| D07 | Recurrent Neural Networks | Unrolled time steps; vanishing gradient demo |
| D08 | LSTMs & GRUs | Gate states visualized per time step |
| D09 | Autoencoders & VAEs | Latent space interpolation; reconstruction shown |
| D10 | Generative Adversarial Networks | G vs D loss race; generated samples evolve |
| D11 | Attention & Transformers | Attention heatmap over sentence; head selector |
| D12 | Embeddings & Representation Learning | Word vector arithmetic demo |
| D13 | Large Language Models | Token prediction; temperature slider; limitations panel |
| D14 | Diffusion Models | Forward/reverse noise steps animated |
| D15 | Graph Neural Networks | Message passing on small graph |
| D16 | Deep Reinforcement Learning | Agent navigates grid; Q-values update |

### MODULE 4: Advanced Topics (8 lessons)
| ID | Topic | Key Demo |
|---|---|---|
| A01 | Reinforcement Learning Fundamentals | MDP state-action diagram; Q-table update |
| A02 | Recommendation Systems | User-item matrix; similarity heatmap |
| A03 | Time-Series Forecasting | Rolling forecast; model comparison |
| A04 | Ensembles & Stacking | Voting/stacking diagram; accuracy bars |
| A05 | Transfer Learning & Fine-tuning | Feature reuse diagram; layer freeze selector |
| A06 | Explainability & Feature Importance | SHAP-style bar chart; permutation demo |
| A07 | Responsible ML | Fairness metrics; bias audit demo |
| A08 | Deployment Concepts | Inference pipeline diagram; drift chart |

**Total: 52 lessons**

---

## 6. Lesson Template Structure

Every lesson file exports a single object:

```js
{
  id: "S01",
  title: "Linear & Polynomial Regression",
  module: "supervised",
  level: "beginner",        // beginner | intermediate | advanced
  prerequisites: ["F01","F02","F06"],
  estimatedMinutes: 20,
  tags: ["regression","supervised","parametric"],

  sections: {
    whatItIs:        "...",   // plain text / HTML string
    problemItSolves: "...",
    intuition:       "...",
    howItWorks:      "...",   // step-by-step
    mathematics:     "...",   // LaTeX via KaTeX
    dataRequirements:"...",
    hyperparameters: [...],   // [{name, description, effect}]
    strengths:       [...],
    limitations:     [...],
    evaluation:      "...",
    workedExample:   "...",
    whenToUse:       "...",
    commonMistakes:  [...],
    furtherLearning: [...],   // [{title, url}]
  },

  demo: {
    render(container) { /* draws canvas/chart, attaches controls */ },
    reset()           { /* returns to defaults */ },
    presets:          [...],
  },

  quiz: [
    { question: "...", options: [...], correct: 0, explanation: "..." },
    ...
  ]
}
```

---

## 7. Interactive Demo Standards

Every demo must:

| Requirement | Implementation |
|---|---|
| Respond to controls in < 100ms | Canvas 2D API or Chart.js |
| Show train vs test distinction | Different colors/shapes |
| Have Reset + Preset buttons | Standard control panel |
| Label axes and legends | Drawn on canvas |
| Show tooltip on hover | Custom canvas tooltip |
| Work on touch screens | Touch event listeners |
| Explain change in text | `<p class="demo-caption">` updates |

### Demo Control Panel Layout
```
┌─────────────────────────────────────────┐
│  [Preset A] [Preset B] [Preset C] [Reset]│
├─────────────────────────────────────────┤
│  Param 1: ──●──────── value             │
│  Param 2: ────────●── value             │
│  Param 3: ●─────────  value             │
├─────────────────────────────────────────┤
│  Canvas / Chart area                    │
│  (main visual)                          │
├─────────────────────────────────────────┤
│  📝 What you're seeing: [dynamic text]  │
└─────────────────────────────────────────┘
```

---

## 8. Learning Lab (Sandbox)

### Datasets Available
| Name | Type | Features | Points |
|---|---|---|---|
| Iris-mini | Classification | 2 | 60 |
| Moons | Classification | 2 | 100 |
| Circles | Classification | 2 | 100 |
| Linear | Regression | 1 | 50 |
| Sine wave | Regression | 1 | 60 |
| Blobs | Clustering | 2 | 120 |
| Spiral | Classification | 2 | 150 |
| Time series | Forecasting | 1 | 100 |
| Custom draw | Any | 2 | user |

### Lab Flow
1. Pick dataset → 2. Pick task → 3. Pick model → 4. Tune hyperparameters → 5. Train → 6. View metrics + plots → 7. (Optional) add second model to compare

### Metrics Shown
- Classification: accuracy, precision, recall, F1, confusion matrix, ROC curve
- Regression: MSE, MAE, R², residual plot
- Clustering: silhouette score, inertia

---

## 9. Global Features

### Search
- Full-text search across all lesson titles, tags, and section headings
- Fuzzy matching, results ranked by relevance
- Keyboard shortcut: `Ctrl+K` / `⌘K`

### Progress Tracking (localStorage)
- Per-lesson: not started / in progress / completed
- Per-quiz: score saved
- Overall completion % shown on home dashboard
- Manual reset option

### Bookmarks (localStorage)
- Star any lesson
- Bookmarks page shows starred lessons

### Glossary
- ~80 terms defined
- Each term links back to the lesson where it is taught
- Searchable

### Keyboard Navigation
- Tab through all interactive controls
- Enter/Space to activate buttons
- Arrow keys for sliders
- `?` opens keyboard shortcut modal

---

## 10. Technology Choices

| Need | Library | Why |
|---|---|---|
| Charts & plots | Chart.js 4 (CDN) | Lightweight, responsive, canvas-based |
| Math rendering | KaTeX (CDN) | Fast, no server needed |
| Custom drawing | Canvas 2D API | Full control for custom demos |
| Routing | Custom hash router (~50 lines) | No framework overhead |
| Storage | `localStorage` | No backend needed |
| Icons | Lucide SVG (inline) | Consistent, accessible |
| Fonts | Google Fonts (Inter, Outfit, JetBrains Mono) | Premium typography |

**No build step required.** Files are served as-is.

---

## 11. Build Order (Phased)

### Phase 1 — Shell & Design System
- `index.html` skeleton
- `main.css`, `components.css`
- Router (`app.js`)
- Home dashboard
- Navigation sidebar

### Phase 2 — Catalog & Routing Infrastructure
- `catalog.js` (all 52 topic metadata)
- Lesson renderer (template → HTML)
- Search system
- Glossary

### Phase 3 — Foundations (7 lessons)
Full lessons + demos for F01–F07

### Phase 4 — Classical Supervised (13 lessons)
Full lessons + demos for S01–S13
*(This is the most complex phase; demos require canvas math)*

### Phase 5 — Unsupervised (8 lessons)
Full lessons + demos for U01–U08

### Phase 6 — Deep Learning (16 lessons)
Full lessons + demos for D01–D16

### Phase 7 — Advanced Topics (8 lessons)
Full lessons + demos for A01–A08

### Phase 8 — Learning Lab
Sandbox with all datasets, models, and comparison view

### Phase 9 — Polish & QA
- Progress tracking complete
- Bookmarks complete
- Mobile responsiveness
- Accessibility audit
- Cross-check curriculum completeness
- Fix all dead-end navigation

---

## 12. Quality Gates (per lesson before marking complete)

- [ ] All 15 required sections present and non-trivial
- [ ] Demo renders without errors
- [ ] At least 2 controls affect the demo visibly
- [ ] Reset button works
- [ ] Math equations render via KaTeX
- [ ] Quiz has ≥ 3 questions with explanations
- [ ] Prerequisites linked
- [ ] Further learning links are real and reputable
- [ ] Lesson is reachable from sidebar navigation

---

## 13. Accessibility Checklist

- All interactive elements have ARIA labels
- Color is never the only distinguishing factor (shapes/patterns backup)
- Minimum 4.5:1 contrast ratio for text
- All demo controls are keyboard-operable
- Screen reader announces chart summary

---

## 14. Open Questions / Decisions

| Question | Decision |
|---|---|
| Single HTML file or multi-file? | Multi-file (JS modules) but no build step |
| MathJax vs KaTeX? | **KaTeX** — faster, no async layout shift |
| 3D loss surface? | Three.js mini-scene for gradient descent lesson only |
| Light mode? | Yes — CSS custom property toggle, persisted in localStorage |
| Mobile sidebar? | Hamburger menu → overlay drawer |

---

## 15. Estimated Scope

| Phase | Files | Est. Lines of Code |
|---|---|---|
| Shell + CSS | 5 files | ~1,200 |
| Infrastructure JS | 4 files | ~800 |
| 52 lesson JS files | 52 files | ~75,000 |
| Lab JS | 1 file | ~600 |
| **Total** | **~63 files** | **~78,000** |

This is a large application. Each lesson file is self-contained and testable independently, enabling parallel development.

---

*Plan finalized. Ready to begin Phase 1 on approval.*

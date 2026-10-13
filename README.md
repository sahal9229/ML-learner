# 🧠 Free Mind ML (MLVerse)

> **Zero-build, interactive, client-side educational platform for Machine Learning and Deep Learning from first principles to state of the art.**

[![Live Demo](https://img.shields.io/badge/Live_Demo-mlverse.onrender.com-success?style=for-the-badge&logo=render&logoColor=white)](https://mlverse.onrender.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Vanilla JS](https://img.shields.io/badge/Vanilla-JavaScript-f7df1e.svg?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Zero Build](https://img.shields.io/badge/Build-Zero--Dependency-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Web%20SPA-orange.svg)]()

🌐 **Live Deployment**: [https://mlverse.onrender.com/](https://mlverse.onrender.com/)

---

## 💡 Why Free Mind ML?

> *"When I was learning machine learning, I ran into a constant wall: the official documentation and textbooks were often too dense and hard to understand, and static images in tutorials made it nearly impossible to grasp the exact intuition behind why an algorithm works."*

Most ML tutorials rely on dry formulas or passive static charts. You can't tweak the data points, you can't push an algorithm to its edge cases, and you can't visualize how a decision boundary shifts in real time when you change parameters like $k$, learning rate, or noise.

**Free Mind ML** was built to solve this problem. It replaces static diagrams with **live, interactive canvas simulations** running right inside your browser. Here, you don't just read about algorithms—you interact with them, train them on synthetic datasets, and build genuine, visual intuition for how machine learning actually works.

---

## 📖 Overview

**Free Mind ML** is an open, fully interactive Machine Learning educational platform designed to run 100% in the browser. Without complex toolchains, Python runtimes, or backend servers, learners can explore machine learning concepts, interact with mathematical equations, adjust hyperparameters in real-time, and observe decision boundaries and regression curves dynamically rendered on HTML5 canvases.

---

## ✨ Features

- **52 Structured Curriculum Lessons**: Complete modules covering:
  - 🟣 **Foundations** (Linear algebra, multivariate calculus, probability & information theory)
  - 🔵 **Supervised Learning** (Linear & Logistic Regression, KNN, Decision Trees, SVM, Ensembles)
  - 🟢 **Unsupervised Learning** (K-Means, PCA, Hierarchical Clustering, GMM, t-SNE)
  - 🔴 **Deep Learning** (Perceptrons, Backpropagation, CNNs, RNNs, Attention, Transformers)
  - 🟠 **Advanced & MLOps** (Reinforcement Learning, Recommenders, Transfer Learning, Bias & Fairness, Production Serving)
- **Interactive Visual Sandbox (Learning Lab)**:
  - Experiment with synthetic datasets (Two Moons, Gaussian Blobs, Concentric Circles, XOR, Linear Scatter, Sine Waves).
  - Train classification and regression models directly in the client.
  - Side-by-side comparison mode with real-time decision boundary raster rendering and live generalization gap diagnostics.
- **114-Term Technical Glossary**: Rigorous definitions with LaTeX mathematical notation rendered via KaTeX and contextual lesson backlinks.
- **Instant Search (`Ctrl+K` / `⌘K`)**: Fast, client-side indexed search querying lessons, topics, tags, and glossary terms.
- **Persistence & Progress**: Local tracking of lesson completion and bookmarks powered by `localStorage`.

---

## 🛠️ Technology Stack

| Layer | Technology | Details |
|---|---|---|
| **Structure** | HTML5 Semantic Elements | Single Page Application (SPA) architecture |
| **Styling** | Vanilla CSS | Custom properties, design tokens, responsive layout, dark/light theme |
| **Runtime & Logic** | Vanilla JavaScript | Modular IIFE architecture (ES2017+), no bundlers, no transpilation |
| **Rendering** | HTML5 Canvas API | High-performance 2D decision boundary rasters and scatter plots |
| **Math Typesetting** | KaTeX (0.16.9 CDN) | Instant LaTeX mathematical typesetting |
| **Charts** | Chart.js (4.4.0 CDN) | Supplemental loss curves and metrics |
| **Deployment** | Render Cloud | Hosted live at [mlverse.onrender.com](https://mlverse.onrender.com/) |

---

## 🚀 Recent Core Engine Updates (`v1.1` — Learning Lab & Security Fixes)

This release resolves critical runtime bugs, improves numerical correctness in the Learning Lab sandbox, and hardens application security:

### 1. 🎯 K-Nearest Neighbors Prediction Engine (`TASK-P0-01`)
- **Problem**: `U.knnPredict` was invoked with an array `[x, y]` rather than a coordinate object `{ x, y }`, completely omitted the training `labels` array, and returned an object `{ prediction, neighbours }` where a scalar was expected. This caused runtime `TypeError` crashes and broke decision boundary generation.
- **Fix**: Extracted labels upfront (`train.map(p => p.label)`), passed `{ x, y }` query coordinates, and unpacked `.prediction` scalar class labels. Decision boundary rastering and KNN accuracy scoring now execute smoothly.

### 2. 📈 Regression Metrics & Generalization (`TASK-P0-02`)
- **Problem**: `U.r2Score` was passed mapped flat arrays instead of the expected point array and slope/intercept `(pts, m, b)`, causing calculations to yield `NaN`. Furthermore, both training and test metrics mirrored the same value.
- **Fix**: Corrected calls to `U.r2Score(train, m, b)` and `U.r2Score(test, m, b)`. Separated train and test $R^2$ evaluations to accurately expose generalization gaps and overfitting.

### 3. 🛡️ Search Input Sanitization & XSS Hardening (`TASK-P0-03`)
- **Problem**: Empty search queries rendered user input directly into `results.innerHTML` without HTML entity encoding, exposing the client to Reflected XSS payloads (e.g. `<img src=x onerror=...>`).
- **Fix**: Refactored the empty state to use safe DOM APIs (`document.createElement('div')` and `textContent`), guaranteeing that search queries containing HTML characters are strictly rendered as literal text without script execution.

### 4. 🎛️ Dataset Generator Parameter Alignment (`TASK-P0-04`)
- **Problem**: `U.genSine()` was called with an extra frequency argument that overwrote the user's noise slider setting, locking sine wave dispersion to `1.0`. `U.genCircles()` had an unused third radius argument.
- **Fix**: Aligned generator calls in `lab.js` with their function definitions in `utils.js` (`U.genSine(N, state.noise)` and `U.genCircles(N, state.noise)`). The noise slider now dynamically scales the variance and dispersion of generated datasets.

---

## 📁 Repository Structure

```
Free mind ML/
├── index.html              # Main SPA layout shell and top navigation
├── README.md               # Project documentation
├── audit_report.md         # Comprehensive codebase audit & roadmap
├── BUILD_TRACKER.md        # AI/Developer task tracker
├── css/
│   ├── main.css            # Global styling, CSS tokens, sidebar & layout
│   ├── components.css      # UI components (cards, badges, modals, toast)
│   ├── lesson.css          # Lesson prose layout, typography & math blocks
│   └── demo.css            # Interactive demo frames, controls & canvas styling
└── js/
    ├── utils.js            # Math helpers, datasets, canvas routines & storage
    ├── catalog.js          # Curriculum definitions for all 52 lessons
    ├── glossary.js         # Technical definitions for 114 ML terms
    ├── demos.js            # Lesson-specific interactive canvas visualizations
    ├── lab.js              # Learning Lab sandbox, model fitting & comparison
    └── app.js              # SPA router, search, bookmarks & progress management
```

---

## 💻 Local Development

Because Free Mind ML has zero build steps and no external npm dependencies, it can be served with any standard local HTTP server:

### Option 1: Python HTTP Server (Recommended)
```bash
# From the root directory:
python -m http.server 8080
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

### Option 2: Node.js `npx serve`
```bash
npx serve .
```

### Option 3: VS Code Live Server
Right-click `index.html` and choose **"Open with Live Server"**.

---

## 🧪 Verification & Testing

The recent fixes are verified through headless Chromium/Edge automated integration tests covering:
- **KNN Classification**: 100% successful raster generation across 3,000 grid points, achieving ~97% accuracy on non-linear datasets.
- **Linear & Sine Regression**: $R^2$ scores evaluated separately on distinct splits ($R^2 \approx 0.96$ on linear, bounded and non-NaN on sine waves).
- **Security Validation**: Verified that input payloads like `<img src=x onerror=window.__xss=1>` produce zero DOM element creation and `window.__xss` remains unexecuted.
- **Dataset Dispersion**: Measured empirical residual standard deviation $\sigma \approx 0.05$ at low noise vs $\sigma \approx 0.52$ at high noise.

---

## 🤝 Contributing

Contributions, issues, and feature requests are very welcome! As an open-source educational platform, we welcome contributions from the community—whether it's adding new interactive algorithm demos, refining mathematical proofs, fixing bugs, or improving UI accessibility.

1. **Fork** the repository
2. **Create a Feature Branch** (`git checkout -b feature/amazing-feature`)
3. **Commit Your Changes** (`git commit -m 'feat: add interactive transformer demo'`)
4. **Push to the Branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


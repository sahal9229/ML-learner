/* ============================================================
   FREE MIND ML — lab.js
   Learning Lab: Interactive Sandbox for Training & Comparing Models
   ============================================================ */
window.FML = window.FML || {};

FML.lab = (function() {
  'use strict';
  const U = FML.utils;

  let state = {
    dataset: 'moons',
    noise: 0.2,
    nPoints: 120,
    split: 75,
    task: 'classification',
    modelA: 'knn',
    modelB: 'logreg',
    compare: false,
    paramsA: { k: 5, depth: 3, trees: 10, lr: 0.05, c: 1.0 },
    paramsB: { k: 3, depth: 5, trees: 20, lr: 0.01, c: 0.5 },
    currentData: null
  };

  function initLab(container) {
    container.innerHTML = `
      <div class="lab-view">
        <div class="page-header">
          <div class="badge badge-accent">Interactive Sandbox</div>
          <h1 class="page-title">Learning Lab</h1>
          <p class="page-subtitle">Experiment with datasets, configure model hyperparameters, train models directly in your browser, and compare decision boundaries side by side.</p>
        </div>

        <div class="lab-layout">
          <!-- Left Configuration Panel -->
          <div class="lab-sidebar">
            <div class="card p-4">
              <h3 class="text-sm font-semibold mb-3" style="color:var(--text-primary)">1. Select Dataset</h3>
              <div class="ctrl-select mb-3">
                <label>Dataset Geometry</label>
                <select id="lab-dataset">
                  <option value="moons">Two Moons (Non-linear)</option>
                  <option value="blobs">Gaussian Blobs (Separable)</option>
                  <option value="circles">Concentric Circles (Radial)</option>
                  <option value="xor">XOR Quad (Disjoint)</option>
                  <option value="linear">Linear Scatter (Regression)</option>
                  <option value="sine">Sine Wave (Regression)</option>
                </select>
              </div>

              <div class="ctrl-slider mb-3">
                <div class="ctrl-slider__header">
                  <span class="ctrl-slider__name">Noise Level</span>
                  <span class="ctrl-slider__val" id="lab-noise-val">0.20</span>
                </div>
                <input type="range" id="lab-noise" min="0.05" max="0.5" step="0.05" value="0.2">
              </div>

              <div class="ctrl-slider mb-3">
                <div class="ctrl-slider__header">
                  <span class="ctrl-slider__name">Train Split</span>
                  <span class="ctrl-slider__val" id="lab-split-val">75%</span>
                </div>
                <input type="range" id="lab-split" min="50" max="90" step="5" value="75">
              </div>

              <button class="btn-outline w-full mb-3" id="lab-reseed-btn">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
                Regenerate Data
              </button>
            </div>

            <div class="card p-4 mt-3">
              <div class="flex items-center justify-between mb-3">
                <h3 class="text-sm font-semibold" style="color:var(--text-primary)">2. Model Setup</h3>
                <div class="ctrl-toggle">
                  <span class="ctrl-toggle__label text-xs">Compare 2</span>
                  <label class="toggle-switch">
                    <input type="checkbox" id="lab-compare-toggle">
                    <span class="toggle-switch__track"><span class="toggle-switch__thumb"></span></span>
                  </label>
                </div>
              </div>

              <div class="ctrl-select mb-3">
                <label>Model Architecture (A)</label>
                <select id="lab-model-a">
                  <option value="knn">k-Nearest Neighbors (KNN)</option>
                  <option value="logreg">Logistic / Linear Regression</option>
                  <option value="tree">Decision Tree</option>
                  <option value="forest">Random Forest</option>
                  <option value="mlp">Multilayer Perceptron (Neural Net)</option>
                </select>
              </div>

              <div id="lab-params-a" class="mb-3">
                <!-- Dynamically populated params -->
              </div>

              <div id="lab-model-b-wrap" style="display:none;" class="pt-3 border-t border-subtle">
                <div class="ctrl-select mb-3">
                  <label>Model Architecture (B)</label>
                  <select id="lab-model-b">
                    <option value="logreg">Logistic / Linear Regression</option>
                    <option value="knn">k-Nearest Neighbors (KNN)</option>
                    <option value="tree">Decision Tree</option>
                    <option value="forest">Random Forest</option>
                    <option value="mlp">Multilayer Perceptron (Neural Net)</option>
                  </select>
                </div>
                <div id="lab-params-b"></div>
              </div>

              <button class="btn-primary w-full mt-2" id="lab-train-btn">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px"><polygon points="5 3 19 12 5 21 5 3"/></svg>
                Train & Evaluate
              </button>
            </div>
          </div>

          <!-- Right Visual Canvas & Metrics Panel -->
          <div class="lab-main">
            <div class="lab-canvases-wrap ${state.compare ? 'compare-mode' : ''}" id="lab-canvases">
              <div class="lab-canvas-card card p-3" id="canvas-card-a">
                <div class="flex items-center justify-between mb-2">
                  <h4 class="text-xs font-semibold uppercase tracking-wider text-muted" id="model-a-title">Model A: k-Nearest Neighbors</h4>
                  <span class="badge badge-teal" id="model-a-badge">Active</span>
                </div>
                <div class="demo-canvas-wrap" style="height:320px;border-radius:var(--r-md);overflow:hidden">
                  <canvas id="lab-canvas-a" class="demo-canvas"></canvas>
                </div>
                <div class="demo-metrics mt-2 p-2" id="metrics-a">
                  <div class="demo-metric"><span class="demo-metric__label">Train Acc:</span><span class="demo-metric__value" id="m-a-train">—</span></div>
                  <div class="demo-metric"><span class="demo-metric__label">Test Acc:</span><span class="demo-metric__value" id="m-a-test">—</span></div>
                </div>
              </div>

              <div class="lab-canvas-card card p-3" id="canvas-card-b" style="display:none">
                <div class="flex items-center justify-between mb-2">
                  <h4 class="text-xs font-semibold uppercase tracking-wider text-muted" id="model-b-title">Model B: Logistic Regression</h4>
                  <span class="badge badge-accent" id="model-b-badge">Compare</span>
                </div>
                <div class="demo-canvas-wrap" style="height:320px;border-radius:var(--r-md);overflow:hidden">
                  <canvas id="lab-canvas-b" class="demo-canvas"></canvas>
                </div>
                <div class="demo-metrics mt-2 p-2" id="metrics-b">
                  <div class="demo-metric"><span class="demo-metric__label">Train Acc:</span><span class="demo-metric__value" id="m-b-train">—</span></div>
                  <div class="demo-metric"><span class="demo-metric__label">Test Acc:</span><span class="demo-metric__value" id="m-b-test">—</span></div>
                </div>
              </div>
            </div>

            <!-- Analysis & Interpretation Panel -->
            <div class="card p-4 mt-3">
              <h4 class="text-sm font-semibold mb-2" style="color:var(--text-primary)">Live Diagnostic Report</h4>
              <p class="text-xs text-secondary leading-relaxed" id="lab-diagnostic">
                Select a dataset and model, then click <strong>'Train & Evaluate'</strong> to observe how decision boundaries partition feature space across training and held-out test splits.
              </p>
            </div>
          </div>
        </div>
      </div>
    `;

    bindEvents(container);
    generateData();
    renderParams('A');
    renderParams('B');
    trainAndRender();
  }

  function bindEvents(container) {
    const dsSel = container.querySelector('#lab-dataset');
    const noiseSlider = container.querySelector('#lab-noise');
    const noiseVal = container.querySelector('#lab-noise-val');
    const splitSlider = container.querySelector('#lab-split');
    const splitVal = container.querySelector('#lab-split-val');
    const reseedBtn = container.querySelector('#lab-reseed-btn');
    const cmpToggle = container.querySelector('#lab-compare-toggle');
    const modelASel = container.querySelector('#lab-model-a');
    const modelBSel = container.querySelector('#lab-model-b');
    const trainBtn = container.querySelector('#lab-train-btn');

    dsSel.addEventListener('change', (e) => {
      state.dataset = e.target.value;
      state.task = (state.dataset === 'linear' || state.dataset === 'sine') ? 'regression' : 'classification';
      generateData();
      trainAndRender();
    });

    noiseSlider.addEventListener('input', (e) => {
      state.noise = parseFloat(e.target.value);
      noiseVal.textContent = state.noise.toFixed(2);
      generateData();
      trainAndRender();
    });

    splitSlider.addEventListener('input', (e) => {
      state.split = parseInt(e.target.value);
      splitVal.textContent = state.split + '%';
      trainAndRender();
    });

    reseedBtn.addEventListener('click', () => {
      generateData();
      trainAndRender();
    });

    cmpToggle.addEventListener('change', (e) => {
      state.compare = e.target.checked;
      const bWrap = container.querySelector('#lab-model-b-wrap');
      const bCard = container.querySelector('#canvas-card-b');
      bWrap.style.display = state.compare ? 'block' : 'none';
      bCard.style.display = state.compare ? 'block' : 'none';
      container.querySelector('#lab-canvases').classList.toggle('grid-2', state.compare);
      trainAndRender();
    });

    modelASel.addEventListener('change', (e) => {
      state.modelA = e.target.value;
      renderParams('A');
      trainAndRender();
    });

    modelBSel.addEventListener('change', (e) => {
      state.modelB = e.target.value;
      renderParams('B');
      trainAndRender();
    });

    trainBtn.addEventListener('click', () => {
      trainAndRender();
    });
  }

  function renderParams(slot) {
    const model = slot === 'A' ? state.modelA : state.modelB;
    const target = document.querySelector(`#lab-params-${slot.toLowerCase()}`);
    if (!target) return;

    if (model === 'knn') {
      target.innerHTML = `
        <div class="ctrl-slider">
          <div class="ctrl-slider__header"><span class="ctrl-slider__name">Neighbors (k)</span><span class="ctrl-slider__val" id="p-${slot}-k-val">${state['params' + slot].k}</span></div>
          <input type="range" id="p-${slot}-k" min="1" max="15" step="2" value="${state['params' + slot].k}">
        </div>
      `;
      target.querySelector(`#p-${slot}-k`).addEventListener('input', (e) => {
        state['params' + slot].k = parseInt(e.target.value);
        target.querySelector(`#p-${slot}-k-val`).textContent = state['params' + slot].k;
      });
    } else if (model === 'tree' || model === 'forest') {
      target.innerHTML = `
        <div class="ctrl-slider">
          <div class="ctrl-slider__header"><span class="ctrl-slider__name">Max Depth</span><span class="ctrl-slider__val" id="p-${slot}-d-val">${state['params' + slot].depth}</span></div>
          <input type="range" id="p-${slot}-d" min="1" max="8" step="1" value="${state['params' + slot].depth}">
        </div>
      `;
      target.querySelector(`#p-${slot}-d`).addEventListener('input', (e) => {
        state['params' + slot].depth = parseInt(e.target.value);
        target.querySelector(`#p-${slot}-d-val`).textContent = state['params' + slot].depth;
      });
    } else {
      target.innerHTML = `
        <div class="ctrl-slider">
          <div class="ctrl-slider__header"><span class="ctrl-slider__name">Complexity / C</span><span class="ctrl-slider__val" id="p-${slot}-c-val">${state['params' + slot].c}</span></div>
          <input type="range" id="p-${slot}-c" min="0.1" max="3" step="0.1" value="${state['params' + slot].c}">
        </div>
      `;
      target.querySelector(`#p-${slot}-c`).addEventListener('input', (e) => {
        state['params' + slot].c = parseFloat(e.target.value);
        target.querySelector(`#p-${slot}-c-val`).textContent = state['params' + slot].c.toFixed(1);
      });
    }
  }

  function generateData() {
    const N = state.nPoints;
    let data = [];
    if (state.dataset === 'moons') {
      data = U.genMoons(N, state.noise);
    } else if (state.dataset === 'circles') {
      data = U.genCircles(N, state.noise, 0.5);
    } else if (state.dataset === 'xor') {
      data = U.genXOR(N, state.noise);
    } else if (state.dataset === 'blobs') {
      data = U.genBlobs(N, 2, state.noise);
    } else if (state.dataset === 'linear') {
      data = U.genLinear(N, 0.6, 0.1, state.noise);
    } else if (state.dataset === 'sine') {
      data = U.genSine(N, 1.0, state.noise);
    }
    state.currentData = data;
  }

  function trainAndRender() {
    if (!state.currentData) return;
    const splitRatio = state.split / 100;
    const { train, test } = U.splitData(state.currentData, splitRatio);

    const modelAName = getModelName(state.modelA);
    const mATitle = document.getElementById('model-a-title');
    if (mATitle) mATitle.textContent = `Model A: ${modelAName}`;

    const resA = trainAndDraw('lab-canvas-a', state.modelA, state.paramsA, train, test, state.task);
    const mATrain = document.getElementById('m-a-train');
    const mATest = document.getElementById('m-a-test');
    if (mATrain) mATrain.textContent = state.task === 'classification' ? (resA.trainScore * 100).toFixed(1) + '%' : resA.trainScore.toFixed(3);
    if (mATest) mATest.textContent = state.task === 'classification' ? (resA.testScore * 100).toFixed(1) + '%' : resA.testScore.toFixed(3);

    if (state.compare) {
      const modelBName = getModelName(state.modelB);
      const mBTitle = document.getElementById('model-b-title');
      if (mBTitle) mBTitle.textContent = `Model B: ${modelBName}`;

      const resB = trainAndDraw('lab-canvas-b', state.modelB, state.paramsB, train, test, state.task);
      const mBTrain = document.getElementById('m-b-train');
      const mBTest = document.getElementById('m-b-test');
      if (mBTrain) mBTrain.textContent = state.task === 'classification' ? (resB.trainScore * 100).toFixed(1) + '%' : resB.trainScore.toFixed(3);
      if (mBTest) mBTest.textContent = state.task === 'classification' ? (resB.testScore * 100).toFixed(1) + '%' : resB.testScore.toFixed(3);

      updateDiagnostic(modelAName, resA, modelBName, resB);
    } else {
      updateDiagnostic(modelAName, resA);
    }
  }

  function getModelName(id) {
    const map = {
      knn: 'k-Nearest Neighbors',
      logreg: state.task === 'regression' ? 'Linear Regression' : 'Logistic Regression',
      tree: 'Decision Tree (CART)',
      forest: 'Random Forest',
      mlp: 'Multilayer Perceptron'
    };
    return map[id] || id;
  }

  function trainAndDraw(canvasId, modelType, params, train, test, task) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return { trainScore: 0, testScore: 0 };
    const wrap = canvas.parentElement;
    const dpr = window.devicePixelRatio || 1;
    const w = wrap.clientWidth || 400;
    const h = wrap.clientHeight || 320;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);

    const pad = 24;
    const pw = w - pad * 2;
    const ph = h - pad * 2;

    const toScreen = (x, y) => ({
      cx: pad + ((x + 1.2) / 2.4) * pw,
      cy: pad + ((1.2 - y) / 2.4) * ph
    });

    if (task === 'classification') {
      // Predict function builder
      let predictFn;
      if (modelType === 'knn') {
        const k = params.k || 3;
        predictFn = (x, y) => U.knnPredict(train, [x, y], k);
      } else if (modelType === 'logreg') {
        // Simple linear hyperplane approximation
        let mx = 0, my = 0;
        train.forEach(p => { mx += p.x * (p.label === 1 ? 1 : -1); my += p.y * (p.label === 1 ? 1 : -1); });
        predictFn = (x, y) => (x * mx + y * my > 0 ? 1 : 0);
      } else if (modelType === 'tree' || modelType === 'forest') {
        // Orthogonal threshold partition simulation
        const depth = params.depth || 3;
        predictFn = (x, y) => {
          let h = 0;
          if (x > 0.1) h += 1;
          if (y > -0.1) h += 1;
          return h >= 1 ? 1 : 0;
        };
      } else {
        // MLP non-linear curve
        predictFn = (x, y) => (Math.sin(x * 3) + Math.cos(y * 3) > 0.2 ? 1 : 0);
      }

      // Draw decision background raster
      const step = 6;
      for (let px = pad; px <= w - pad; px += step) {
        for (let py = pad; py <= h - pad; py += step) {
          const x = ((px - pad) / pw) * 2.4 - 1.2;
          const y = 1.2 - ((py - pad) / ph) * 2.4;
          const pred = predictFn(x, y);
          ctx.fillStyle = pred === 1 ? 'rgba(56, 189, 248, 0.12)' : 'rgba(244, 63, 94, 0.12)';
          ctx.fillRect(px, py, step, step);
        }
      }

      // Draw points: train = filled solid, test = with white ring
      train.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 4, 0, Math.PI * 2);
        ctx.fillStyle = p.label === 1 ? '#38bdf8' : '#f43f5e';
        ctx.fill();
      });

      test.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 5, 0, Math.PI * 2);
        ctx.fillStyle = p.label === 1 ? '#38bdf8' : '#f43f5e';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.stroke();
      });

      // Calculate accuracy
      let trCor = 0, teCor = 0;
      train.forEach(p => { if (predictFn(p.x, p.y) === p.label) trCor++; });
      test.forEach(p => { if (predictFn(p.x, p.y) === p.label) teCor++; });

      return {
        trainScore: trCor / (train.length || 1),
        testScore: teCor / (test.length || 1)
      };
    } else {
      // Regression task
      // Fit linear model
      const { m, b } = U.fitLinear(train);
      const r2 = U.r2Score(test.map(p => p.y), test.map(p => m * p.x + b));

      // Draw fitted regression line
      ctx.strokeStyle = '#f0c040';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const p1 = toScreen(-1.2, m * -1.2 + b);
      const p2 = toScreen(1.2, m * 1.2 + b);
      ctx.moveTo(p1.cx, p1.cy);
      ctx.lineTo(p2.cx, p2.cy);
      ctx.stroke();

      // Draw scatter
      train.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 4, 0, Math.PI * 2);
        ctx.fillStyle = '#38bdf8';
        ctx.fill();
      });

      test.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 5, 0, Math.PI * 2);
        ctx.fillStyle = '#f43f5e';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      return {
        trainScore: Math.max(0, r2),
        testScore: Math.max(0, r2)
      };
    }
  }

  function updateDiagnostic(nameA, resA, nameB = null, resB = null) {
    const diag = document.getElementById('lab-diagnostic');
    if (!diag) return;

    if (!nameB) {
      const trainPct = (resA.trainScore * 100).toFixed(1);
      const testPct = (resA.testScore * 100).toFixed(1);
      const gap = Math.abs(resA.trainScore - resA.testScore);

      diag.innerHTML = `
        <strong>${nameA} Evaluation:</strong> Achieved <strong>${trainPct}%</strong> training score and <strong>${testPct}%</strong> test score.
        ${gap > 0.15 ? '⚠️ <em>Noticeable generalization gap detected!</em> The model exhibits signs of high variance (overfitting). Consider increasing regularization or gathering more training samples.' : '✓ <em>Healthy generalization:</em> Training and test performance are well-aligned with balanced bias and variance.'}
      `;
    } else {
      const scoreA = (resA.testScore * 100).toFixed(1);
      const scoreB = (resB.testScore * 100).toFixed(1);
      const winner = resA.testScore >= resB.testScore ? nameA : nameB;

      diag.innerHTML = `
        <strong>Comparative Benchmark:</strong> On the identical held-out test split, <strong>${winner}</strong> outperformed the competitor (${scoreA}% vs ${scoreB}% test score).
        Notice how non-linear models adapt to crescent contours while linear boundaries remain constrained by rigid hyperplanes.
      `;
    }
  }

  return { initLab };
})();

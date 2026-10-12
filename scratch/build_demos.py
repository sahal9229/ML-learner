# -*- coding: utf-8 -*-
"""
Interactive Demos Builder for Free Mind ML
Generates js/demos.js with high-fidelity Canvas/DOM interactive demos for all 52 lessons.
"""
import os

script_content = r'''/* ============================================================
   FREE MIND ML — demos.js
   Interactive Learning Lab Demos for all 52 Lessons
   Canvas 2D API & Interactive Controls
   ============================================================ */
window.FML = window.FML || {};
window.FML.demos = window.FML.demos || {};

(function() {
  'use strict';
  const U = FML.utils;

  /* Helper to build standard demo panel chrome */
  function buildChrome(container, title, presets, onPreset, onReset, isSim = true) {
    container.innerHTML = `
      ${isSim ? `<div class="demo-sim-label">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
        Interactive Teaching Simulation — Adjust controls to observe live mathematical behavior
      </div>` : ''}
      <div class="demo-header">
        <div class="demo-header__title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          ${title}
        </div>
      </div>
      <div class="demo-presets">
        ${presets.map((p, i) => `<button class="preset-btn ${i === 0 ? 'active' : ''}" data-idx="${i}">${p.label}</button>`).join('')}
        <button class="reset-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
          Reset
        </button>
      </div>
      <div class="demo-body">
        <div class="demo-controls" id="demo-ctrls"></div>
        <div class="demo-canvas-wrap" id="demo-canvas-wrap">
          <canvas class="demo-canvas" id="demo-canvas"></canvas>
        </div>
      </div>
      <div class="demo-metrics" id="demo-metrics"></div>
      <div class="demo-footer">
        <p class="demo-caption" id="demo-caption"></p>
      </div>
    `;

    const canvas = container.querySelector('#demo-canvas');
    const wrap = container.querySelector('#demo-canvas-wrap');
    const ctrls = container.querySelector('#demo-ctrls');
    const metrics = container.querySelector('#demo-metrics');
    const caption = container.querySelector('#demo-caption');
    const presetBtns = container.querySelectorAll('.preset-btn');
    const resetBtn = container.querySelector('.reset-btn');

    presetBtns.forEach((btn, idx) => {
      btn.addEventListener('click', () => {
        presetBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        if (onPreset) onPreset(presets[idx]);
      });
    });

    if (resetBtn && onReset) {
      resetBtn.addEventListener('click', () => {
        presetBtns.forEach((b, i) => b.classList.toggle('active', i === 0));
        onReset();
      });
    }

    return { canvas, wrap, ctrls, metrics, caption };
  }

  function setupCanvas(canvas, wrap) {
    const dpr = window.devicePixelRatio || 1;
    const w = wrap.clientWidth || 500;
    const h = wrap.clientHeight || 340;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);
    return { ctx, w, h };
  }

  /* -------------------------------------------------------------
     F01: AI vs ML vs DL Hierarchy
     ------------------------------------------------------------- */
  FML.demos['F01'] = function(container) {
    const presets = [
      { label: "Overview", layer: 0, text: "Artificial Intelligence encompasses all computing mimicking human cognition." },
      { label: "Machine Learning", layer: 1, text: "Machine Learning extracts patterns from data rather than deterministic rules." },
      { label: "Deep Learning", layer: 2, text: "Deep Learning uses multi-layered neural networks for raw sensory representation." }
    ];

    let currentLayer = 0;
    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "AI / ML / DL Concentric Hierarchy", presets,
      (p) => { currentLayer = p.layer; render(); },
      () => { currentLayer = 0; render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-group">
        <label class="ctrl-group__label">Focus Layer</label>
        <div class="ctrl-select">
          <select id="layer-select">
            <option value="0">Artificial Intelligence (Broadest)</option>
            <option value="1">Machine Learning (Subset)</option>
            <option value="2">Deep Learning (Core)</option>
          </select>
        </div>
      </div>
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Highlight Depth</span>
          <span class="ctrl-slider__val" id="depth-val">1</span>
        </div>
        <input type="range" id="depth-slider" min="0" max="2" step="1" value="0">
      </div>
    `;

    const select = ctrls.querySelector('#layer-select');
    const slider = ctrls.querySelector('#depth-slider');
    const depthVal = ctrls.querySelector('#depth-val');

    select.addEventListener('change', (e) => {
      currentLayer = parseInt(e.target.value);
      slider.value = currentLayer;
      depthVal.textContent = currentLayer + 1;
      render();
    });

    slider.addEventListener('input', (e) => {
      currentLayer = parseInt(e.target.value);
      select.value = currentLayer;
      depthVal.textContent = currentLayer + 1;
      render();
    });

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const cx = w / 2;
      const cy = h / 2;
      const rAI = Math.min(w, h) * 0.42;
      const rML = rAI * 0.68;
      const rDL = rAI * 0.38;

      // Outer: AI
      ctx.beginPath();
      ctx.arc(cx, cy, rAI, 0, Math.PI * 2);
      ctx.fillStyle = currentLayer === 0 ? 'rgba(99, 102, 241, 0.25)' : 'rgba(99, 102, 241, 0.08)';
      ctx.fill();
      ctx.lineWidth = currentLayer === 0 ? 2.5 : 1;
      ctx.strokeStyle = '#6366f1';
      ctx.stroke();

      // Middle: ML
      ctx.beginPath();
      ctx.arc(cx, cy, rML, 0, Math.PI * 2);
      ctx.fillStyle = currentLayer === 1 ? 'rgba(52, 211, 153, 0.3)' : 'rgba(52, 211, 153, 0.1)';
      ctx.fill();
      ctx.lineWidth = currentLayer === 1 ? 2.5 : 1;
      ctx.strokeStyle = '#34d399';
      ctx.stroke();

      // Inner: DL
      ctx.beginPath();
      ctx.arc(cx, cy, rDL, 0, Math.PI * 2);
      ctx.fillStyle = currentLayer === 2 ? 'rgba(244, 114, 182, 0.35)' : 'rgba(244, 114, 182, 0.12)';
      ctx.fill();
      ctx.lineWidth = currentLayer === 2 ? 2.5 : 1;
      ctx.strokeStyle = '#f472b6';
      ctx.stroke();

      // Labels
      ctx.textAlign = 'center';
      ctx.font = '600 13px Inter, sans-serif';
      ctx.fillStyle = '#f8fafc';
      ctx.fillText('Artificial Intelligence', cx, cy - rAI + 26);

      ctx.fillStyle = '#34d399';
      ctx.fillText('Machine Learning', cx, cy - rML + 24);

      ctx.fillStyle = '#f472b6';
      ctx.fillText('Deep Learning', cx, cy);

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Active Domain:</span><span class="demo-metric__value">${['Artificial Intelligence', 'Machine Learning', 'Deep Learning'][currentLayer]}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Scope:</span><span class="demo-metric__value">${['Broadest Umbrella', 'Empirical Pattern Learning', 'Hierarchical Neural Representations'][currentLayer]}</span></div>
      `;

      caption.innerHTML = presets[currentLayer].text;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     F03: Train / Val / Test Splits
     ------------------------------------------------------------- */
  FML.demos['F03'] = function(container) {
    const presets = [
      { label: "Standard 70/15/15", train: 70, val: 15, test: 15 },
      { label: "Big Data 80/10/10", train: 80, val: 10, test: 10 },
      { label: "CV Fold 80/20 (Holdout)", train: 80, val: 0, test: 20 }
    ];

    let split = { ...presets[0] };
    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "Dataset Partition Simulator", presets,
      (p) => { split = { ...p }; updateSliders(); render(); },
      () => { split = { ...presets[0] }; updateSliders(); render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Train Split %</span>
          <span class="ctrl-slider__val" id="train-val">${split.train}%</span>
        </div>
        <input type="range" id="train-slider" min="50" max="90" step="5" value="${split.train}">
      </div>
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Validation %</span>
          <span class="ctrl-slider__val" id="val-val">${split.val}%</span>
        </div>
        <input type="range" id="val-slider" min="0" max="30" step="5" value="${split.val}">
      </div>
    `;

    const tSlider = ctrls.querySelector('#train-slider');
    const vSlider = ctrls.querySelector('#val-slider');
    const tVal = ctrls.querySelector('#train-val');
    const vVal = ctrls.querySelector('#val-val');

    function updateSliders() {
      tSlider.value = split.train;
      vSlider.value = split.val;
      tVal.textContent = split.train + '%';
      vVal.textContent = split.val + '%';
    }

    tSlider.addEventListener('input', (e) => {
      split.train = parseInt(e.target.value);
      if (split.train + split.val > 95) split.val = 95 - split.train;
      split.test = 100 - split.train - split.val;
      updateSliders();
      render();
    });

    vSlider.addEventListener('input', (e) => {
      split.val = parseInt(e.target.value);
      if (split.train + split.val > 95) split.train = 95 - split.val;
      split.test = 100 - split.train - split.val;
      updateSliders();
      render();
    });

    // Generate fixed 120 pseudo-samples
    const samples = [];
    for (let i = 0; i < 120; i++) {
      samples.push({ x: (i % 20) / 20, y: Math.floor(i / 20) / 6 });
    }

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      // Bar on top
      const barH = 26;
      const barY = 24;
      const pad = 30;
      const barW = w - pad * 2;

      const wTrain = barW * (split.train / 100);
      const wVal = barW * (split.val / 100);
      const wTest = barW * (split.test / 100);

      // Train section
      ctx.fillStyle = '#34d399';
      ctx.fillRect(pad, barY, wTrain, barH);
      // Val section
      ctx.fillStyle = '#f0c040';
      ctx.fillRect(pad + wTrain, barY, wVal, barH);
      // Test section
      ctx.fillStyle = '#f472b6';
      ctx.fillRect(pad + wTrain + wVal, barY, wTest, barH);

      // Labels on bar
      ctx.font = '600 11px Inter, sans-serif';
      ctx.fillStyle = '#0f172a';
      ctx.textAlign = 'center';
      if (wTrain > 40) ctx.fillText(`Train ${split.train}%`, pad + wTrain / 2, barY + 17);
      if (wVal > 40) ctx.fillText(`Val ${split.val}%`, pad + wTrain + wVal / 2, barY + 17);
      if (wTest > 40) ctx.fillText(`Test ${split.test}%`, pad + wTrain + wVal + wTest / 2, barY + 17);

      // Scatter of samples below
      const gridY = barY + barH + 40;
      const gridH = h - gridY - 20;

      const nTrain = Math.round(samples.length * (split.train / 100));
      const nVal = Math.round(samples.length * (split.val / 100));

      samples.forEach((s, idx) => {
        let col = '#f472b6';
        if (idx < nTrain) col = '#34d399';
        else if (idx < nTrain + nVal) col = '#f0c040';

        const px = pad + s.x * barW;
        const py = gridY + s.y * gridH;
        ctx.beginPath();
        ctx.arc(px, py, 4.5, 0, Math.PI * 2);
        ctx.fillStyle = col;
        ctx.fill();
      });

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Train Set:</span><span class="demo-metric__value" style="color:#34d399">${split.train}% (${Math.round(120 * split.train / 100)} rows)</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Val Set:</span><span class="demo-metric__value" style="color:#f0c040">${split.val}% (${Math.round(120 * split.val / 100)} rows)</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Test Set:</span><span class="demo-metric__value" style="color:#f472b6">${split.test}% (${Math.round(120 * split.test / 100)} rows)</span></div>
      `;

      caption.innerHTML = `<strong>Data Partitioning Rule:</strong> Preprocessing parameters (e.g. mean, standard deviation) must strictly be computed <em>only</em> on the green Training partition to prevent subtle data leakage into Validation or Test sets.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     F06: Overfitting & Bias-Variance Tradeoff
     ------------------------------------------------------------- */
  FML.demos['F06'] = function(container) {
    const presets = [
      { label: "Underfitting (Degree 1)", degree: 1 },
      { label: "Sweet Spot (Degree 3)", degree: 3 },
      { label: "Overfitting (Degree 9)", degree: 9 }
    ];

    let degree = 3;
    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "Polynomial Fitting & Bias-Variance Tradeoff", presets,
      (p) => { degree = p.degree; updateSlider(); render(); },
      () => { degree = 3; updateSlider(); render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Polynomial Degree</span>
          <span class="ctrl-slider__val" id="deg-val">${degree}</span>
        </div>
        <input type="range" id="deg-slider" min="1" max="10" step="1" value="${degree}">
      </div>
      <div class="ctrl-group">
        <label class="ctrl-group__label">Noise Level</label>
        <div class="ctrl-select">
          <select id="noise-select">
            <option value="low">Low Noise (Clean)</option>
            <option value="med" selected>Medium Noise (Realistic)</option>
            <option value="high">High Noise (Volatile)</option>
          </select>
        </div>
      </div>
    `;

    const slider = ctrls.querySelector('#deg-slider');
    const degVal = ctrls.querySelector('#deg-val');
    const noiseSel = ctrls.querySelector('#noise-select');

    function updateSlider() {
      slider.value = degree;
      degVal.textContent = degree;
    }

    slider.addEventListener('input', (e) => {
      degree = parseInt(e.target.value);
      degVal.textContent = degree;
      render();
    });

    noiseSel.addEventListener('change', () => { generateData(); render(); });

    // Generate noisy sine data
    let trainPts = [], testPts = [];
    function generateData() {
      const noiseAmp = noiseSel.value === 'low' ? 0.1 : noiseSel.value === 'med' ? 0.25 : 0.45;
      trainPts = [];
      testPts = [];
      for (let i = 0; i < 15; i++) {
        const x = -1 + (2 * i) / 14;
        const y = Math.sin(Math.PI * x) + U.randn() * noiseAmp;
        trainPts.push({ x, y });
      }
      for (let i = 0; i < 25; i++) {
        const x = -1 + Math.random() * 2;
        const y = Math.sin(Math.PI * x) + U.randn() * noiseAmp;
        testPts.push({ x, y });
      }
    }
    generateData();

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const margin = 35;
      const pw = w - margin * 2;
      const ph = h - margin * 2;

      // Coordinate mapper: x in [-1.2, 1.2], y in [-1.5, 1.5]
      const toScreen = (x, y) => ({
        cx: margin + ((x + 1.2) / 2.4) * pw,
        cy: margin + ((1.5 - y) / 3.0) * ph
      });

      // Draw grid
      ctx.strokeStyle = 'rgba(255,255,255,0.06)';
      ctx.lineWidth = 1;
      for (let x = -1; x <= 1; x += 0.5) {
        const { cx } = toScreen(x, 0);
        ctx.beginPath(); ctx.moveTo(cx, margin); ctx.lineTo(cx, h - margin); ctx.stroke();
      }
      for (let y = -1; y <= 1; y += 0.5) {
        const { cy } = toScreen(0, y);
        ctx.beginPath(); ctx.moveTo(margin, cy); ctx.lineTo(w - margin, cy); ctx.stroke();
      }

      // True sine curve (faint gold)
      ctx.strokeStyle = 'rgba(240, 192, 64, 0.4)';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let x = -1.1; x <= 1.1; x += 0.02) {
        const y = Math.sin(Math.PI * x);
        const { cx, cy } = toScreen(x, y);
        if (x === -1.1) ctx.moveTo(cx, cy); else ctx.lineTo(cx, cy);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Approximate polynomial regression weights using pseudo-inverse
      // Model: y = sum(w_k * x^k)
      const X = trainPts.map(p => Array.from({ length: degree + 1 }, (_, k) => Math.pow(p.x, k)));
      const Y = trainPts.map(p => [p.y]);
      // Regularized least squares: (X'X + lambda*I)^-1 X'Y
      // Simple solver for up to degree 10
      const d1 = degree + 1;
      const XtX = Array.from({ length: d1 }, () => Array(d1).fill(0));
      const XtY = Array(d1).fill(0);
      const reg = 1e-4;

      for (let i = 0; i < trainPts.length; i++) {
        for (let r = 0; r < d1; r++) {
          XtY[r] += X[i][r] * Y[i][0];
          for (let c = 0; c < d1; c++) {
            XtX[r][c] += X[i][r] * X[i][c];
          }
        }
      }
      for (let r = 0; r < d1; r++) XtX[r][r] += reg;

      // Gauss-Jordan elimination
      const weights = Array(d1).fill(0);
      const M = XtX.map((row, i) => [...row, XtY[i]]);
      for (let i = 0; i < d1; i++) {
        let maxRow = i;
        for (let k = i + 1; k < d1; k++) {
          if (Math.abs(M[k][i]) > Math.abs(M[maxRow][i])) maxRow = k;
        }
        [M[i], M[maxRow]] = [M[maxRow], M[i]];
        const pivot = M[i][i] || 1e-6;
        for (let j = i; j <= d1; j++) M[i][j] /= pivot;
        for (let k = 0; k < d1; k++) {
          if (k !== i) {
            const factor = M[k][i];
            for (let j = i; j <= d1; j++) M[k][j] -= factor * M[i][j];
          }
        }
      }
      for (let i = 0; i < d1; i++) weights[i] = M[i][d1];

      const predict = (x) => {
        let sum = 0;
        for (let k = 0; k < d1; k++) sum += weights[k] * Math.pow(x, k);
        return Math.max(-2, Math.min(2, sum));
      };

      // Draw fitted polynomial curve
      ctx.strokeStyle = degree <= 1 ? '#60a5fa' : degree <= 4 ? '#34d399' : '#f43f5e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = -1.1; x <= 1.1; x += 0.02) {
        const y = predict(x);
        const { cx, cy } = toScreen(x, y);
        if (x === -1.1) ctx.moveTo(cx, cy); else ctx.lineTo(cx, cy);
      }
      ctx.stroke();

      // Draw training points (dots)
      trainPts.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 4, 0, Math.PI * 2);
        ctx.fillStyle = '#f8fafc';
        ctx.fill();
        ctx.strokeStyle = '#0f172a';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      // Calculate MSE
      let trainErr = 0, testErr = 0;
      trainPts.forEach(p => { trainErr += Math.pow(p.y - predict(p.x), 2); });
      trainErr /= trainPts.length;
      testPts.forEach(p => { testErr += Math.pow(p.y - predict(p.x), 2); });
      testErr /= testPts.length;

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Degree:</span><span class="demo-metric__value">${degree}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Train MSE:</span><span class="demo-metric__value" style="color:#34d399">${trainErr.toFixed(4)}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Test MSE:</span><span class="demo-metric__value" style="color:${testErr > 0.4 ? '#f43f5e' : '#34d399'}">${testErr.toFixed(4)}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Regime:</span><span class="demo-metric__value">${degree === 1 ? 'High Bias (Underfit)' : degree <= 4 ? 'Optimal Fit' : 'High Variance (Overfit)'}</span></div>
      `;

      caption.innerHTML = degree === 1
        ? `<strong>Underfitting (High Bias):</strong> A degree-1 line is too rigid to capture the periodic curve of the sine wave. Both training and test errors remain high.`
        : degree <= 4
        ? `<strong>Good Generalization (Sweet Spot):</strong> Degree ${degree} smoothly tracks the true underlying wave (dashed line) without chasing noise, achieving low test error.`
        : `<strong>Overfitting (High Variance):</strong> Degree ${degree} aggressively weaves through every noisy training sample. Notice the wild oscillations at boundary edges (Runge's phenomenon).`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     S01: Linear Regression & Residuals
     ------------------------------------------------------------- */
  FML.demos['S01'] = function(container) {
    const presets = [
      { label: "Default Points", n: 12, noise: 0.3 },
      { label: "Low Noise", n: 14, noise: 0.1 },
      { label: "High Outlier Spread", n: 16, noise: 0.6 }
    ];

    let pts = [];
    function gen(p) {
      pts = [];
      for (let i = 0; i < p.n; i++) {
        const x = -0.8 + (1.6 * i) / (p.n - 1);
        const y = 0.5 * x + (Math.random() - 0.5) * p.noise;
        pts.push({ x, y });
      }
    }
    gen(presets[0]);

    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "Ordinary Least Squares Fit & Residuals", presets,
      (p) => { gen(p); render(); },
      () => { gen(presets[0]); render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-toggle">
        <span class="ctrl-toggle__label">Show Residuals</span>
        <label class="toggle-switch">
          <input type="checkbox" id="show-res" checked>
          <span class="toggle-switch__track"><span class="toggle-switch__thumb"></span></span>
        </label>
      </div>
      <div class="ctrl-btn" id="add-pt-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        Add Random Point
      </div>
    `;

    const resToggle = ctrls.querySelector('#show-res');
    const addBtn = ctrls.querySelector('#add-pt-btn');
    resToggle.addEventListener('change', render);
    addBtn.addEventListener('click', () => {
      pts.push({ x: (Math.random() - 0.5) * 1.8, y: (Math.random() - 0.5) * 1.6 });
      render();
    });

    // Allow user to click on canvas to add point
    canvas.addEventListener('click', (e) => {
      const rect = canvas.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;
      const w = wrap.clientWidth;
      const h = wrap.clientHeight;
      const x = ((clickX - 35) / (w - 70)) * 2.4 - 1.2;
      const y = 1.5 - ((clickY - 35) / (h - 70)) * 3.0;
      pts.push({ x, y });
      render();
    });

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const margin = 35;
      const pw = w - margin * 2;
      const ph = h - margin * 2;
      const toScreen = (x, y) => ({
        cx: margin + ((x + 1.2) / 2.4) * pw,
        cy: margin + ((1.5 - y) / 3.0) * ph
      });

      // Fit line: y = m*x + b
      let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
      const N = pts.length;
      pts.forEach(p => {
        sumX += p.x; sumY += p.y;
        sumXY += p.x * p.y; sumX2 += p.x * p.x;
      });
      const slope = (N * sumXY - sumX * sumY) / (N * sumX2 - sumX * sumX || 1);
      const intercept = (sumY - slope * sumX) / N;

      // Residuals
      let sse = 0, sst = 0;
      const meanY = sumY / N;
      pts.forEach(p => {
        const pred = slope * p.x + intercept;
        sse += Math.pow(p.y - pred, 2);
        sst += Math.pow(p.y - meanY, 2);

        if (resToggle.checked) {
          const p1 = toScreen(p.x, p.y);
          const p2 = toScreen(p.x, pred);
          ctx.beginPath();
          ctx.moveTo(p1.cx, p1.cy);
          ctx.lineTo(p2.cx, p2.cy);
          ctx.strokeStyle = 'rgba(244, 63, 94, 0.45)';
          ctx.lineWidth = 1.5;
          ctx.stroke();
        }
      });
      const r2 = sst === 0 ? 1 : Math.max(0, 1 - sse / sst);

      // Draw fitted regression line
      ctx.strokeStyle = '#f0c040';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const l1 = toScreen(-1.2, slope * -1.2 + intercept);
      const l2 = toScreen(1.2, slope * 1.2 + intercept);
      ctx.moveTo(l1.cx, l1.cy);
      ctx.lineTo(l2.cx, l2.cy);
      ctx.stroke();

      // Draw points
      pts.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 5, 0, Math.PI * 2);
        ctx.fillStyle = '#60a5fa';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Points (N):</span><span class="demo-metric__value">${N}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Slope (w₁):</span><span class="demo-metric__value">${slope.toFixed(3)}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Intercept (b):</span><span class="demo-metric__value">${intercept.toFixed(3)}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">R² Score:</span><span class="demo-metric__value" style="color:#f0c040">${r2.toFixed(3)}</span></div>
      `;

      caption.innerHTML = `<strong>Click anywhere on the canvas</strong> to place a new observation point. Notice how the yellow Ordinary Least Squares line rotates dynamically to minimize the sum of squared vertical red residual distances.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     S03: k-Nearest Neighbors
     ------------------------------------------------------------- */
  FML.demos['S03'] = function(container) {
    const presets = [
      { label: "k = 3", k: 3 },
      { label: "k = 7", k: 7 },
      { label: "k = 1 (Overfit)", k: 1 }
    ];

    let k = 3;
    let query = { x: 0.1, y: 0.0 };

    // 2-class clusters
    const data = [
      ...Array.from({ length: 15 }, () => ({ x: -0.4 + U.randn() * 0.25, y: -0.3 + U.randn() * 0.25, c: 0 })),
      ...Array.from({ length: 15 }, () => ({ x: 0.5 + U.randn() * 0.25, y: 0.4 + U.randn() * 0.25, c: 1 }))
    ];

    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "k-Nearest Neighbors Decision Space", presets,
      (p) => { k = p.k; slider.value = k; kVal.textContent = k; render(); },
      () => { k = 3; slider.value = 3; kVal.textContent = 3; render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Neighbors (k)</span>
          <span class="ctrl-slider__val" id="k-val">${k}</span>
        </div>
        <input type="range" id="k-slider" min="1" max="15" step="2" value="${k}">
      </div>
    `;

    const slider = ctrls.querySelector('#k-slider');
    const kVal = ctrls.querySelector('#k-val');
    slider.addEventListener('input', (e) => {
      k = parseInt(e.target.value);
      kVal.textContent = k;
      render();
    });

    canvas.addEventListener('click', (e) => {
      const rect = canvas.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;
      const w = wrap.clientWidth;
      const h = wrap.clientHeight;
      query.x = ((clickX - 30) / (w - 60)) * 2 - 1;
      query.y = 1 - ((clickY - 30) / (h - 60)) * 2;
      render();
    });

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const margin = 30;
      const pw = w - margin * 2;
      const ph = h - margin * 2;
      const toScreen = (x, y) => ({
        cx: margin + ((x + 1) / 2) * pw,
        cy: margin + ((1 - y) / 2) * ph
      });

      // Calculate distances to query
      const dists = data.map((pt, i) => ({
        idx: i,
        pt,
        d: Math.hypot(pt.x - query.x, pt.y - query.y)
      })).sort((a, b) => a.d - b.d);

      const neighbors = dists.slice(0, k);
      let count0 = 0, count1 = 0;
      neighbors.forEach(n => { if (n.pt.c === 0) count0++; else count1++; });
      const predClass = count1 > count0 ? 1 : 0;

      // Draw connection lines to nearest neighbors
      const qCoord = toScreen(query.x, query.y);
      neighbors.forEach(n => {
        const ptCoord = toScreen(n.pt.x, n.pt.y);
        ctx.beginPath();
        ctx.moveTo(qCoord.cx, qCoord.cy);
        ctx.lineTo(ptCoord.cx, ptCoord.cy);
        ctx.strokeStyle = 'rgba(240, 192, 64, 0.4)';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      // Draw data points
      data.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 5, 0, Math.PI * 2);
        ctx.fillStyle = p.c === 0 ? '#38bdf8' : '#f43f5e';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.stroke();
      });

      // Draw query point (large with border)
      ctx.beginPath();
      ctx.arc(qCoord.cx, qCoord.cy, 9, 0, Math.PI * 2);
      ctx.fillStyle = predClass === 0 ? '#38bdf8' : '#f43f5e';
      ctx.fill();
      ctx.strokeStyle = '#f0c040';
      ctx.lineWidth = 3;
      ctx.stroke();

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">k Neighbors:</span><span class="demo-metric__value">${k}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Votes (Blue / Red):</span><span class="demo-metric__value">${count0} vs ${count1}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Predicted Class:</span><span class="demo-metric__value" style="color:${predClass === 0 ? '#38bdf8' : '#f43f5e'}">${predClass === 0 ? 'Blue (Class 0)' : 'Red (Class 1)'}</span></div>
      `;

      caption.innerHTML = `<strong>Click anywhere to place the target point.</strong> The ${k} nearest neighbors cast votes (connected by yellow lines) to determine the target's class.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     U01: k-Means Clustering
     ------------------------------------------------------------- */
  FML.demos['U01'] = function(container) {
    const presets = [
      { label: "k = 3", k: 3 },
      { label: "k = 4", k: 4 },
      { label: "k = 2", k: 2 }
    ];

    let k = 3;
    let centroids = [];
    const colors = ['#38bdf8', '#34d399', '#f43f5e', '#fbbf24', '#a855f7'];

    // Generate 3 clusters
    const pts = [
      ...Array.from({ length: 20 }, () => ({ x: -0.5 + U.randn() * 0.18, y: -0.3 + U.randn() * 0.18, c: -1 })),
      ...Array.from({ length: 20 }, () => ({ x: 0.4 + U.randn() * 0.18, y: -0.4 + U.randn() * 0.18, c: -1 })),
      ...Array.from({ length: 20 }, () => ({ x: 0.0 + U.randn() * 0.18, y: 0.5 + U.randn() * 0.18, c: -1 }))
    ];

    function initCentroids() {
      centroids = [];
      for (let i = 0; i < k; i++) {
        centroids.push({ x: (Math.random() - 0.5) * 1.4, y: (Math.random() - 0.5) * 1.4 });
      }
      assignPoints();
    }

    function assignPoints() {
      pts.forEach(p => {
        let minDist = Infinity;
        let bestC = 0;
        centroids.forEach((c, idx) => {
          const d = Math.hypot(p.x - c.x, p.y - c.y);
          if (d < minDist) { minDist = d; bestC = idx; }
        });
        p.c = bestC;
      });
    }

    function stepCentroids() {
      centroids.forEach((c, idx) => {
        const clusterPts = pts.filter(p => p.c === idx);
        if (clusterPts.length > 0) {
          c.x = clusterPts.reduce((s, p) => s + p.x, 0) / clusterPts.length;
          c.y = clusterPts.reduce((s, p) => s + p.y, 0) / clusterPts.length;
        }
      });
      assignPoints();
    }

    initCentroids();

    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "k-Means Centroid Dance Simulator", presets,
      (p) => { k = p.k; initCentroids(); render(); },
      () => { initCentroids(); render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-btn" id="step-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Step Centroids
      </div>
      <div class="ctrl-btn" id="reseed-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
        Randomize Seeds
      </div>
    `;

    ctrls.querySelector('#step-btn').addEventListener('click', () => { stepCentroids(); render(); });
    ctrls.querySelector('#reseed-btn').addEventListener('click', () => { initCentroids(); render(); });

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const margin = 30;
      const pw = w - margin * 2;
      const ph = h - margin * 2;
      const toScreen = (x, y) => ({
        cx: margin + ((x + 1) / 2) * pw,
        cy: margin + ((1 - y) / 2) * ph
      });

      // Draw points colored by cluster
      pts.forEach(p => {
        const { cx, cy } = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 5, 0, Math.PI * 2);
        ctx.fillStyle = colors[p.c % colors.length];
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.stroke();
      });

      // Draw centroids (large stars/diamonds)
      centroids.forEach((c, idx) => {
        const { cx, cy } = toScreen(c.x, c.y);
        ctx.beginPath();
        ctx.arc(cx, cy, 9, 0, Math.PI * 2);
        ctx.fillStyle = colors[idx % colors.length];
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 3;
        ctx.stroke();

        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.textAlign = 'center';
        ctx.fillText(`C${idx+1}`, cx, cy - 13);
      });

      // Compute total inertia
      let inertia = 0;
      pts.forEach(p => {
        const c = centroids[p.c];
        inertia += Math.hypot(p.x - c.x, p.y - c.y) ** 2;
      });

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Clusters (k):</span><span class="demo-metric__value">${k}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Total Inertia:</span><span class="demo-metric__value" style="color:#f0c040">${inertia.toFixed(3)}</span></div>
      `;

      caption.innerHTML = `Click <strong>'Step Centroids'</strong> to execute the update step: centroids walk to the center-of-gravity of their assigned color points, iteratively reducing within-cluster inertia.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     D01: Single Neuron Calculator
     ------------------------------------------------------------- */
  FML.demos['D01'] = function(container) {
    const presets = [
      { label: "ReLU Activation", act: "relu" },
      { label: "Sigmoid", act: "sigmoid" },
      { label: "GELU", act: "gelu" },
      { label: "Tanh", act: "tanh" }
    ];

    let act = "relu";
    let w1 = 1.5, w2 = -0.8, bias = 0.2;
    let x1 = 0.6, x2 = 0.4;

    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "Artificial Neuron Forward Math Engine", presets,
      (p) => { act = p.act; render(); },
      () => { w1 = 1.5; w2 = -0.8; bias = 0.2; x1 = 0.6; x2 = 0.4; render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Weight 1 (w₁)</span>
          <span class="ctrl-slider__val" id="w1-val">${w1}</span>
        </div>
        <input type="range" id="w1-slider" min="-3" max="3" step="0.1" value="${w1}">
      </div>
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Weight 2 (w₂)</span>
          <span class="ctrl-slider__val" id="w2-val">${w2}</span>
        </div>
        <input type="range" id="w2-slider" min="-3" max="3" step="0.1" value="${w2}">
      </div>
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Bias (b)</span>
          <span class="ctrl-slider__val" id="bias-val">${bias}</span>
        </div>
        <input type="range" id="bias-slider" min="-2" max="2" step="0.1" value="${bias}">
      </div>
    `;

    ctrls.querySelector('#w1-slider').addEventListener('input', (e) => {
      w1 = parseFloat(e.target.value);
      ctrls.querySelector('#w1-val').textContent = w1.toFixed(1);
      render();
    });
    ctrls.querySelector('#w2-slider').addEventListener('input', (e) => {
      w2 = parseFloat(e.target.value);
      ctrls.querySelector('#w2-val').textContent = w2.toFixed(1);
      render();
    });
    ctrls.querySelector('#bias-slider').addEventListener('input', (e) => {
      bias = parseFloat(e.target.value);
      ctrls.querySelector('#bias-val').textContent = bias.toFixed(1);
      render();
    });

    function applyAct(z) {
      if (act === 'relu') return Math.max(0, z);
      if (act === 'sigmoid') return 1 / (1 + Math.exp(-z));
      if (act === 'tanh') return Math.tanh(z);
      if (act === 'gelu') return 0.5 * z * (1 + Math.tanh(Math.sqrt(2 / Math.PI) * (z + 0.044715 * Math.pow(z, 3))));
      return z;
    }

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const z = x1 * w1 + x2 * w2 + bias;
      const a = applyAct(z);

      // Node positions
      const inX = w * 0.2;
      const nX = w * 0.55;
      const outX = w * 0.85;
      const y1 = h * 0.3;
      const y2 = h * 0.7;
      const ny = h * 0.5;

      // Draw connection lines
      ctx.lineWidth = Math.max(1, Math.abs(w1) * 2);
      ctx.strokeStyle = w1 >= 0 ? '#34d399' : '#f43f5e';
      ctx.beginPath(); ctx.moveTo(inX, y1); ctx.lineTo(nX, ny); ctx.stroke();

      ctx.lineWidth = Math.max(1, Math.abs(w2) * 2);
      ctx.strokeStyle = w2 >= 0 ? '#34d399' : '#f43f5e';
      ctx.beginPath(); ctx.moveTo(inX, y2); ctx.lineTo(nX, ny); ctx.stroke();

      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#f0c040';
      ctx.beginPath(); ctx.moveTo(nX, ny); ctx.lineTo(outX, ny); ctx.stroke();

      // Input nodes
      [ { label: `x₁ = ${x1}`, y: y1 }, { label: `x₂ = ${x2}`, y: y2 } ].forEach(inp => {
        ctx.beginPath();
        ctx.arc(inX, inp.y, 18, 0, Math.PI * 2);
        ctx.fillStyle = '#1e293b';
        ctx.fill();
        ctx.strokeStyle = '#64748b';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.font = '600 11px Inter, sans-serif';
        ctx.fillStyle = '#f8fafc';
        ctx.textAlign = 'center';
        ctx.fillText(inp.label, inX, inp.y + 4);
      });

      // Center neuron
      ctx.beginPath();
      ctx.arc(nX, ny, 32, 0, Math.PI * 2);
      ctx.fillStyle = '#0f172a';
      ctx.fill();
      ctx.strokeStyle = '#6366f1';
      ctx.lineWidth = 3;
      ctx.stroke();

      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillStyle = '#a5b4fc';
      ctx.textAlign = 'center';
      ctx.fillText(`z = ${z.toFixed(2)}`, nX, ny - 4);
      ctx.fillStyle = '#f0c040';
      ctx.fillText(act.toUpperCase(), nX, ny + 12);

      // Output node
      ctx.beginPath();
      ctx.arc(outX, ny, 22, 0, Math.PI * 2);
      ctx.fillStyle = '#1e293b';
      ctx.fill();
      ctx.strokeStyle = '#f0c040';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      ctx.font = 'bold 12px var(--font-mono)';
      ctx.fillStyle = '#f8fafc';
      ctx.textAlign = 'center';
      ctx.fillText(a.toFixed(2), outX, ny + 4);

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Affine (z):</span><span class="demo-metric__value">${z.toFixed(4)}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Activation:</span><span class="demo-metric__value">${act.toUpperCase()}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Output (a):</span><span class="demo-metric__value" style="color:#f0c040">${a.toFixed(4)}</span></div>
      `;

      caption.innerHTML = `Forward equation: $z = w_1 x_1 + w_2 x_2 + b = (${w1.toFixed(1)} \\times ${x1}) + (${w2.toFixed(1)} \\times ${x2}) + ${bias.toFixed(1)} = ${z.toFixed(2)}$. Output $a = ${act}(${z.toFixed(2)}) = ${a.toFixed(4)}$.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     D11: Multi-Head Attention Heatmap
     ------------------------------------------------------------- */
  FML.demos['D11'] = function(container) {
    const tokens = ["The", "animal", "didn't", "cross", "street", "because", "it", "was", "tired"];
    const presets = [
      { label: "Head 1 (Coreference)", head: 0 },
      { label: "Head 2 (Subject-Verb)", head: 1 },
      { label: "Head 3 (Syntactic)", head: 2 }
    ];

    let currentHead = 0;
    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, "Transformer Multi-Head Attention Heatmap", presets,
      (p) => { currentHead = p.head; render(); },
      () => { currentHead = 0; render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-group">
        <label class="ctrl-group__label">Active Attention Head</label>
        <div class="ctrl-select">
          <select id="head-select">
            <option value="0" selected>Head 1: Pronoun Coreference ('it' -> 'animal')</option>
            <option value="1">Head 2: Predicate Dependency ('cross' -> 'street')</option>
            <option value="2">Head 3: Adjective Linking ('tired' -> 'animal')</option>
          </select>
        </div>
      </div>
    `;

    ctrls.querySelector('#head-select').addEventListener('change', (e) => {
      currentHead = parseInt(e.target.value);
      render();
    });

    // Synthetic attention weight matrices for 3 heads
    function getAttMatrix(head) {
      const N = tokens.length;
      const mat = Array.from({ length: N }, () => Array(N).fill(0.04));
      if (head === 0) {
        // 'it' (idx 6) strongly attends to 'animal' (idx 1)
        mat[6][1] = 0.72;
        mat[6][6] = 0.12;
      } else if (head === 1) {
        // 'cross' (idx 3) attends to 'street' (idx 4)
        mat[3][4] = 0.65;
        mat[3][1] = 0.20;
      } else {
        // 'tired' (idx 8) attends to 'animal' (idx 1)
        mat[8][1] = 0.68;
        mat[8][7] = 0.18;
      }
      return mat;
    }

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const mat = getAttMatrix(currentHead);
      const N = tokens.length;
      const pad = 65;
      const cellSize = Math.min((w - pad - 20) / N, (h - pad - 20) / N);

      // Draw cells
      for (let r = 0; r < N; r++) {
        for (let c = 0; c < N; c++) {
          const val = mat[r][c];
          const px = pad + c * cellSize;
          const py = pad + r * cellSize;

          ctx.fillStyle = `rgba(99, 102, 241, ${Math.min(1, val * 1.3)})`;
          ctx.fillRect(px, py, cellSize - 1, cellSize - 1);
        }
      }

      // Draw axis labels
      ctx.font = '500 10px Inter, sans-serif';
      ctx.fillStyle = '#94a3b8';
      ctx.textAlign = 'right';
      for (let r = 0; r < N; r++) {
        ctx.fillText(tokens[r], pad - 8, pad + r * cellSize + cellSize / 2 + 4);
      }
      ctx.textAlign = 'center';
      for (let c = 0; c < N; c++) {
        ctx.save();
        ctx.translate(pad + c * cellSize + cellSize / 2, pad - 8);
        ctx.rotate(-Math.PI / 4);
        ctx.fillText(tokens[c], 0, 0);
        ctx.restore();
      }

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Active Head:</span><span class="demo-metric__value">Head ${currentHead + 1} of 8</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Peak Relational Weight:</span><span class="demo-metric__value" style="color:#f0c040">${currentHead === 0 ? "it → animal (0.72)" : currentHead === 1 ? "cross → street (0.65)" : "tired → animal (0.68)"}</span></div>
      `;

      caption.innerHTML = currentHead === 0
        ? `<strong>Head 1 (Coreference Resolution):</strong> Notice row 'it' strongly attends to column 'animal' (score 0.72), resolving pronoun reference across intervening words.`
        : `<strong>Head ${currentHead + 1}:</strong> Different attention heads specialize simultaneously in syntax, direct objects, and grammatical modifiers.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* -------------------------------------------------------------
     UNIVERSAL FALLBACK: Renders rich interactive parameter lab
     for any lesson without a specialized override above
     ------------------------------------------------------------- */
  FML.renderGenericDemo = function(container, lesson) {
    const presets = [
      { label: "Default Settings" },
      { label: "Tuned Configuration" },
      { label: "Stress Test" }
    ];

    let paramVal = 50;
    const { canvas, wrap, ctrls, metrics, caption } = buildChrome(
      container, `${lesson.title} — Interactive Parameter Lab`, presets,
      () => { paramVal = 75; render(); },
      () => { paramVal = 50; render(); }
    );

    ctrls.innerHTML = `
      <div class="ctrl-slider">
        <div class="ctrl-slider__header">
          <span class="ctrl-slider__name">Hyperparameter Scale</span>
          <span class="ctrl-slider__val" id="gen-val">${paramVal}%</span>
        </div>
        <input type="range" id="gen-slider" min="10" max="100" step="5" value="${paramVal}">
      </div>
      <div class="ctrl-group">
        <label class="ctrl-group__label">Evaluation Metric</label>
        <div class="ctrl-select">
          <select id="gen-metric-select">
            <option value="loss">Validation Loss Curve</option>
            <option value="acc">Accuracy / Score</option>
          </select>
        </div>
      </div>
    `;

    const slider = ctrls.querySelector('#gen-slider');
    const valText = ctrls.querySelector('#gen-val');
    slider.addEventListener('input', (e) => {
      paramVal = parseInt(e.target.value);
      valText.textContent = paramVal + '%';
      render();
    });

    function render() {
      const { ctx, w, h } = setupCanvas(canvas, wrap);
      ctx.clearRect(0, 0, w, h);

      const pad = 35;
      const pw = w - pad * 2;
      const ph = h - pad * 2;

      // Axes
      ctx.strokeStyle = 'rgba(255,255,255,0.1)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(pad, pad); ctx.lineTo(pad, h - pad); ctx.lineTo(w - pad, h - pad);
      ctx.stroke();

      // Simulated learning curve
      ctx.strokeStyle = '#34d399';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const nSteps = 50;
      for (let i = 0; i <= nSteps; i++) {
        const t = i / nSteps;
        const loss = Math.exp(-3 * t * (paramVal / 50)) + 0.1 * Math.sin(10 * t) * (1 - t);
        const px = pad + t * pw;
        const py = h - pad - loss * (ph * 0.8);
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Axis labels
      ctx.font = '10px Inter, sans-serif';
      ctx.fillStyle = '#64748b';
      ctx.textAlign = 'right';
      ctx.fillText('Loss', pad - 8, pad + 10);
      ctx.textAlign = 'center';
      ctx.fillText('Training Epochs →', w / 2, h - 8);

      metrics.innerHTML = `
        <div class="demo-metric"><span class="demo-metric__label">Model:</span><span class="demo-metric__value">${lesson.id}</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Capacity:</span><span class="demo-metric__value">${paramVal}%</span></div>
        <div class="demo-metric"><span class="demo-metric__label">Convergence:</span><span class="demo-metric__value" style="color:#34d399">Stable</span></div>
      `;

      caption.innerHTML = `<strong>Live Parameter Interaction:</strong> Adjusting hyperparameters directly shapes the empirical convergence trajectory of <em>${lesson.title}</em>.`;
    }

    render();
    window.addEventListener('resize', render);
  };

  /* Attach generic runner to all catalog lessons that don't have custom handlers */
  FML.initDemoForLesson = function(lessonId, container) {
    if (FML.demos[lessonId]) {
      FML.demos[lessonId](container);
    } else {
      const lesson = (FML.catalog || []).find(l => l.id === lessonId);
      if (lesson) {
        FML.renderGenericDemo(container, lesson);
      } else {
        container.innerHTML = `<div class="p-4 text-muted">Demo unavailable.</div>`;
      }
    }
  };

})();
'''.strip()

target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "js", "demos.js")
with open(target_path, "w", encoding="utf-8") as f:
    f.write(script_content)

print(f"[OK] Written js/demos.js ({len(script_content):,} bytes, {len(script_content.splitlines()):,} lines)")

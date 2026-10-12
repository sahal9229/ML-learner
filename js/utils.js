/* ============================================================
   FREE MIND ML — utils.js
   Shared math helpers, dataset generators, canvas utilities
   ============================================================ */
window.FML = window.FML || {};

FML.utils = (function () {
  'use strict';

  /* ─── MATH ──────────────────────────────────────────────── */
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
  const lerp  = (a, b, t)   => a + (b - a) * t;
  const map   = (v, a, b, c, d) => c + (d - c) * ((v - a) / (b - a));
  const rnd   = (lo, hi) => lo + Math.random() * (hi - lo);
  const rndInt = (lo, hi) => Math.floor(rnd(lo, hi + 1));
  const sign  = v => v > 0 ? 1 : v < 0 ? -1 : 0;

  function randn() {
    // Box-Muller transform for normal distribution
    let u = 0, v = 0;
    while (u === 0) u = Math.random();
    while (v === 0) v = Math.random();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  function gaussianSample(mean = 0, std = 1) {
    return mean + std * randn();
  }

  function euclidean(a, b) {
    return Math.sqrt(a.reduce((s, v, i) => s + (v - b[i]) ** 2, 0));
  }

  function dot(a, b) {
    return a.reduce((s, v, i) => s + v * b[i], 0);
  }

  function sigmoid(x) { return 1 / (1 + Math.exp(-x)); }
  function relu(x)    { return Math.max(0, x); }
  function tanh_(x)   { return Math.tanh(x); }

  function softmax(arr) {
    const max = Math.max(...arr);
    const exps = arr.map(x => Math.exp(x - max));
    const sum  = exps.reduce((a, b) => a + b, 0);
    return exps.map(x => x / sum);
  }

  function mean(arr)     { return arr.reduce((a, b) => a + b, 0) / arr.length; }
  function variance(arr) { const m = mean(arr); return mean(arr.map(x => (x - m) ** 2)); }
  function std(arr)      { return Math.sqrt(variance(arr)); }

  function linspace(lo, hi, n) {
    const step = (hi - lo) / (n - 1);
    return Array.from({ length: n }, (_, i) => lo + i * step);
  }

  function argmin(arr) { return arr.indexOf(Math.min(...arr)); }
  function argmax(arr) { return arr.indexOf(Math.max(...arr)); }

  // Simple matrix multiply (row-major arrays of arrays)
  function matMul(A, B) {
    const m = A.length, n = B[0].length, k = B.length;
    return Array.from({ length: m }, (_, i) =>
      Array.from({ length: n }, (_, j) =>
        Array.from({ length: k }, (_, l) => A[i][l] * B[l][j]).reduce((a, b) => a + b, 0)
      )
    );
  }

  /* ─── DATASET GENERATORS ────────────────────────────────── */

  // 2D blobs
  function genBlobs(n = 100, k = 3, spread = 0.5) {
    const centres = Array.from({ length: k }, () => [rnd(-2, 2), rnd(-2, 2)]);
    const pts = [];
    for (let i = 0; i < n; i++) {
      const c = centres[i % k];
      pts.push({ x: gaussianSample(c[0], spread), y: gaussianSample(c[1], spread), label: i % k });
    }
    return pts;
  }

  // Two moons
  function genMoons(n = 100, noise = 0.1) {
    const pts = [];
    for (let i = 0; i < n; i++) {
      const half = Math.floor(n / 2);
      const t = Math.PI * (i / half);
      if (i < half) {
        pts.push({ x: Math.cos(t) + gaussianSample(0, noise), y: Math.sin(t) + gaussianSample(0, noise), label: 0 });
      } else {
        const t2 = Math.PI * ((i - half) / half);
        pts.push({ x: 1 - Math.cos(t2) + gaussianSample(0, noise), y: 0.5 - Math.sin(t2) + gaussianSample(0, noise), label: 1 });
      }
    }
    return pts;
  }

  // Circles
  function genCircles(n = 100, noise = 0.05) {
    const pts = [];
    for (let i = 0; i < n; i++) {
      const r = (i < n / 2) ? 0.5 : 1.0;
      const t = 2 * Math.PI * Math.random();
      pts.push({ x: r * Math.cos(t) + gaussianSample(0, noise), y: r * Math.sin(t) + gaussianSample(0, noise), label: i < n / 2 ? 0 : 1 });
    }
    return pts;
  }

  // Linear regression data
  function genLinear(n = 60, slope = 1.2, intercept = 0.5, noise = 0.4) {
    return Array.from({ length: n }, () => {
      const x = rnd(-3, 3);
      const y = slope * x + intercept + gaussianSample(0, noise);
      return { x, y };
    });
  }

  // Sine wave regression data
  function genSine(n = 80, noise = 0.3) {
    return Array.from({ length: n }, (_, i) => {
      const x = map(i, 0, n - 1, -3, 3);
      const y = Math.sin(x * 1.5) + gaussianSample(0, noise);
      return { x, y };
    });
  }

  // XOR dataset
  function genXOR(n = 100, noise = 0.1) {
    const pts = [];
    for (let i = 0; i < n; i++) {
      const x = rnd(-1, 1);
      const y = rnd(-1, 1);
      const label = ((x > 0) !== (y > 0)) ? 1 : 0;
      pts.push({ x: x + gaussianSample(0, noise), y: y + gaussianSample(0, noise), label });
    }
    return pts;
  }

  // Spiral dataset
  function genSpiral(n = 100, noise = 0.1) {
    const pts = [];
    for (let c = 0; c < 2; c++) {
      for (let i = 0; i < n / 2; i++) {
        const t = (i / (n / 2)) * 3 * Math.PI + c * Math.PI;
        const r = t / (3 * Math.PI);
        pts.push({
          x: r * Math.cos(t) + gaussianSample(0, noise),
          y: r * Math.sin(t) + gaussianSample(0, noise),
          label: c
        });
      }
    }
    return pts;
  }

  // Time series (sine + trend + noise)
  function genTimeSeries(n = 100, freq = 0.1, trend = 0.02, noise = 0.3) {
    return Array.from({ length: n }, (_, i) => ({
      t: i,
      y: Math.sin(2 * Math.PI * freq * i) + trend * i + gaussianSample(0, noise)
    }));
  }

  // Train / test split
  function splitData(pts, ratio = 0.8) {
    const shuffled = [...pts].sort(() => Math.random() - 0.5);
    const cut = Math.floor(shuffled.length * ratio);
    return { train: shuffled.slice(0, cut), test: shuffled.slice(cut) };
  }

  /* ─── LINEAR REGRESSION ─────────────────────────────────── */
  function fitLinear(pts) {
    const n = pts.length;
    if (!n) return { m: 0, b: 0 };
    let sx = 0, sy = 0, sxy = 0, sx2 = 0;
    for (const p of pts) { sx += p.x; sy += p.y; sxy += p.x * p.y; sx2 += p.x * p.x; }
    const denom = n * sx2 - sx * sx;
    if (Math.abs(denom) < 1e-10) return { m: 0, b: sy / n };
    const m = (n * sxy - sx * sy) / denom;
    const b = (sy - m * sx) / n;
    return { m, b };
  }

  function r2Score(pts, m, b) {
    const ys = pts.map(p => p.y);
    const yMean = mean(ys);
    const ssTot = ys.reduce((s, y) => s + (y - yMean) ** 2, 0);
    const ssRes = pts.reduce((s, p) => s + (p.y - (m * p.x + b)) ** 2, 0);
    return 1 - ssRes / ssTot;
  }

  function mse(pts, m, b) {
    return mean(pts.map(p => (p.y - (m * p.x + b)) ** 2));
  }

  /* ─── K-MEANS ───────────────────────────────────────────── */
  function kMeansInit(pts, k) {
    const shuffled = [...pts].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, k).map(p => ({ x: p.x, y: p.y }));
  }

  function kMeansStep(pts, centroids) {
    const k = centroids.length;
    // Assign
    const assignments = pts.map(p => {
      const dists = centroids.map(c => (p.x - c.x) ** 2 + (p.y - c.y) ** 2);
      return argmin(dists);
    });
    // Update
    const newCentroids = Array.from({ length: k }, (_, ci) => {
      const members = pts.filter((_, i) => assignments[i] === ci);
      if (!members.length) return { ...centroids[ci] };
      return { x: mean(members.map(p => p.x)), y: mean(members.map(p => p.y)) };
    });
    return { assignments, centroids: newCentroids };
  }

  function kMeansInertia(pts, assignments, centroids) {
    return pts.reduce((s, p, i) => {
      const c = centroids[assignments[i]];
      return s + (p.x - c.x) ** 2 + (p.y - c.y) ** 2;
    }, 0);
  }

  /* ─── K-NEAREST NEIGHBOURS ──────────────────────────────── */
  function knnPredict(train, query, k, labels) {
    const dists = train.map((p, i) => ({
      d: (p.x - query.x) ** 2 + (p.y - query.y) ** 2,
      label: labels[i], idx: i
    }));
    dists.sort((a, b) => a.d - b.d);
    const neighbours = dists.slice(0, k);
    const votes = {};
    for (const n of neighbours) votes[n.label] = (votes[n.label] || 0) + 1;
    return { prediction: +Object.entries(votes).sort((a,b) => b[1]-a[1])[0][0], neighbours };
  }

  /* ─── CANVAS UTILITIES ──────────────────────────────────── */
  const PALETTE = [
    '#6366f1', '#2dd4bf', '#f472b6', '#fbbf24', '#34d399',
    '#60a5fa', '#a78bfa', '#fb923c', '#4ade80', '#f87171'
  ];

  // Theme-aware canvas colors
  function isDark() {
    return document.documentElement.getAttribute('data-theme') === 'dark';
  }

  function canvasTextColor(alpha = 1) {
    return isDark() ? `rgba(255,255,255,${alpha})` : `rgba(30,30,60,${alpha})`;
  }

  function canvasLineColor(alpha = 0.15) {
    return isDark() ? `rgba(255,255,255,${alpha})` : `rgba(0,0,0,${alpha})`;
  }

  function canvasBg() {
    return isDark() ? '#161B22' : '#FFFFFF';
  }

  function canvasDPR(canvas) {
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width  = rect.width  * dpr;
    canvas.height = rect.height * dpr;
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);
    return ctx;
  }

  function drawAxes(ctx, W, H, pad = 40, xLabel = 'x', yLabel = 'y') {
    ctx.strokeStyle = canvasLineColor(0.2);
    ctx.lineWidth   = 1;
    ctx.beginPath();
    ctx.moveTo(pad, H - pad); ctx.lineTo(W - pad, H - pad);  // x axis
    ctx.moveTo(pad, pad);     ctx.lineTo(pad, H - pad);       // y axis
    ctx.stroke();

    // Tick marks
    ctx.fillStyle = canvasTextColor(0.4);
    ctx.font = `10px 'JetBrains Mono', monospace`;
    ctx.textAlign = 'center';
    for (let i = 0; i <= 4; i++) {
      const x = pad + (i / 4) * (W - 2 * pad);
      ctx.fillText(((i / 4) * 4 - 2).toFixed(1), x, H - pad + 14);
    }
    ctx.textAlign = 'right';
    for (let i = 0; i <= 4; i++) {
      const y = pad + (i / 4) * (H - 2 * pad);
      ctx.fillText((2 - (i / 4) * 4).toFixed(1), pad - 6, y + 3);
    }

    // Labels
    ctx.fillStyle = canvasTextColor(0.6);
    ctx.font = `11px 'Inter', sans-serif`;
    ctx.textAlign = 'center';
    ctx.fillText(xLabel, W / 2, H - 4);
    ctx.save(); ctx.translate(10, H / 2); ctx.rotate(-Math.PI / 2);
    ctx.fillText(yLabel, 0, 0); ctx.restore();
  }

  // Map data coords to canvas pixels
  function dataToCanvas(px, py, W, H, pad, xMin, xMax, yMin, yMax) {
    const cx = map(px, xMin, xMax, pad, W - pad);
    const cy = map(py, yMax, yMin, pad, H - pad);
    return { cx, cy };
  }

  function drawPoint(ctx, cx, cy, r, color, shape = 'circle', alpha = 1) {
    ctx.save();
    ctx.globalAlpha = alpha;
    ctx.fillStyle = color;
    ctx.strokeStyle = canvasLineColor(0.3);
    ctx.lineWidth = 1.2;
    if (shape === 'circle') {
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, 2 * Math.PI);
      ctx.fill();
      ctx.stroke();
    } else if (shape === 'cross') {
      ctx.beginPath();
      ctx.moveTo(cx - r, cy - r); ctx.lineTo(cx + r, cy + r);
      ctx.moveTo(cx + r, cy - r); ctx.lineTo(cx - r, cy + r);
      ctx.strokeStyle = color; ctx.lineWidth = 2;
      ctx.stroke();
    } else if (shape === 'diamond') {
      ctx.beginPath();
      ctx.moveTo(cx, cy - r); ctx.lineTo(cx + r, cy);
      ctx.lineTo(cx, cy + r); ctx.lineTo(cx - r, cy);
      ctx.closePath(); ctx.fill(); ctx.stroke();
    }
    ctx.restore();
  }

  function drawGrid(ctx, W, H, pad = 40, gridCount = 5) {
    ctx.strokeStyle = canvasLineColor(0.07);
    ctx.lineWidth = 1;
    for (let i = 0; i <= gridCount; i++) {
      const x = pad + (i / gridCount) * (W - 2 * pad);
      const y = pad + (i / gridCount) * (H - 2 * pad);
      ctx.beginPath(); ctx.moveTo(x, pad); ctx.lineTo(x, H - pad); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(pad, y); ctx.lineTo(W - pad, y); ctx.stroke();
    }
  }

  /* ─── STORAGE HELPERS ───────────────────────────────────── */
  function save(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch {}
  }

  function load(key, def = null) {
    try {
      const v = localStorage.getItem(key);
      return v !== null ? JSON.parse(v) : def;
    } catch { return def; }
  }

  /* ─── DOM HELPERS ───────────────────────────────────────── */
  const $ = sel => document.querySelector(sel);
  const $$ = sel => [...document.querySelectorAll(sel)];

  function el(tag, attrs = {}, children = []) {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'class') e.className = v;
      else if (k === 'html') e.innerHTML = v;
      else if (k === 'text') e.textContent = v;
      else e.setAttribute(k, v);
    }
    for (const c of children) {
      if (typeof c === 'string') e.insertAdjacentHTML('beforeend', c);
      else e.appendChild(c);
    }
    return e;
  }

  function renderMath(container) {
    if (typeof renderMathInElement !== 'undefined') {
      renderMathInElement(container, {
        delimiters: [
          { left: '$$', right: '$$', display: true  },
          { left: '$',  right: '$',  display: false },
        ],
        throwOnError: false
      });
    }
  }

  function formatNum(n, decimals = 4) {
    if (n === null || n === undefined) return '—';
    return (+n).toFixed(decimals);
  }

  function shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function debounce(fn, ms) {
    let t;
    return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
  }

  function throttle(fn, ms) {
    let last = 0;
    return (...args) => {
      const now = Date.now();
      if (now - last < ms) return;
      last = now;
      fn(...args);
    };
  }

  /* ─── COLOUR UTILITIES ──────────────────────────────────── */
  function hsl(h, s, l, a = 1) { return `hsla(${h},${s}%,${l}%,${a})`; }

  function moduleColor(module) {
    const map_ = { F: 'var(--mod-f)', S: 'var(--mod-s)', U: 'var(--mod-u)', D: 'var(--mod-d)', A: 'var(--mod-a)' };
    return map_[module[0].toUpperCase()] || 'var(--accent-indigo)';
  }

  function levelColor(level) {
    if (level === 'beginner')     return 'var(--accent-teal)';
    if (level === 'intermediate') return 'var(--accent-gold)';
    if (level === 'advanced')     return 'var(--accent-rose)';
    return 'var(--accent-indigo)';
  }

  /* ─── TOAST ─────────────────────────────────────────────── */
  function toast(msg, type = 'info') {
    const icons = { info: '◎', success: '✓', error: '✗' };
    const div = document.createElement('div');
    div.className = `toast ${type}`;
    div.innerHTML = `<span>${icons[type] || '◎'}</span><span>${msg}</span>`;
    const container = document.getElementById('toast-container');
    if (container) {
      container.appendChild(div);
      setTimeout(() => div.remove(), 3200);
    }
  }

  /* ─── EXPORTS ───────────────────────────────────────────── */
  return {
    clamp, lerp, map, rnd, rndInt, randn, gaussianSample, euclidean, dot,
    sigmoid, relu, tanh_, softmax, mean, variance, std, linspace, argmin, argmax, matMul,
    genBlobs, genMoons, genCircles, genLinear, genSine, genXOR, genSpiral, genTimeSeries, splitData,
    fitLinear, r2Score, mse,
    kMeansInit, kMeansStep, kMeansInertia,
    knnPredict,
    PALETTE, isDark, canvasTextColor, canvasLineColor, canvasBg,
    canvasDPR, drawAxes, dataToCanvas, drawPoint, drawGrid,
    save, load, $, $$, el, renderMath, formatNum, shuffle, debounce, throttle,
    hsl, moduleColor, levelColor, toast
  };
})();

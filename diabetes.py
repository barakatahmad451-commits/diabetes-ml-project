<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Glyc AI — Diabetes Risk Intelligence</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Mono:wght@300;400;500&family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
:root {
  --bg:#060b0e;--bg-1:#0a1318;--bg-2:#0e1c23;--bg-3:#122028;
  --teal:#0fd4b4;--teal-dim:rgba(15,212,180,0.12);--teal-glow:0 0 60px rgba(15,212,180,0.14);--teal-mid:rgba(15,212,180,0.55);
  --amber:#f5a524;--red:#f04b4b;--green:#2de37a;
  --text:#e8f2f0;--text-mid:#6d9490;--text-dim:#2e4845;
  --border:rgba(15,212,180,0.08);--border-hi:rgba(15,212,180,0.18);
  --font-serif:'Cormorant Garamond',Georgia,serif;--font-body:'Manrope',sans-serif;--font-mono:'DM Mono',monospace;
  --ease:cubic-bezier(0.25,0.46,0.45,0.94);--ease-out:cubic-bezier(0.16,1,0.3,1);
  --r-sm:8px;--r-md:14px;--r-lg:22px;--r-xl:30px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{font-size:16px;scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--font-body);min-height:100vh;overflow-x:hidden;-webkit-font-smoothing:antialiased}
#bgCanvas{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:0.6}
.grain{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:0.028;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");background-size:256px;animation:grainShift 0.4s steps(1) infinite}
@keyframes grainShift{0%{transform:translate(0,0)}20%{transform:translate(-3px,2px)}40%{transform:translate(2px,-3px)}60%{transform:translate(-2px,-2px)}80%{transform:translate(3px,1px)}100%{transform:translate(0,0)}}
.shell{position:relative;z-index:2;max-width:1320px;margin:0 auto;padding:0 40px 60px;display:flex;flex-direction:column;min-height:100vh}
.hero{padding:52px 0 64px;border-bottom:1px solid var(--border);display:flex;flex-direction:column;gap:36px;animation:fadeUp 0.8s var(--ease-out) both}
.hero__top{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px}
.logo{display:flex;align-items:center;gap:10px}
.logo__mark{width:36px;height:36px;display:flex;align-items:center;justify-content:center;color:var(--teal);background:var(--teal-dim);border:1px solid rgba(15,212,180,0.25);border-radius:10px}
.logo__name{font-family:var(--font-serif);font-size:1.5rem;font-weight:700;color:var(--text);letter-spacing:-0.01em}
.logo__name em{font-style:italic;color:var(--teal)}
.hero__meta{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.chip{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;border:1px solid var(--border-hi);border-radius:999px;font-family:var(--font-mono);font-size:0.67rem;letter-spacing:0.12em;color:var(--text-mid);background:rgba(15,212,180,0.04)}
.chip--live{border-color:rgba(45,227,122,0.3);color:var(--green);background:rgba(45,227,122,0.07)}
.chip__dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:dotBlink 1.6s ease-in-out infinite}
@keyframes dotBlink{0%,100%{opacity:1}50%{opacity:0.25}}
.hero__center{max-width:680px;animation:fadeUp 0.9s var(--ease-out) 0.1s both}
.hero__eyebrow{font-family:var(--font-mono);font-size:0.7rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--teal);margin-bottom:14px;display:flex;align-items:center;gap:10px}
.hero__eyebrow::before{content:'';display:inline-block;width:28px;height:1px;background:var(--teal);opacity:0.5}
.hero__title{font-family:var(--font-serif);font-size:clamp(2.8rem,5.5vw,5rem);font-weight:600;line-height:0.95;letter-spacing:-0.025em;color:var(--text);margin-bottom:22px}
.hero__title em{font-style:italic;color:var(--teal)}
.hero__desc{font-size:1rem;color:var(--text-mid);line-height:1.8;font-weight:300;max-width:540px}
.hero__stats{display:flex;align-items:center;gap:0;animation:fadeUp 1s var(--ease-out) 0.2s both}
.hstat{display:flex;flex-direction:column;gap:4px;padding:0 28px}
.hstat:first-child{padding-left:0}
.hstat__val{font-family:var(--font-serif);font-size:2rem;font-weight:600;color:var(--text);line-height:1}
.hstat__key{font-family:var(--font-mono);font-size:0.62rem;letter-spacing:0.14em;color:var(--text-dim);text-transform:uppercase}
.hstat__div{width:1px;height:36px;background:var(--border-hi)}
.main{display:grid;grid-template-columns:1fr 1fr;gap:28px;padding-top:36px;flex:1}
@media(max-width:1040px){.main{grid-template-columns:1fr}.shell{padding-left:24px;padding-right:24px}.hero{padding:40px 0 48px}}
.form-col,.result-col{background:var(--bg-1);border:1px solid var(--border);border-radius:var(--r-xl);padding:32px;position:relative;overflow:hidden;display:flex;flex-direction:column;gap:24px;transition:border-color 0.4s,box-shadow 0.4s}
.form-col::before,.result-col::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--teal-mid),transparent);opacity:0.5}
.form-col{animation:fadeUp 0.8s var(--ease-out) 0.15s both}
.result-col{animation:fadeUp 0.8s var(--ease-out) 0.25s both}
.form-col:hover,.result-col:hover{border-color:rgba(15,212,180,0.18);box-shadow:var(--teal-glow)}
.col-head{display:flex;align-items:center;gap:14px;padding-bottom:20px;border-bottom:1px solid var(--border)}
.col-icon{font-size:1.3rem;width:42px;height:42px;display:flex;align-items:center;justify-content:center;background:var(--teal-dim);border:1px solid rgba(15,212,180,0.2);border-radius:var(--r-sm);color:var(--teal);flex-shrink:0}
.col-title{font-family:var(--font-serif);font-size:1.4rem;font-weight:600;color:var(--text);letter-spacing:-0.01em;line-height:1.2}
.col-sub{font-size:0.78rem;color:var(--text-mid);margin-top:2px;font-weight:300}
.rform{display:flex;flex-direction:column;gap:18px}
.field{display:flex;flex-direction:column;gap:7px;animation:fadeUp 0.5s var(--ease-out) both}
.field:nth-child(1){animation-delay:0.05s}.field:nth-child(2){animation-delay:0.10s}.field:nth-child(3){animation-delay:0.15s}.field:nth-child(4){animation-delay:0.20s}.field:nth-child(5){animation-delay:0.25s}.field:nth-child(6){animation-delay:0.30s}
.field__header{display:flex;justify-content:space-between;align-items:center}
.field__label{font-size:0.78rem;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--text-mid);cursor:pointer}
.field__range{font-family:var(--font-mono);font-size:0.65rem;color:var(--text-dim)}
.field__row{display:flex;align-items:center;gap:12px}
.field__input-wrap{position:relative;flex:0 0 180px}
.field__input{width:100%;background:rgba(15,212,180,0.04);border:1px solid var(--border-hi);border-radius:var(--r-md);padding:11px 52px 11px 14px;color:var(--text);font-family:var(--font-mono);font-size:0.95rem;font-weight:400;transition:border-color 0.3s,background 0.3s,box-shadow 0.3s;appearance:none;-moz-appearance:textfield}
.field__input::-webkit-outer-spin-button,.field__input::-webkit-inner-spin-button{-webkit-appearance:none}
.field__input::placeholder{color:var(--text-dim)}
.field__input:hover{border-color:rgba(15,212,180,0.3);background:rgba(15,212,180,0.06)}
.field__input:focus{outline:none;border-color:var(--teal);background:rgba(15,212,180,0.08);box-shadow:0 0 0 3px rgba(15,212,180,0.1)}
.field__unit{position:absolute;right:12px;top:50%;transform:translateY(-50%);font-family:var(--font-mono);font-size:0.62rem;color:var(--text-dim);pointer-events:none}
.field__bar-wrap{flex:1}
.field__bar{height:3px;background:rgba(255,255,255,0.05);border-radius:99px;overflow:hidden}
.field__bar-fill{height:100%;width:0%;background:var(--teal);border-radius:99px;transition:width 0.4s var(--ease),background 0.3s}
.field__bar-fill.warn{background:var(--amber)}.field__bar-fill.danger{background:var(--red)}
.field__hint{font-size:0.71rem;color:var(--text-dim);font-style:italic}
.submit-btn{margin-top:8px;display:flex;align-items:center;justify-content:center;gap:12px;padding:15px 28px;background:linear-gradient(135deg,rgba(15,212,180,0.15) 0%,rgba(15,212,180,0.08) 100%);border:1px solid var(--teal);border-radius:var(--r-md);color:var(--teal);font-family:var(--font-body);font-size:0.88rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;cursor:pointer;position:relative;overflow:hidden;transition:all 0.25s var(--ease);box-shadow:0 8px 32px rgba(15,212,180,0.1),inset 0 1px 0 rgba(15,212,180,0.15)}
.submit-btn::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(15,212,180,0.12),transparent);transition:left 0.5s var(--ease)}
.submit-btn:hover{background:linear-gradient(135deg,rgba(15,212,180,0.22) 0%,rgba(15,212,180,0.14) 100%);box-shadow:0 12px 48px rgba(15,212,180,0.22),inset 0 1px 0 rgba(15,212,180,0.2);transform:translateY(-2px)}
.submit-btn:hover::before{left:100%}
.submit-btn:active{transform:translateY(0)}
.submit-btn:disabled{opacity:0.5;cursor:not-allowed;transform:none}
.submit-btn__arrow{display:flex;align-items:center;transition:transform 0.3s var(--ease)}
.submit-btn:hover .submit-btn__arrow{transform:translateX(4px)}
.result-idle{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;padding:40px 20px;text-align:center}
.idle-visual{width:110px;height:110px;color:var(--teal);animation:idleSpin 20s linear infinite}
@keyframes idleSpin{to{transform:rotate(360deg)}}
.idle-msg{font-size:0.88rem;color:var(--text-mid);line-height:1.8;font-weight:300;max-width:260px}
.result-loading{flex:1;display:flex;align-items:center;justify-content:center}
.loader{display:flex;flex-direction:column;align-items:center;gap:16px}
.loader__ring{width:52px;height:52px;border:2px solid rgba(15,212,180,0.12);border-top-color:var(--teal);border-radius:50%;animation:spin 0.8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.loader__text{font-family:var(--font-mono);font-size:0.7rem;letter-spacing:0.14em;color:var(--text-mid)}
.result-output{display:flex;flex-direction:column;gap:18px;animation:fadeUp 0.4s var(--ease-out) both}
.verdict{display:flex;justify-content:space-between;align-items:center;padding:20px 22px;border-radius:var(--r-lg);border:1px solid;gap:16px}
.verdict.high{background:rgba(240,75,75,0.08);border-color:rgba(240,75,75,0.3)}
.verdict.low{background:rgba(45,227,122,0.07);border-color:rgba(45,227,122,0.25)}
.verdict__left{display:flex;align-items:center;gap:14px}
.verdict__icon{width:48px;height:48px;display:flex;align-items:center;justify-content:center;border-radius:50%;font-size:1.4rem;flex-shrink:0}
.verdict.high .verdict__icon{background:rgba(240,75,75,0.12)}
.verdict.low .verdict__icon{background:rgba(45,227,122,0.1)}
.verdict__label{font-family:var(--font-mono);font-size:0.62rem;letter-spacing:0.16em;color:var(--text-dim);margin-bottom:4px}
.verdict__title{font-family:var(--font-serif);font-size:1.3rem;font-weight:600;color:var(--text)}
.verdict__right{text-align:right;flex-shrink:0}
.verdict__conf-label{font-family:var(--font-mono);font-size:0.6rem;letter-spacing:0.14em;color:var(--text-dim);margin-bottom:4px}
.verdict__conf-val{font-family:var(--font-serif);font-size:1.9rem;font-weight:600;color:var(--text);line-height:1}
.conf-ring-wrap{position:relative;width:110px;height:110px;margin:0 auto}
.conf-ring{width:110px;height:110px;transform:rotate(-90deg)}
.conf-ring__track{fill:none;stroke:rgba(255,255,255,0.05);stroke-width:6}
.conf-ring__fill{fill:none;stroke-width:6;stroke-linecap:round;stroke-dasharray:314;stroke-dashoffset:314;transition:stroke-dashoffset 1.2s var(--ease-out),stroke 0.5s}
.conf-ring__center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.conf-ring__pct{font-family:var(--font-serif);font-size:1.5rem;font-weight:600;color:var(--text);line-height:1}
.conf-ring__lbl{font-family:var(--font-mono);font-size:0.58rem;letter-spacing:0.14em;color:var(--text-dim)}
.advice-card{padding:16px 18px;background:var(--bg-2);border:1px solid var(--border);border-radius:var(--r-md);border-left:3px solid var(--teal)}
.advice-card__text{font-size:0.85rem;color:var(--text-mid);line-height:1.75;font-weight:300}
.factors{display:flex;flex-direction:column;gap:10px}
.factors__title{font-family:var(--font-mono);font-size:0.65rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--text-dim)}
.factors__list{display:flex;flex-direction:column;gap:7px}
.fbar{display:grid;grid-template-columns:120px 1fr 48px;align-items:center;gap:10px}
.fbar__name{font-size:0.75rem;font-weight:600;color:var(--text-mid);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fbar__track{height:5px;background:rgba(255,255,255,0.05);border-radius:99px;overflow:hidden}
.fbar__fill{height:100%;border-radius:99px;transition:width 0.8s var(--ease-out)}
.fbar__fill.ok{background:var(--teal)}.fbar__fill.warn{background:var(--amber)}.fbar__fill.danger{background:var(--red)}
.fbar__val{font-family:var(--font-mono);font-size:0.68rem;color:var(--text-dim);text-align:right;white-space:nowrap}
.disclaimer{display:flex;align-items:flex-start;gap:8px;padding:12px 14px;background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:var(--r-sm);font-size:0.7rem;color:var(--text-dim);line-height:1.6}
.disclaimer svg{flex-shrink:0;margin-top:1px}
.site-footer{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;padding:28px 0 0;border-top:1px solid var(--border);margin-top:40px;font-family:var(--font-mono);font-size:0.65rem;letter-spacing:0.1em;color:var(--text-dim)}
.footer-dot{opacity:0.4}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--border-hi);border-radius:3px}
:focus-visible{outline:2px solid var(--teal);outline-offset:3px}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:0.01ms !important;transition-duration:0.01ms !important}}
@media(max-width:600px){.hero__title{font-size:2.4rem}.form-col,.result-col{padding:22px 18px}.field__input-wrap{flex:0 0 140px}.fbar{grid-template-columns:90px 1fr 44px}}
  </style>
</head>
<body>

  <canvas id="bgCanvas" aria-hidden="true"></canvas>
  <div class="grain" aria-hidden="true"></div>

  <div class="shell">
    <header class="hero">
      <div class="hero__top">
        <div class="logo">
          <div class="logo__mark">
            <svg width="22" height="22" viewBox="0 0 22 22" fill="none">
              <circle cx="11" cy="11" r="10" stroke="currentColor" stroke-width="1.2"/>
              <path d="M11 5v6l4 2.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
              <circle cx="11" cy="11" r="2" fill="currentColor"/>
            </svg>
          </div>
          <span class="logo__name">Glyc<em>AI</em></span>
        </div>
        <div class="hero__meta">
          <span class="chip chip--live"><span class="chip__dot"></span>LIVE MODEL</span>
          <span class="chip">Random Forest · Pima Dataset</span>
        </div>
      </div>
      <div class="hero__center">
        <p class="hero__eyebrow">Clinical Decision Support</p>
        <h1 class="hero__title">Diabetes<br><em>Risk Intelligence</em></h1>
        <p class="hero__desc">Enter six clinical measurements. Our Random Forest model — trained on the Pima Indian Diabetes dataset — delivers an instant, confidence-weighted risk assessment.</p>
      </div>
      <div class="hero__stats" role="list">
        <div class="hstat" role="listitem"><span class="hstat__val">6</span><span class="hstat__key">Input features</span></div>
        <div class="hstat__div"></div>
        <div class="hstat" role="listitem"><span class="hstat__val">RF</span><span class="hstat__key">Model type</span></div>
        <div class="hstat__div"></div>
        <div class="hstat" role="listitem"><span class="hstat__val">2</span><span class="hstat__key">Output classes</span></div>
      </div>
    </header>

    <main class="main">
      <!-- LEFT: FORM -->
      <section class="form-col" aria-label="Patient data input">
        <div class="col-head">
          <span class="col-icon" aria-hidden="true">⬡</span>
          <div><h2 class="col-title">Patient Metrics</h2><p class="col-sub">All fields required for prediction</p></div>
        </div>
        <form id="riskForm" class="rform" novalidate>

          <div class="field" data-feature="Pregnancies">
            <div class="field__header">
              <label class="field__label" for="Pregnancies">Pregnancies</label>
              <span class="field__range">0 – 12 times</span>
            </div>
            <div class="field__row">
              <div class="field__input-wrap">
                <input class="field__input" type="number" id="Pregnancies" name="Pregnancies" placeholder="0" min="0" max="20" step="1" autocomplete="off"/>
                <span class="field__unit">×</span>
              </div>
              <div class="field__bar-wrap" aria-hidden="true"><div class="field__bar"><div class="field__bar-fill" data-max="12"></div></div></div>
            </div>
            <p class="field__hint">Number of times pregnant</p>
          </div>

          <div class="field" data-feature="Glucose">
            <div class="field__header">
              <label class="field__label" for="Glucose">Glucose</label>
              <span class="field__range">70 – 200 mg/dL</span>
            </div>
            <div class="field__row">
              <div class="field__input-wrap">
                <input class="field__input" type="number" id="Glucose" name="Glucose" placeholder="100" min="0" max="300" step="1" autocomplete="off"/>
                <span class="field__unit">mg/dL</span>
              </div>
              <div class="field__bar-wrap" aria-hidden="true"><div class="field__bar"><div class="field__bar-fill" data-max="300" data-warn="140"></div></div></div>
            </div>
            <p class="field__hint">Fasting plasma glucose concentration</p>
          </div>

          <div class="field" data-feature="BloodPressure">
            <div class="field__header">
              <label class="field__label" for="BloodPressure">Blood Pressure</label>
              <span class="field__range">40 – 120 mmHg</span>
            </div>
            <div class="field__row">
              <div class="field__input-wrap">
                <input class="field__input" type="number" id="BloodPressure" name="BloodPressure" placeholder="70" min="0" max="200" step="1" autocomplete="off"/>
                <span class="field__unit">mmHg</span>
              </div>
              <div class="field__bar-wrap" aria-hidden="true"><div class="field__bar"><div class="field__bar-fill" data-max="200" data-warn="90"></div></div></div>
            </div>
            <p class="field__hint">Diastolic blood pressure</p>
          </div>

          <div class="field" data-feature="BMI">
            <div class="field__header">
              <label class="field__label" for="BMI">BMI</label>
              <span class="field__range">15 – 45 kg/m²</span>
            </div>
            <div class="field__row">
              <div class="field__input-wrap">
                <input class="field__input" type="number" id="BMI" name="BMI" placeholder="25.0" min="0" max="70" step="0.1" autocomplete="off"/>
                <span class="field__unit">kg/m²</span>
              </div>
              <div class="field__bar-wrap" aria-hidden="true"><div class="field__bar"><div class="field__bar-fill" data-max="70" data-warn="30"></div></div></div>
            </div>
            <p class="field__hint">Body mass index</p>
          </div>

          <div class="field" data-feature="Age">
            <div class="field__header">
              <label class="field__label" for="Age">Age</label>
              <span class="field__range">15 – 90 years</span>
            </div>
            <div class="field__row">
              <div class="field__input-wrap">
                <input class="field__input" type="number" id="Age" name="Age" placeholder="33" min="0" max="120" step="1" autocomplete="off"/>
                <span class="field__unit">yrs</span>
              </div>
              <div class="field__bar-wrap" aria-hidden="true"><div class="field__bar"><div class="field__bar-fill" data-max="120" data-warn="50"></div></div></div>
            </div>
            <p class="field__hint">Patient age in years</p>
          </div>

          <div class="field" data-feature="DiabetesPedigreeFunction">
            <div class="field__header">
              <label class="field__label" for="DiabetesPedigreeFunction">Diabetes Pedigree</label>
              <span class="field__range">0.0 – 1.0</span>
            </div>
            <div class="field__row">
              <div class="field__input-wrap">
                <input class="field__input" type="number" id="DiabetesPedigreeFunction" name="DiabetesPedigreeFunction" placeholder="0.47" min="0" max="3" step="0.01" autocomplete="off"/>
                <span class="field__unit">score</span>
              </div>
              <div class="field__bar-wrap" aria-hidden="true"><div class="field__bar"><div class="field__bar-fill" data-max="2.5" data-warn="0.5"></div></div></div>
            </div>
            <p class="field__hint">Family history risk function</p>
          </div>

          <button type="submit" class="submit-btn" id="submitBtn">
            <span class="submit-btn__label">Run Risk Analysis</span>
            <span class="submit-btn__arrow" aria-hidden="true">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </span>
          </button>
        </form>
      </section>

      <!-- RIGHT: RESULT -->
      <section class="result-col" aria-label="Risk prediction output" aria-live="polite">
        <div class="col-head">
          <span class="col-icon" aria-hidden="true">◈</span>
          <div><h2 class="col-title">Risk Output</h2><p class="col-sub">ML inference result</p></div>
        </div>

        <div class="result-idle" id="resultIdle">
          <div class="idle-visual" aria-hidden="true">
            <svg viewBox="0 0 120 120" fill="none">
              <circle cx="60" cy="60" r="54" stroke="currentColor" stroke-width="1" stroke-dasharray="6 4" opacity="0.2"/>
              <circle cx="60" cy="60" r="38" stroke="currentColor" stroke-width="1" stroke-dasharray="3 6" opacity="0.15"/>
              <circle cx="60" cy="60" r="20" stroke="currentColor" stroke-width="1.5" opacity="0.12"/>
              <circle cx="60" cy="60" r="6" fill="currentColor" opacity="0.2"/>
            </svg>
          </div>
          <p class="idle-msg">Fill in patient metrics and run the analysis to receive your AI-powered risk assessment.</p>
        </div>

        <div class="result-loading" id="resultLoading" hidden>
          <div class="loader" aria-label="Analysing…">
            <div class="loader__ring"></div>
            <span class="loader__text">Running model inference…</span>
          </div>
        </div>

        <div class="result-output" id="resultOutput" hidden>
          <div class="verdict" id="verdictCard">
            <div class="verdict__left">
              <div class="verdict__icon" id="verdictIcon" aria-hidden="true"></div>
              <div>
                <p class="verdict__label">ASSESSMENT</p>
                <p class="verdict__title" id="verdictTitle"></p>
              </div>
            </div>
            <div class="verdict__right">
              <p class="verdict__conf-label">CONFIDENCE</p>
              <p class="verdict__conf-val" id="verdictConf"></p>
            </div>
          </div>

          <div class="conf-ring-wrap" aria-hidden="true">
            <svg class="conf-ring" viewBox="0 0 120 120" id="confRingSvg">
              <circle class="conf-ring__track" cx="60" cy="60" r="50"/>
              <circle class="conf-ring__fill" cx="60" cy="60" r="50" id="confRingFill"/>
            </svg>
            <div class="conf-ring__center">
              <span class="conf-ring__pct" id="confRingPct"></span>
              <span class="conf-ring__lbl">CONF.</span>
            </div>
          </div>

          <div class="advice-card" id="adviceCard">
            <p class="advice-card__text" id="adviceText"></p>
          </div>

          <div class="factors" id="factorBars">
            <p class="factors__title">Input profile</p>
            <div class="factors__list" id="factorsList"></div>
          </div>

          <div class="disclaimer" role="note">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            <span>For informational purposes only. Not a medical diagnosis. Always consult a qualified healthcare professional.</span>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <span>GlycAI · Random Forest Classifier · Pima Indian Diabetes Dataset</span>
      <span class="footer-dot" aria-hidden="true">·</span>
      <span>Built for clinical decision support research</span>
    </footer>
  </div>

  <script>
'use strict';
(function initBgCanvas(){
  const canvas=document.getElementById('bgCanvas');
  if(!canvas)return;
  const ctx=canvas.getContext('2d');
  let W,H,particles=[];
  const TEAL='15,212,180',N=55;
  class Particle{
    constructor(){this.reset(true)}
    reset(init=false){this.x=Math.random()*W;this.y=init?Math.random()*H:H+20;this.vy=-(0.2+Math.random()*0.5);this.vx=(Math.random()-0.5)*0.3;this.r=1+Math.random()*2;this.a=0.08+Math.random()*0.18}
    update(){this.x+=this.vx;this.y+=this.vy;if(this.y<-10)this.reset()}
    draw(){ctx.beginPath();ctx.arc(this.x,this.y,this.r,0,Math.PI*2);ctx.fillStyle=`rgba(${TEAL},${this.a})`;ctx.fill()}
  }
  function resize(){W=canvas.width=window.innerWidth;H=canvas.height=window.innerHeight}
  function draw(){
    ctx.clearRect(0,0,W,H);
    for(let i=0;i<particles.length;i++)for(let j=i+1;j<particles.length;j++){
      const dx=particles[i].x-particles[j].x,dy=particles[i].y-particles[j].y,d=Math.sqrt(dx*dx+dy*dy);
      if(d<120){ctx.beginPath();ctx.moveTo(particles[i].x,particles[i].y);ctx.lineTo(particles[j].x,particles[j].y);ctx.strokeStyle=`rgba(${TEAL},${(1-d/120)*0.06})`;ctx.lineWidth=1;ctx.stroke()}
    }
    particles.forEach(p=>{p.update();p.draw()});
    requestAnimationFrame(draw);
  }
  resize();particles=Array.from({length:N},()=>new Particle());draw();
  window.addEventListener('resize',resize);
})();

function updateBar(input){
  const field=input.closest('.field');if(!field)return;
  const fill=field.querySelector('.field__bar-fill');if(!fill)return;
  const val=parseFloat(input.value)||0,max=parseFloat(fill.dataset.max)||100,warn=parseFloat(fill.dataset.warn)||Infinity;
  fill.style.width=Math.min((val/max)*100,100)+'%';
  fill.classList.remove('warn','danger');
  if(val>warn*1.3)fill.classList.add('danger');else if(val>warn)fill.classList.add('warn');
}
document.querySelectorAll('.field__input').forEach(i=>i.addEventListener('input',()=>updateBar(i)));

const form=document.getElementById('riskForm'),submitBtn=document.getElementById('submitBtn');
const idle=document.getElementById('resultIdle'),loading=document.getElementById('resultLoading'),output=document.getElementById('resultOutput');
function showState(s){idle.hidden=s!=='idle';loading.hidden=s!=='loading';output.hidden=s!=='output'}

form.addEventListener('submit',async(e)=>{
  e.preventDefault();
  const glucose=parseFloat(document.getElementById('Glucose').value),bmi=parseFloat(document.getElementById('BMI').value);
  if(isNaN(glucose)||isNaN(bmi)){['Glucose','BMI'].forEach(id=>{const el=document.getElementById(id);if(!el||el.value)return;el.style.borderColor='#f04b4b';el.style.boxShadow='0 0 0 3px rgba(240,75,75,0.15)';setTimeout(()=>{el.style.borderColor='';el.style.boxShadow=''},1800)});return}
  showState('loading');submitBtn.disabled=true;
  const payload={};form.querySelectorAll('input[name]').forEach(i=>{payload[i.name]=i.value});
  try{
    const res=await fetch('/predict',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    if(!res.ok)throw new Error(`Server responded ${res.status}`);
    renderResult(await res.json(),payload);
  }catch(err){
    output.innerHTML=`<div class="advice-card" style="border-left-color:#f04b4b"><p class="advice-card__text" style="color:#f04b4b">⚠ ${err.message}<br><span style="color:var(--text-dim);font-size:0.78rem">Make sure Flask is running at /predict</span></p></div>`;
    showState('output');
  }finally{submitBtn.disabled=false}
});

function renderResult(data,inputs){
  const isHigh=data.badge==='high-risk',conf=parseFloat(data.confidence)||0;
  const vc=document.getElementById('verdictCard');vc.className='verdict '+(isHigh?'high':'low');
  document.getElementById('verdictIcon').textContent=isHigh?'⚠':'✓';
  document.getElementById('verdictTitle').textContent=data.prediction||(isHigh?'High Diabetes Risk':'Low Diabetes Risk');
  document.getElementById('verdictConf').textContent=conf.toFixed(1)+'%';
  const fill=document.getElementById('confRingFill'),offset=314-(conf/100)*314;
  fill.style.stroke=isHigh?'#f04b4b':'#2de37a';fill.style.strokeDashoffset=314;
  document.getElementById('confRingPct').textContent=conf.toFixed(0)+'%';
  requestAnimationFrame(()=>requestAnimationFrame(()=>{fill.style.strokeDashoffset=offset}));
  document.getElementById('adviceText').textContent=data.advice||'';
  const FACTORS=[
    {key:'Glucose',label:'Glucose',max:300,warn:140},{key:'BMI',label:'BMI',max:70,warn:30},
    {key:'Age',label:'Age',max:100,warn:50},{key:'DiabetesPedigreeFunction',label:'Pedigree',max:2.5,warn:0.5},
    {key:'BloodPressure',label:'Diastolic BP',max:200,warn:90},{key:'Pregnancies',label:'Pregnancies',max:12,warn:7}
  ];
  const listEl=document.getElementById('factorsList');listEl.innerHTML='';
  const vals=data.values||{};
  FACTORS.forEach(f=>{
    const raw=parseFloat(vals[f.key]??inputs[f.key])||0,pct=Math.min((raw/f.max)*100,100);
    let s='ok';if(raw>f.warn*1.3)s='danger';else if(raw>f.warn)s='warn';
    const row=document.createElement('div');row.className='fbar';
    row.innerHTML=`<span class="fbar__name">${f.label}</span><div class="fbar__track"><div class="fbar__fill ${s}" style="width:0%"></div></div><span class="fbar__val">${raw%1!==0?parseFloat(raw).toFixed(2):raw}</span>`;
    listEl.appendChild(row);
    requestAnimationFrame(()=>requestAnimationFrame(()=>{row.querySelector('.fbar__fill').style.width=pct+'%'}));
  });
  showState('output');
}
  </script>
</body>
</html>

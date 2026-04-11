---
layout: default
title: About
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">

<style>
.pp-page h1, .pp-page h2, .pp-page h3 {
  color: #1a1a1a !important;
  font-family: inherit;
  border: none;
  padding: 0;
  margin: 0;
}
.pp-page a { text-decoration: none !important; }
.pp-page {
  font-family: 'DM Sans', sans-serif;
  color: #1a1a1a;
  padding: 0.5rem 0 4rem;
  font-size: 15px;
  line-height: 1.6;
}
.pp-hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
  margin-bottom: 3rem;
}
.pp-eyebrow {
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #BA7517;
  font-weight: 500;
  margin-bottom: 0.875rem;
}
.pp-hero-name {
  font-family: 'Playfair Display', serif !important;
  font-size: 34px !important;
  font-weight: 400 !important;
  line-height: 1.25 !important;
  color: #1a1a1a !important;
  margin-bottom: 1.25rem !important;
}
.pp-tagline {
  font-size: 14px;
  line-height: 1.8;
  color: #555;
  border-left: 2px solid #BA7517;
  padding-left: 1rem;
  margin: 0 0 1.75rem;
}
.pp-cta { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 0.875rem; }
.pp-btn-primary {
  background: #BA7517; color: #fff !important;
  padding: 9px 20px; border-radius: 7px;
  font-size: 13px; font-weight: 500; display: inline-block;
}
.pp-btn-primary:hover { background: #9a6010; color: #fff !important; }
.pp-btn-secondary {
  background: transparent; color: #1a1a1a !important;
  border: 1px solid #ddd; padding: 9px 20px;
  border-radius: 7px; font-size: 13px; display: inline-block;
}
.pp-btn-secondary:hover { border-color: #999; }
.pp-loc { font-size: 11px; color: #999; margin-top: 0.5rem; }
.pp-photo-wrap { position: relative; border-radius: 12px; overflow: hidden; }
.pp-photo-wrap img {
  width: 100%; display: block; border-radius: 12px;
  object-fit: cover; aspect-ratio: 4/5;
}
.pp-photo-cap {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 1.5rem 1rem 1rem;
  background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 100%);
}
.pp-photo-cap p { margin: 0; font-size: 11px; color: rgba(255,255,255,0.9); letter-spacing: 0.04em; }
.pp-stats {
  display: grid; grid-template-columns: repeat(3, 1fr);
  border: 1px solid #e8e8e8; border-radius: 10px;
  overflow: hidden; margin-bottom: 2.75rem;
}
.pp-stat { padding: 1.25rem; text-align: center; border-right: 1px solid #e8e8e8; }
.pp-stat:last-child { border-right: none; }
.pp-stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 26px; font-weight: 400; color: #BA7517; display: block;
}
.pp-stat-label {
  font-size: 10px; color: #999; letter-spacing: 0.07em;
  text-transform: uppercase; margin-top: 4px; display: block;
}
.pp-label {
  font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase;
  color: #bbb; margin-bottom: 1.1rem; font-weight: 500;
}
.pp-pillars {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 1.25rem; margin-bottom: 2.75rem;
}
.pp-pillar { border: 1px solid #e8e8e8; border-radius: 10px; padding: 1.5rem; }
.pp-pillar-icon {
  width: 34px; height: 34px; border-radius: 7px;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 0.875rem; font-size: 16px;
}
.icon-tech { background: #EBF3FB; }
.icon-run  { background: #FEF0DC; }
.pp-pillar-title {
  font-family: 'Playfair Display', serif !important;
  font-size: 17px !important; font-weight: 500 !important;
  color: #1a1a1a !important; margin: 0 0 0.5rem !important;
}
.pp-pillar-body { font-size: 13px; line-height: 1.75; color: #555; margin: 0 0 0.875rem; }
.pp-tags { display: flex; flex-wrap: wrap; gap: 6px; }
.pp-tag {
  font-size: 11px; padding: 3px 10px; border-radius: 20px;
  background: #f5f5f5; color: #666; border: 1px solid #ebebeb;
}
.pp-posts {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 1rem; margin-bottom: 2.75rem;
}
.pp-post {
  border: 1px solid #e8e8e8; border-radius: 10px;
  padding: 1.25rem; display: block; color: #1a1a1a !important;
}
.pp-post:hover { border-color: #ccc; }
.pp-badge {
  font-size: 10px; letter-spacing: 0.07em; text-transform: uppercase;
  font-weight: 500; padding: 2px 9px; border-radius: 20px;
  display: inline-block; margin-bottom: 0.75rem;
}
.badge-tech { background: #EBF3FB; color: #185FA5; }
.badge-run  { background: #FEF0DC; color: #854F0B; }
.badge-comm { background: #EAF3DE; color: #3B6D11; }
.pp-post-title { font-size: 13px; font-weight: 500; line-height: 1.5; color: #1a1a1a; margin-bottom: 0.4rem; }
.pp-post-date  { font-size: 11px; color: #bbb; }
.pp-connect {
  border-top: 1px solid #e8e8e8; padding-top: 2rem;
  display: flex; justify-content: space-between;
  align-items: center; flex-wrap: wrap; gap: 1.25rem;
}
.pp-connect-text { font-size: 14px; color: #444; margin: 0 0 3px; }
.pp-connect-sub  { font-size: 12px; color: #aaa; }
.pp-connect-links { display: flex; gap: 8px; flex-wrap: wrap; }
.pp-link {
  font-size: 12px; padding: 7px 14px;
  border: 1px solid #e8e8e8; border-radius: 7px; color: #555 !important;
}
.pp-link:hover { border-color: #aaa; color: #1a1a1a !important; }
@media (max-width: 680px) {
  .pp-hero    { grid-template-columns: 1fr; gap: 1.5rem; }
  .pp-hero-name { font-size: 26px !important; }
  .pp-photo-wrap { max-width: 300px; margin: 0 auto; }
  .pp-pillars { grid-template-columns: 1fr; }
  .pp-posts   { grid-template-columns: 1fr; }
  .pp-stats   { grid-template-columns: 1fr; }
  .pp-stat    { border-right: none; border-bottom: 1px solid #e8e8e8; }
  .pp-stat:last-child { border-bottom: none; }
  .pp-connect { flex-direction: column; align-items: flex-start; }
}
</style>

<div class="pp-page">

  <div class="pp-hero">
    <div>
      <div class="pp-eyebrow">AI/ML Architect &middot; Ultra Runner &middot; Researcher</div>
      <h1 class="pp-hero-name">20 years in tech.<br>Every finish line<br>teaches me something new.</h1>
      <p class="pp-tagline">Building production-grade AI systems at LTIMindtree. Running Western Ghats trails on weekends. PhD researcher at IIIT Allahabad.</p>
      <div class="pp-cta">
        <a class="pp-btn-primary" href="/blog/">Read the blog</a>
        <a class="pp-btn-secondary" href="https://www.linkedin.com/in/ppant/">Connect on LinkedIn</a>
      </div>
      <p class="pp-loc">📍 Bengaluru, India &nbsp;&middot;&nbsp; Originally from the lower Himalayas</p>
    </div>
    <div class="pp-photo-wrap">
      <!-- Save your trail running photo as pp_trail_hero.jpg in /data/images/ -->
      <img src="/data/images/pp_trail_hero.jpg" alt="Pradeep Pant running on trail" />
      <div class="pp-photo-cap">
        <p>Vagamon trails. Where I debug my thinking. 🙂</p>
      </div>
    </div>
  </div>

  <div class="pp-stats">
    <div class="pp-stat">
      <span class="pp-stat-num">20+</span>
      <span class="pp-stat-label">Years in software</span>
    </div>
    <div class="pp-stat">
      <span class="pp-stat-num">7+</span>
      <span class="pp-stat-label">Ultras completed</span>
    </div>
    <div class="pp-stat">
      <span class="pp-stat-num">2026</span>
      <span class="pp-stat-label">PhD expected</span>
    </div>
  </div>

  <p class="pp-label">Two things I care about deeply</p>
  <div class="pp-pillars">
    <div class="pp-pillar">
      <div class="pp-pillar-icon icon-tech">💻</div>
      <h2 class="pp-pillar-title">Building AI Systems</h2>
      <p class="pp-pillar-body">Designing scalable, production-grade AI and ML systems. From embedded systems at Xerox to GenAI architectures at LTIMindtree — I build things that work at scale and stand the test of time.</p>
      <div class="pp-tags">
        <span class="pp-tag">Generative AI</span>
        <span class="pp-tag">MLOps</span>
        <span class="pp-tag">LLMs</span>
        <span class="pp-tag">Software Architecture</span>
        <span class="pp-tag">Process Mining</span>
      </div>
    </div>
    <div class="pp-pillar">
      <div class="pp-pillar-icon icon-run">🏃</div>
      <h2 class="pp-pillar-title">Running Mountains</h2>
      <p class="pp-pillar-body">Ultra trail runner across the Western Ghats and Himalayas. Malnad Ultra, Bison Ultra, Ooty Ultra — the trails teach patience, pacing, and perspective that no classroom can.</p>
      <div class="pp-tags">
        <span class="pp-tag">Trail Running</span>
        <span class="pp-tag">50K Ultras</span>
        <span class="pp-tag">Western Ghats</span>
        <span class="pp-tag">Himalayas</span>
        <span class="pp-tag">Community Runs</span>
      </div>
    </div>
  </div>

  <p class="pp-label">Latest from the blog</p>
  <div class="pp-posts">
    <a class="pp-post" href="/tech/software/machine%20learning/ai/software%20engineering/why-dsa-matters-agentic-era/">
      <span class="pp-badge badge-tech">AI · Engineering</span>
      <div class="pp-post-title">Why DSA Matters in the Agentic Era</div>
      <div class="pp-post-date">Apr 2026</div>
    </a>
    <a class="pp-post" href="/fitness/running/run_diary_2025/">
      <span class="pp-badge badge-run">Running</span>
      <div class="pp-post-title">2025 Race Diary — Five Runs, One Journey</div>
      <div class="pp-post-date">Dec 2025</div>
    </a>
    <a class="pp-post" href="/community/running/nag_devta_parikrama_run/">
      <span class="pp-badge badge-comm">Community</span>
      <div class="pp-post-title">Nag Mandir Parikrama Run — A Himalayan Initiative</div>
      <div class="pp-post-date">Sep 2025</div>
    </a>
  </div>

  <div class="pp-connect">
    <div>
      <p class="pp-connect-text">Open to collaborations, mentoring, and good conversations.</p>
      <p class="pp-connect-sub">pp@pradeeppant.com &nbsp;&middot;&nbsp; Bengaluru, India</p>
    </div>
    <div class="pp-connect-links">
      <a class="pp-link" href="https://www.linkedin.com/in/ppant/">LinkedIn</a>
      <a class="pp-link" href="https://github.com/ppant">GitHub</a>
      <a class="pp-link" href="https://www.instagram.com/pradeepkpant/">Instagram</a>
      <a class="pp-link" href="mailto:pp@pradeeppant.com">Email</a>
    </div>
  </div>

</div>

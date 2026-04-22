---
layout: default
title: About
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

.pp-page { font-family: 'DM Sans', sans-serif; max-width: 900px; margin: 0 auto; padding: 0 1.5rem 4rem; color: #1a1a1a; }

/* Hero */
.pp-hero { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; margin: 2rem 0 3rem; }
.pp-eyebrow { font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: #BA7517; font-weight: 500; margin-bottom: 1rem; }
.pp-hero-name { font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 400; line-height: 1.2; margin: 0 0 1.25rem; }
.pp-hero-tagline { font-size: 15px; line-height: 1.8; color: #555; border-left: 2px solid #BA7517; padding-left: 1rem; margin: 0 0 1.75rem; }
.pp-hero-cta { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 1rem; }
.pp-btn-primary { background: #BA7517; color: #fff !important; padding: 10px 22px; border-radius: 8px; font-size: 13px; font-weight: 500; text-decoration: none !important; display: inline-block; }
.pp-btn-primary:hover { background: #9a6010; }
.pp-btn-secondary { background: transparent; color: #1a1a1a !important; border: 1px solid #ddd; padding: 10px 22px; border-radius: 8px; font-size: 13px; text-decoration: none !important; display: inline-block; }
.pp-btn-secondary:hover { border-color: #aaa; }
.pp-location { font-size: 11px; color: #999; margin-top: 0.75rem; letter-spacing: 0.03em; }

/* Photo */
.pp-photo-wrap { position: relative; border-radius: 12px; overflow: hidden; }
.pp-photo-wrap img { width: 100%; display: block; border-radius: 12px; object-fit: cover; aspect-ratio: 3/4; }
.pp-photo-caption { position: absolute; bottom: 0; left: 0; right: 0; padding: 1.25rem 1rem 1rem; background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 100%); }
.pp-photo-caption p { margin: 0; font-size: 11px; color: rgba(255,255,255,0.85); letter-spacing: 0.05em; }

/* Avatar fallback if only headshot available */
.pp-avatar { width: 72px; height: 72px; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.15); object-fit: cover; }

/* Stats */
.pp-stats { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid #e8e8e8; border-radius: 12px; overflow: hidden; margin-bottom: 3rem; }
.pp-stat { padding: 1.25rem; text-align: center; border-right: 1px solid #e8e8e8; }
.pp-stat:last-child { border-right: none; }
.pp-stat-num { font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 400; color: #BA7517; display: block; }
.pp-stat-label { font-size: 11px; color: #888; letter-spacing: 0.06em; text-transform: uppercase; margin-top: 4px; display: block; }

/* Pillars */
.pp-section-label { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: #aaa; margin-bottom: 1.25rem; font-weight: 500; }
.pp-pillars { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 3rem; }
.pp-pillar { border: 1px solid #e8e8e8; border-radius: 12px; padding: 1.5rem; }
.pp-pillar-icon { width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem; font-size: 18px; }
.pp-pillar-icon-tech { background: #E6F1FB; }
.pp-pillar-icon-run { background: #FAEEDA; }
.pp-pillar-title { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: 500; margin: 0 0 0.5rem; }
.pp-pillar-body { font-size: 13px; line-height: 1.7; color: #555; margin: 0 0 1rem; }
.pp-tags { display: flex; flex-wrap: wrap; gap: 6px; }
.pp-tag { font-size: 11px; padding: 3px 10px; border-radius: 20px; background: #f5f5f5; color: #666; border: 1px solid #e8e8e8; }

/* Posts */
.pp-posts { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 3rem; }
.pp-post { border: 1px solid #e8e8e8; border-radius: 12px; padding: 1.25rem; text-decoration: none !important; display: block; }
.pp-post:hover { border-color: #ccc; }
.pp-badge { font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 500; padding: 2px 8px; border-radius: 20px; display: inline-block; margin-bottom: 0.75rem; }
.pp-badge-tech { background: #E6F1FB; color: #185FA5; }
.pp-badge-run { background: #FAEEDA; color: #854F0B; }
.pp-post-title { font-size: 13px; font-weight: 500; line-height: 1.5; color: #1a1a1a; margin-bottom: 0.5rem; }
.pp-post-date { font-size: 11px; color: #aaa; }

/* Connect */
.pp-connect { border-top: 1px solid #e8e8e8; padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem; }
.pp-connect-left p { font-size: 14px; color: #555; margin: 0 0 0.25rem; }
.pp-connect-left small { font-size: 12px; color: #aaa; }
.pp-connect-links { display: flex; gap: 10px; flex-wrap: wrap; }
.pp-connect-link { font-size: 12px; padding: 7px 14px; border: 1px solid #e8e8e8; border-radius: 8px; color: #555 !important; text-decoration: none !important; }
.pp-connect-link:hover { border-color: #aaa; color: #1a1a1a !important; }

/* Responsive */
@media (max-width: 640px) {
  .pp-hero { grid-template-columns: 1fr; gap: 2rem; }
  .pp-hero-name { font-size: 28px; }
  .pp-photo-wrap { max-width: 320px; margin: 0 auto; }
  .pp-pillars { grid-template-columns: 1fr; }
  .pp-posts { grid-template-columns: 1fr; }
  .pp-stats { grid-template-columns: 1fr; }
  .pp-stat { border-right: none; border-bottom: 1px solid #e8e8e8; }
  .pp-stat:last-child { border-bottom: none; }
  .pp-connect { flex-direction: column; align-items: flex-start; }
}
</style>

<div class="pp-page">

  <!-- HERO -->
  <div class="pp-hero">
    <div class="pp-hero-text">
      <div class="pp-eyebrow">AI/ML Architect · Ultra Runner · Researcher</div>
      <h1 class="pp-hero-name">20 years in tech.<br>Every finish line<br>teaches me something new.</h1>
      <p class="pp-hero-tagline">Building production-grade AI systems at LTIMindtree. Running trails on weekends. PhD researcher at IIIT Allahabad.</p>
      <div class="pp-hero-cta">
        <a class="pp-btn-primary" href="/blog/">Read the blog</a>
        <a class="pp-btn-secondary" href="https://www.linkedin.com/in/ppant/">Connect on LinkedIn</a>
      </div>
      <p class="pp-location">📍 Bengaluru, India &nbsp;·&nbsp; Originally from the lower Himalayas</p>
    </div>
    <div class="pp-photo-wrap">
      <!-- Replace with your trail running photo. Landscape photo works too — remove aspect-ratio style if needed -->
      <img src="/data/images/pp_trail_running.jpg" alt="Pradeep Pant on trail" />
      <div class="pp-photo-caption">
        <p>Sahyadri trails. Where I debug my thinking. 🙂</p>
      </div>
    </div>
  </div>

  <!-- STATS -->
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

  <!-- PILLARS -->
  <div class="pp-section-label">Two things I care about deeply</div>
  <div class="pp-pillars">
    <div class="pp-pillar">
      <div class="pp-pillar-icon pp-pillar-icon-tech">💻</div>
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
      <div class="pp-pillar-icon pp-pillar-icon-run">🏃</div>
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

  <!-- LATEST POSTS -->
  <div class="pp-section-label">Latest from the blog</div>
  <div class="pp-posts">
    <a class="pp-post" href="/2026/04/04/why-dsa-matters-agentic-era/">
      <span class="pp-badge pp-badge-tech">AI · Engineering</span>
      <div class="pp-post-title">Why DSA Matters in the Agentic Era</div>
      <div class="pp-post-date">Apr 2026</div>
    </a>
    <a class="pp-post" href="/2025/12/20/run_diary_2025/">
      <span class="pp-badge pp-badge-run">Running</span>
      <div class="pp-post-title">2025 Race Diary — Five Runs, One Journey</div>
      <div class="pp-post-date">Dec 2025</div>
    </a>
    <a class="pp-post" href="/2025/09/10/nag_devta_parikrama_run/">
      <span class="pp-badge pp-badge-run">Community</span>
      <div class="pp-post-title">Nag Mandir Parikrama Run — A Himalayan Initiative</div>
      <div class="pp-post-date">Sep 2025</div>
    </a>
  </div>

  <!-- CONNECT -->
  <div class="pp-connect">
    <div class="pp-connect-left">
      <p>Open to collaborations, mentoring, and good conversations.</p>
      <small>pp@pradeeppant.com &nbsp;·&nbsp; Bengaluru, India</small>
    </div>
    <div class="pp-connect-links">
      <a class="pp-connect-link" href="https://www.linkedin.com/in/ppant/">LinkedIn</a>
      <a class="pp-connect-link" href="https://github.com/ppant">GitHub</a>
      <a class="pp-connect-link" href="https://www.instagram.com/pradeepkpant/">Instagram</a>
      <a class="pp-connect-link" href="mailto:pp@pradeeppant.com">Email</a>
    </div>
  </div>

</div>

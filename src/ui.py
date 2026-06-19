import streamlit as st

_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: #f5f3ef;
        color: #1a1a1a;
    }
    ::selection { background: #c8b56044; }
    [data-testid="stSidebar"] {
        background-color: #e8e6e1;
        border-right: 1px solid #dcd8cf;
    }
    [data-testid="stSidebar"] * { font-family: 'DM Sans', sans-serif !important; }
    #MainMenu, footer { visibility: hidden; }
    header { visibility: hidden; }
    /* Show the sidebar re-open button even when header is hidden */
    [data-testid="collapsedControl"] { visibility: visible !important; }
    /* Hide the close-sidebar button so sidebar can't be accidentally closed */
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #f5f3ef; }
    ::-webkit-scrollbar-thumb { background: #d9d4c8; border-radius: 6px; border: 3px solid #f5f3ef; }

    .page-eyebrow {
        font-family: 'DM Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #a39a86;
        margin-bottom: 0;
    }
    .page-title {
        font-family: 'Instrument Serif', serif;
        font-size: 2.8rem;
        font-weight: 400;
        color: #1a1a1a;
        letter-spacing: -0.01em;
        line-height: 1.04;
        margin: 8px 0 0;
    }
    .page-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        color: #5a564e;
        line-height: 1.5;
        margin: 10px 0 2rem;
        max-width: 560px;
    }
    .section-label {
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #a39a86;
        margin-bottom: 0.6rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #e4e0d8;
    }
    .card {
        background: #fff;
        border: 1px solid #e4e0d8;
        border-radius: 14px;
        padding: 22px 24px;
        margin-bottom: 14px;
    }
    .card-accent-green { border-left: 3px solid #1D9E75; }
    .card-accent-red { border-left: 3px solid #e07070; }

    .match-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 9px 0;
        border-bottom: 1px solid #f0ede6;
        font-size: 0.88rem;
    }
    .match-row:last-child { border-bottom: none; }
    .match-skill { color: #1a1a1a; font-weight: 500; }
    .match-cv { color: #8a8474; font-size: 0.75rem; font-family: 'DM Mono', monospace; }
    .gap-skill { color: #b05050; font-weight: 400; }
    .match-badge {
        font-family: 'DM Mono', monospace;
        font-size: 0.62rem;
        background: #e6f5ee;
        color: #1D9E75;
        padding: 2px 8px;
        border-radius: 999px;
        flex-shrink: 0;
        border: 1px solid #cfe9dd;
    }
    .ner-container {
        background: #fff;
        border: 1px solid #e4e0d8;
        border-radius: 14px;
        padding: 22px 24px;
        line-height: 2.4;
        font-size: 0.88rem;
        color: #3a372f;
    }
    .stButton > button {
        background: #c8b560 !important;
        color: #332b0e !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 11px !important;
        height: 48px !important;
        width: 100% !important;
        transition: opacity 0.2s ease !important;
    }
    .stButton > button:hover { opacity: 0.88 !important; transform: none !important; box-shadow: none !important; }
    [data-testid="stFileUploaderDropzone"] {
        background: #faf8f2 !important;
        border: 1.5px dashed #cfc9ba !important;
        border-radius: 12px !important;
    }
    textarea {
        background: #fff !important;
        border: 1px solid #e4e0d8 !important;
        border-radius: 10px !important;
        color: #1a1a1a !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.88rem !important;
    }
    textarea:focus { border-color: #c8b560 !important; box-shadow: none !important; }
    hr { border: none; border-top: 1px solid #dcd8cf; margin: 20px 0; }
    [data-testid="stSpinner"] { color: #c8b560 !important; }
    .metric-tag {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        color: #7a7466;
        background: #f1eee7;
        border: 1px solid #e6e1d6;
        padding: 4px 10px;
        border-radius: 6px;
        margin-right: 7px;
        margin-bottom: 6px;
    }
    .badge-green {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.6rem;
        background: #e6f5ee;
        color: #137a59;
        border: 1px solid #cfe9dd;
        padding: 3px 10px;
        border-radius: 999px;
        letter-spacing: 0.5px;
    }
    .badge-amber {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.6rem;
        background: #faf6ea;
        color: #97812a;
        border: 1px solid #ece0c0;
        padding: 3px 10px;
        border-radius: 999px;
        letter-spacing: 0.5px;
    }
    [data-testid="stProgressBar"] > div { background: #f0ede6 !important; border-radius: 999px !important; }
    [data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, #c8b560, #bda849) !important; border-radius: 999px !important; }
    .stAlert { border-radius: 10px !important; }
</style>
"""


def inject_css() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def render_sidebar(tfidf_available: bool) -> str:
    with st.sidebar:
        badge = (
            '<span class="badge-green">TF-IDF loaded</span>'
            if tfidf_available
            else '<span class="badge-amber">Run notebook to export TF-IDF</span>'
        )
        st.markdown(f"""
        <div style="padding:24px 10px 16px;">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:20px;">
                <div style="width:34px; height:34px; border-radius:9px; background:#c8b560; display:flex; align-items:center; justify-content:center; font-family:'DM Mono',monospace; font-weight:500; font-size:12px; color:#332b0e; flex:none;">CV</div>
                <div>
                    <div style="font-family:'Instrument Serif',serif; font-size:18px; line-height:1; color:#1a1a1a;">Smart CV</div>
                    <div style="font-family:'DM Mono',monospace; font-size:9px; letter-spacing:0.14em; color:#9a9488; margin-top:3px;">ANALYZER</div>
                </div>
            </div>
            <div style="margin-bottom:16px;">{badge}</div>
        </div>
        <div style="border-top:1px solid #dcd8cf; margin:0 0 8px;"></div>
        <div style="font-family:'DM Mono',monospace; font-size:10px; letter-spacing:0.16em; color:#a8a294; padding:12px 10px 8px;">MENU</div>
        """, unsafe_allow_html=True)

        page = st.radio(
            "",
            options=["Overview", "Analyzer", "Candidate Ranking", "System Evaluation"],
            label_visibility="collapsed",
        )

        st.markdown("""
        <div style="border-top:1px solid #dcd8cf; margin-top:auto; padding:16px 10px 8px; display:flex; align-items:center; gap:8px;">
            <span style="width:7px; height:7px; border-radius:50%; background:#1D9E75; flex:none;"></span>
            <span style="font-family:'DM Mono',monospace; font-size:10px; color:#9a9488; letter-spacing:0.04em;">spaCy + SBERT · BINUS NLP</span>
        </div>
        <div style="padding:0 10px 20px;">
            <p style="font-family:'DM Mono',monospace; font-size:9px; color:#c8c0ac; letter-spacing:1px; margin:0;">
                COMP6885001 — 2025/2026
            </p>
        </div>
        """, unsafe_allow_html=True)

    return page


def render_analyzer_inputs() -> tuple:
    st.markdown('<p class="page-eyebrow">Analyzer</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-title">Analyze a résumé</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Upload a candidate PDF and paste a job description to score the match.</p>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.4], gap="large")
    with col_left:
        st.markdown('<div class="section-label">Résumé — PDF</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Drop PDF here", type=["pdf"], label_visibility="collapsed")
    with col_right:
        st.markdown('<div class="section-label">Job Requirements</div>', unsafe_allow_html=True)
        jd_text = st.text_area(
            "Paste the job description or qualifications",
            height=140,
            placeholder="e.g. Required: Python, 3+ years experience in machine learning, proficiency in SQL...",
            label_visibility="collapsed",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    run_clicked = st.button("Analyze résumé")
    return uploaded_file, jd_text, run_clicked


def render_score(score: float, tfidf_score: float | None) -> None:
    label = "Strong fit" if score >= 70 else "Moderate fit" if score >= 45 else "Weak fit"
    pct = min(score, 100)
    r, cx, cy = 54, 70, 70
    circ = 2 * 3.14159 * r
    dash_filled = circ * pct / 100
    dash_empty = circ - dash_filled
    offset = circ * 0.25  # start arc from 12 o'clock

    tfidf_line = ""
    if tfidf_score is not None:
        tfidf_line = f'<p style="font-family:DM Mono,monospace; font-size:0.75rem; color:#a39a86; margin:6px 0 0;">TF-IDF Lexical Score: {tfidf_score:.3f}</p>'

    svg = (f'<svg width="140" height="140" viewBox="0 0 140 140" style="flex:none;overflow:visible;">'
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#ece8dd" stroke-width="10"/>'
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#c8b560" stroke-width="10"'
           f' stroke-dasharray="{dash_filled:.1f} {dash_empty:.1f}" stroke-dashoffset="{offset:.1f}" stroke-linecap="round"/>'
           f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" font-family="Georgia,serif" font-size="38" fill="#1a1a1a">{score:.0f}</text>'
           f'<text x="{cx}" y="{cy + 18}" text-anchor="middle" font-family="monospace" font-size="11" fill="#a39a86">/ 100</text>'
           f'</svg>')
    text_block = (f'<div style="flex:1;">'
                  f'<div style="font-family:DM Mono,monospace;font-size:0.65rem;letter-spacing:0.16em;text-transform:uppercase;color:#a39a86;">Match Score</div>'
                  f'<div style="font-family:Georgia,serif;font-size:1.9rem;line-height:1.1;color:#1a1a1a;margin-top:6px;">{label}</div>'
                  f'{tfidf_line}'
                  f'</div>')
    st.markdown(
        f'<div style="background:#fff;border:1px solid #e4e0d8;border-radius:16px;padding:32px 28px;'
        f'display:flex;align-items:center;gap:28px;margin:24px 0;box-shadow:0 1px 4px rgba(0,0,0,0.05);">'
        f'{svg}{text_block}</div>',
        unsafe_allow_html=True,
    )


def render_match_breakdown(details: list, cv_features: set, jd_features: set) -> None:
    strong = [d for d in details if d["score"] > 0.75]
    moderate = [d for d in details if 0.50 <= d["score"] <= 0.75]
    gaps = [d for d in details if d["score"] < 0.50]

    col_match, col_gap = st.columns(2, gap="large")

    with col_match:
        strong_rows = "".join(
            f'<div class="match-row"><span class="match-skill">{d["jd"]}</span>'
            f'<span class="match-badge">{d["score"]:.0%}</span></div>'
            for d in strong
        ) if strong else '<p style="color:#a39a86; font-size:0.85rem; margin:0;">No strong matches found.</p>'

        st.markdown(f"""
        <div class="card card-accent-green">
            <div class="section-label">Strong Matches — {len(strong)}</div>
            {strong_rows}
        </div>
        """, unsafe_allow_html=True)

        if moderate:
            moderate_rows = "".join(
                f'<div class="match-row">'
                f'<span style="color:#7a6e52; font-size:0.88rem;">{d["jd"]}</span>'
                f'<span style="font-family:\'DM Mono\',monospace; font-size:0.62rem; background:#faf6ea; color:#97812a; border:1px solid #ece0c0; padding:2px 8px; border-radius:999px;">{d["score"]:.0%}</span>'
                f'</div>'
                for d in moderate
            )
            st.markdown(f"""
            <div class="card">
                <div class="section-label">Partial Matches — {len(moderate)}</div>
                {moderate_rows}
            </div>
            """, unsafe_allow_html=True)

    with col_gap:
        gap_rows = "".join(
            f'<div class="match-row"><span class="gap-skill">{d["jd"]}</span>'
            f'<span style="font-family:\'DM Mono\',monospace; font-size:0.62rem; color:#c8c0ac;">not found</span></div>'
            for d in gaps
        ) if gaps else '<p style="color:#1D9E75; font-size:0.85rem; margin:0;">No significant gaps detected.</p>'

        st.markdown(f"""
        <div class="card card-accent-red">
            <div class="section-label">Requirements Gap — {len(gaps)}</div>
            {gap_rows}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card">
            <div class="section-label">Extraction Stats</div>
            <div class="match-row">
                <span style="color:#8a8474; font-size:0.85rem;">CV features (after filter)</span>
                <span style="color:#1a1a1a; font-family:'DM Mono',monospace; font-size:0.8rem;">{len(cv_features)}</span>
            </div>
            <div class="match-row">
                <span style="color:#8a8474; font-size:0.85rem;">JD requirements (after filter)</span>
                <span style="color:#1a1a1a; font-family:'DM Mono',monospace; font-size:0.8rem;">{len(jd_features)}</span>
            </div>
            <div class="match-row">
                <span style="color:#8a8474; font-size:0.85rem;">Requirements evaluated</span>
                <span style="color:#1a1a1a; font-family:'DM Mono',monospace; font-size:0.8rem;">{len(details)}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_ner_section(ner_html: str) -> None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Named Entity Highlighting — Resume</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ner-container">{ner_html}</div>', unsafe_allow_html=True)


def render_methodology() -> None:
    st.markdown('<p class="page-eyebrow">Overview</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-title">Smart CV Analyzer</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">A semantic résumé-to-role matching engine — reads meaning, not keywords, to score fit and surface the skills that matter.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style="background:#fff; border:1px solid #e4e0d8; border-radius:16px; padding:26px; margin-bottom:18px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px;">
                <div style="width:42px; height:42px; border-radius:11px; background:#f6f2e0; display:flex; align-items:center; justify-content:center; color:#b39a3a;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 3 7.5 12 12l9-4.5L12 3Z"/><path d="M3 12.5 12 17l9-4.5"/><path d="M3 17 12 21.5 21 17"/></svg>
                </div>
                <span style="font-family:'Instrument Serif',serif; font-size:28px; color:#e3ddcc;">01</span>
            </div>
            <div style="font-family:'DM Sans',sans-serif; font-weight:600; font-size:17px; color:#1a1a1a;">Architecture</div>
            <div style="font-family:'DM Mono',monospace; font-size:11px; color:#a39a86; margin-top:3px; letter-spacing:0.03em;">spaCy + SBERT pipeline</div>
            <div style="margin-top:14px; display:flex; flex-direction:column; gap:8px;">
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">spaCy NER for entity &amp; skill extraction</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">SBERT sentence embeddings</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Cosine similarity scoring</span></div>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:7px; margin-top:16px;">
                <span class="metric-tag">spaCy</span>
                <span class="metric-tag">SBERT</span>
                <span class="metric-tag">PyTorch</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#fff; border:1px solid #e4e0d8; border-radius:16px; padding:26px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px;">
                <div style="width:42px; height:42px; border-radius:11px; background:#e6f5ee; display:flex; align-items:center; justify-content:center; color:#1D9E75;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.22 4.22l2.12 2.12M17.66 17.66l2.12 2.12M2 12h3M19 12h3M4.22 19.78l2.12-2.12M17.66 6.34l2.12-2.12"/></svg>
                </div>
                <span style="font-family:'Instrument Serif',serif; font-size:28px; color:#e3ddcc;">03</span>
            </div>
            <div style="font-family:'DM Sans',sans-serif; font-weight:600; font-size:17px; color:#1a1a1a;">Scoring Method</div>
            <div style="font-family:'DM Mono',monospace; font-size:11px; color:#a39a86; margin-top:3px; letter-spacing:0.03em;">per-requirement cosine similarity</div>
            <div style="margin-top:14px; display:flex; flex-direction:column; gap:8px;">
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Each JD requirement vs. all CV features</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Match threshold: 65% similarity</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Final score = mean similarity × 100</span></div>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:7px; margin-top:16px;">
                <span class="metric-tag">Cosine Similarity</span>
                <span class="metric-tag">Vector Space</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background:#fff; border:1px solid #e4e0d8; border-radius:16px; padding:26px; margin-bottom:18px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px;">
                <div style="width:42px; height:42px; border-radius:11px; background:#e7f0fb; display:flex; align-items:center; justify-content:center; color:#378ADD;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 5h18l-7 8v6l-4 2v-8L3 5Z"/></svg>
                </div>
                <span style="font-family:'Instrument Serif',serif; font-size:28px; color:#e3ddcc;">02</span>
            </div>
            <div style="font-family:'DM Sans',sans-serif; font-weight:600; font-size:17px; color:#1a1a1a;">Semantic Filtering</div>
            <div style="font-family:'DM Mono',monospace; font-size:11px; color:#a39a86; margin-top:3px; letter-spacing:0.03em;">meaning over keywords</div>
            <div style="margin-top:14px; display:flex; flex-direction:column; gap:8px;">
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Semantic anchor phrases filter noise</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Removes admin terms automatically</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#c8b560; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">No hardcoded blacklists</span></div>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:7px; margin-top:16px;">
                <span class="metric-tag">Embeddings</span>
                <span class="metric-tag">NER</span>
                <span class="metric-tag">Noun Phrases</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#fff; border:1px solid #e4e0d8; border-radius:16px; padding:26px;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px;">
                <div style="width:42px; height:42px; border-radius:11px; background:#f1eee7; display:flex; align-items:center; justify-content:center; color:#97812a;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><polyline points="3,17 9,11 13,14 21,5"/><line x1="3" y1="21" x2="21" y2="21"/></svg>
                </div>
                <span style="font-family:'Instrument Serif',serif; font-size:28px; color:#e3ddcc;">04</span>
            </div>
            <div style="font-family:'DM Sans',sans-serif; font-weight:600; font-size:17px; color:#1a1a1a;">Evaluation Results</div>
            <div style="font-family:'DM Mono',monospace; font-size:11px; color:#a39a86; margin-top:3px; letter-spacing:0.03em;">exceeds F1 ≥ 0.75 target</div>
            <div style="margin-top:14px; display:flex; flex-direction:column; gap:8px;">
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#1D9E75; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Precision 0.9524 · Recall 0.80</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#1D9E75; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;"><strong style="color:#1a1a1a;">F1 = 0.8696</strong> (+11.9pp above target)</span></div>
                <div style="display:flex; gap:10px; align-items:flex-start;"><span style="width:5px; height:5px; border-radius:50%; background:#1D9E75; margin-top:7px; flex:none;"></span><span style="font-size:13.5px; line-height:1.45; color:#5a564e;">Hybrid accuracy: 4/5 test cases</span></div>
            </div>
            <div style="display:flex; flex-wrap:wrap; gap:7px; margin-top:16px;">
                <span class="metric-tag">Sentence Transformers</span>
                <span class="metric-tag">mpnet-base-v2</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_candidate_ranking(nlp, sbert_model, tfidf_vectorizer) -> None:
    import PyPDF2
    from src.extraction.engine import extract_features, calculate_semantic_score
    from src.utils.preprocessor import pdf_clean

    GREEN = "#1D9E75"
    BLUE = "#378ADD"
    GRAY = "#888780"
    _card_base = "background:#fff; border:1px solid #e4e0d8; border-radius:14px; padding:20px 18px; text-align:center;"

    st.markdown('<p class="page-eyebrow">Candidate Ranking</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-title">Compare candidates</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Score multiple résumés against one role and rank them on a single leaderboard.</p>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.4], gap="large")
    with col_left:
        st.markdown('<div class="section-label">Résumés — Multiple PDFs</div>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "Drop PDFs here",
            type=["pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed",
        )
    with col_right:
        st.markdown('<div class="section-label">Job Description</div>', unsafe_allow_html=True)
        jd_text = st.text_area(
            "Paste the job description or qualifications",
            height=140,
            placeholder="e.g. Required: Python, 3+ years experience in machine learning, proficiency in SQL...",
            label_visibility="collapsed",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    col_slider, col_btn = st.columns([2, 1], gap="large")
    with col_slider:
        st.markdown('<div class="section-label">Top-K</div>', unsafe_allow_html=True)
        top_k = st.slider("Top-K Candidates", min_value=3, max_value=20, value=5, label_visibility="collapsed")
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        rank_clicked = st.button("Rank Candidates")

    if not rank_clicked:
        return

    if not jd_text.strip():
        st.error("Job description is empty. Please enter job requirements before ranking.")
        return

    if not uploaded_files or len(uploaded_files) < 2:
        st.warning("Please upload at least 2 PDF resumes to compare and rank.")
        return

    results = []
    with st.spinner("Analyzing candidates..."):
        clean_jd = pdf_clean(jd_text)
        doc_jd = nlp(clean_jd)
        jd_features = extract_features(doc_jd, sbert_model)

        for pdf_file in uploaded_files:
            try:
                reader = PyPDF2.PdfReader(pdf_file)
                raw_text = " ".join(p.extract_text() or "" for p in reader.pages)
                clean_cv = pdf_clean(raw_text)
                doc_cv = nlp(clean_cv)
                cv_features = extract_features(doc_cv, sbert_model)

                if not cv_features:
                    score = 0.0
                else:
                    score, _ = calculate_semantic_score(cv_features, jd_features, sbert_model)

                results.append({
                    "filename": pdf_file.name,
                    "score": score,
                    "cv_features": cv_features,
                })
            except Exception:
                st.warning(f"Could not read \"{pdf_file.name}\" — file skipped.")

    if not results:
        st.error("No resumes could be processed. Please check your PDF files.")
        return

    results.sort(key=lambda x: x["score"], reverse=True)
    top_results = results[:top_k]

    total_uploaded = len(uploaded_files)
    candidates_ranked = len(results)
    top_score = top_results[0]["score"] / 100 if top_results else 0.0
    avg_score = sum(r["score"] for r in results) / len(results) / 100

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Summary</div>', unsafe_allow_html=True)
    mc1, mc2, mc3, mc4 = st.columns(4, gap="small")
    with mc1:
        st.markdown(f"""
        <div style="{_card_base}">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Total Uploaded</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:#1a1a1a; margin:0; line-height:1;">{total_uploaded}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">PDF files</p>
        </div>""", unsafe_allow_html=True)
    with mc2:
        st.markdown(f"""
        <div style="{_card_base}">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Ranked</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:#1a1a1a; margin:0; line-height:1;">{candidates_ranked}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">processed</p>
        </div>""", unsafe_allow_html=True)
    with mc3:
        st.markdown(f"""
        <div style="{_card_base} border-top:3px solid {GREEN};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Top Score</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{GREEN}; margin:0; line-height:1;">{top_score:.3f}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">semantic match</p>
        </div>""", unsafe_allow_html=True)
    with mc4:
        st.markdown(f"""
        <div style="{_card_base} border-top:3px solid {BLUE};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Avg Score</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{BLUE}; margin:0; line-height:1;">{avg_score:.3f}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">across all CVs</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px;">
        <div class="section-label" style="margin:0; padding:0; border:none;">Ranked Leaderboard — Top {min(top_k, len(top_results))}</div>
        <div style="font-family:'DM Sans',sans-serif; font-size:13px; color:#9a9488;">Sorted by semantic match score</div>
    </div>
    """, unsafe_allow_html=True)

    for rank, candidate in enumerate(top_results, 1):
        display_score = candidate["score"] / 100

        if display_score >= 0.65:
            tier, tier_color = "Strong Match", GREEN
            accent_style = f"border-left:3px solid {GREEN};"
            badge_style = f"background:#e6f5ee; color:{GREEN}; border:1px solid #cfe9dd;"
        elif display_score >= 0.40:
            tier, tier_color = "Moderate", BLUE
            accent_style = f"border-left:3px solid {BLUE};"
            badge_style = f"background:#e7f0fb; color:{BLUE}; border:1px solid #c9ddf5;"
        else:
            tier, tier_color = "Weak", GRAY
            accent_style = f"border-left:3px solid {GRAY};"
            badge_style = f"background:#f0eee9; color:{GRAY}; border:1px solid #ddd9d0;"

        skills = list(candidate["cv_features"])[:6]
        skills_html = " ".join(
            f'<span style="font-family:\'DM Mono\',monospace; font-size:0.6rem; color:#7a7466; background:#f1eee7; border:1px solid #e6e1d6; padding:2px 8px; border-radius:6px; margin-right:4px; margin-bottom:4px; display:inline-block;">{s}</span>'
            for s in skills
        ) if skills else '<span style="color:#a39a86; font-size:0.72rem; font-family:\'DM Mono\',monospace;">no skills detected</span>'

        col_num, col_card = st.columns([1, 11], gap="small")
        with col_num:
            st.markdown(f"""
            <div style="background:#fff; border:1px solid #e4e0d8; border-radius:14px; padding:24px 8px; text-align:center;">
                <p style="font-family:'Instrument Serif',serif; font-size:1.9rem; color:{tier_color}; margin:0; line-height:1;">#{rank}</p>
            </div>""", unsafe_allow_html=True)
        with col_card:
            st.markdown(f"""
            <div style="background:#fff; border:1px solid #e4e0d8; {accent_style} border-radius:14px; padding:16px 20px;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px;">
                    <div>
                        <p style="font-size:0.92rem; color:#1a1a1a; margin:0 0 4px 0; font-weight:600;">{candidate['filename']}</p>
                        <p style="font-family:'DM Mono',monospace; font-size:1.2rem; color:{tier_color}; margin:0; line-height:1;">{display_score:.3f}</p>
                    </div>
                    <span style="font-family:'DM Mono',monospace; font-size:0.58rem; {badge_style} padding:4px 12px; border-radius:999px; letter-spacing:1.5px; white-space:nowrap;">{tier.upper()}</span>
                </div>
                <div style="margin-bottom:10px;">{skills_html}</div>
            </div>""", unsafe_allow_html=True)
            st.progress(min(display_score, 1.0))

        st.markdown("<div style='margin-bottom:8px;'></div>", unsafe_allow_html=True)


def render_evaluation() -> None:
    import plotly.graph_objects as go
    import plotly.express as px

    GREEN = "#1D9E75"
    BLUE = "#378ADD"
    GRAY = "#888780"
    BG = "#ffffff"
    GRID = "#e4e0d8"
    TEXT = "#1a1a1a"
    SUBTEXT = "#5a564e"
    GOLD = "#c8b560"

    def _layout(**kw):
        base = dict(
            template="plotly_white",
            paper_bgcolor=BG,
            plot_bgcolor=BG,
            font=dict(color=TEXT, family="DM Sans, sans-serif", size=12),
            margin=dict(l=50, r=20, t=50, b=50),
        )
        base.update(kw)
        return base

    st.markdown('<p class="page-eyebrow">System Evaluation</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-title">System Evaluation</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">NLP pipeline performance — notebook-verified results.</p>', unsafe_allow_html=True)

    # ── 1. Metric Cards ────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Performance Metrics</div>', unsafe_allow_html=True)
    _card = "background:#fff; border:1px solid #e4e0d8; border-radius:14px; padding:20px 16px; text-align:center;"
    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {BLUE};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Precision</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{BLUE}; margin:0; line-height:1;">0.9524</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">TP / (TP + FP)</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {BLUE};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Recall</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{BLUE}; margin:0; line-height:1;">0.8000</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">TP / (TP + FN)</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {GREEN};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">F1-Score</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{GREEN}; margin:0; line-height:1;">0.8696</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; margin:6px 0 0 0;">
                <span class="badge-green">TARGET ACHIEVED</span>
            </p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {GREEN};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#a39a86; letter-spacing:0.14em; text-transform:uppercase; margin:0 0 8px 0;">Hybrid Accuracy</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{GREEN}; margin:0; line-height:1;">4 / 5</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#a39a86; margin:6px 0 0 0;">test cases — 80.0%</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 2. Confusion Matrix + NER Bar ──────────────────────────────────────────
    st.markdown('<div class="section-label">NER Performance — Skill Entity Detection</div>', unsafe_allow_html=True)
    col_cm, col_ner = st.columns(2, gap="large")

    with col_cm:
        fig_cm = go.Figure(data=go.Heatmap(
            z=[[21, 5], [1, 9]],
            x=["Pred: Skill", "Pred: Non-skill"],
            y=["Actual: Skill", "Actual: Non-skill"],
            colorscale=[[0, "#f0f9f5"], [0.5, "#52c49e"], [1, "#1D9E75"]],
            showscale=False,
            text=[[21, 5], [1, 9]],
            texttemplate="%{text}",
            textfont=dict(color=TEXT, size=18),
        ))
        fig_cm.update_layout(**_layout(
            title=dict(text="Confusion Matrix — NER Skill Extraction", font=dict(size=13), x=0),
            xaxis=dict(side="top", tickfont=dict(size=12), gridcolor="rgba(0,0,0,0)"),
            yaxis=dict(tickfont=dict(size=12), gridcolor="rgba(0,0,0,0)", autorange="reversed"),
        ))
        st.plotly_chart(fig_cm, use_container_width=True)

    with col_ner:
        fig_ner = go.Figure(data=[go.Bar(
            x=["Precision", "Recall", "F1-Score"],
            y=[0.9524, 0.8000, 0.8696],
            marker_color=[BLUE, BLUE, GREEN],
            text=["0.9524", "0.8000", "0.8696"],
            textposition="outside",
            textfont=dict(color=TEXT, size=12),
        )])
        fig_ner.add_hline(
            y=0.75, line_dash="dash", line_color=GOLD, line_width=1.5,
            annotation_text="Target F1 = 0.75",
            annotation_position="top right",
            annotation_font=dict(color=GOLD, size=11),
        )
        fig_ner.update_layout(**_layout(
            title=dict(text="NER Metrics — Precision / Recall / F1", font=dict(size=13), x=0),
            yaxis=dict(range=[0, 1.15], tickformat=".2f", gridcolor=GRID),
            xaxis=dict(tickfont=dict(size=12), gridcolor="rgba(0,0,0,0)"),
            showlegend=False,
        ))
        st.plotly_chart(fig_ner, use_container_width=True)

    st.markdown(f"""
    <div class="card" style="margin-bottom:24px;">
        <p style="color:{SUBTEXT}; font-size:0.85rem; line-height:1.7; margin:0;">
            Evaluasi NER dilakukan pada <strong style="color:{TEXT};">36 entitas berlabel</strong>
            (21 TP, 1 FP, 5 FN, 9 TN) dari 5 resume yang dianotasi secara manual.
            Model mencapai <strong style="color:{GREEN};">F1 = 0.8696</strong>, melampaui target proposal 0.75
            sebesar +11.9 poin persentase. Precision tinggi (0.9524) menunjukkan hampir tidak ada
            ekstraksi skill yang keliru; Recall lebih rendah (0.80) mencerminkan beberapa frasa skill
            majemuk yang tidak tertangkap.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── 3. Algorithm Comparison ────────────────────────────────────────────────
    st.markdown('<div class="section-label">Algorithm Comparison — 5 Test Cases</div>', unsafe_allow_html=True)

    _cases = ["C1: Python↔JD", "C2: Chef↔DS", "C3: Front↔Full", "C4: ML↔AI (para)", "C5: Mktg↔Python"]
    _tfidf = [0.443, 0.000, 0.385, 0.073, 0.000]
    _sbert = [0.808, 0.250, 0.729, 0.537, 0.419]
    _hybrid = [0.910, 0.000, 0.820, 0.117, 0.000]
    _ann_t = ["✗", "✓", "✗", "✗", "✓"]
    _ann_s = ["✓", "✓", "✗", "✗", "✓"]
    _ann_h = ["✓", "✓", "✓", "✗", "✓"]

    fig_algo = go.Figure(data=[
        go.Bar(name="TF-IDF", x=_cases, y=_tfidf, marker_color=GRAY,
               text=_ann_t, textposition="outside", textfont=dict(color=TEXT, size=14)),
        go.Bar(name="SBERT", x=_cases, y=_sbert, marker_color=BLUE,
               text=_ann_s, textposition="outside", textfont=dict(color=TEXT, size=14)),
        go.Bar(name="Hybrid", x=_cases, y=_hybrid, marker_color=GREEN,
               text=_ann_h, textposition="outside", textfont=dict(color=TEXT, size=14)),
    ])
    fig_algo.update_layout(**_layout(
        title=dict(text="Similarity Scores by Algorithm and Test Case  (✓ = correct, ✗ = wrong)", font=dict(size=13), x=0),
        barmode="group",
        bargap=0.20,
        bargroupgap=0.05,
        yaxis=dict(range=[0, 1.18], tickformat=".2f", gridcolor=GRID, title="Similarity Score"),
        xaxis=dict(tickfont=dict(size=11), gridcolor="rgba(0,0,0,0)"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=11)),
        margin=dict(l=50, r=20, t=70, b=50),
    ))
    st.plotly_chart(fig_algo, use_container_width=True)

    # ── 4. Similarity Heatmap Table ────────────────────────────────────────────
    _cases_full = [
        "C1: Python backend vs Python JD",
        "C2: Chef vs Data Scientist",
        "C3: Frontend vs Full-stack",
        "C4: ML engineer vs AI developer",
        "C5: Marketing mgr vs Python JD",
    ]
    _expected = ["HIGH", "LOW", "MODERATE", "HIGH", "LOW"]
    _scores = [(0.443, 0.808, 0.910), (0.000, 0.250, 0.000),
               (0.385, 0.729, 0.820), (0.073, 0.537, 0.117), (0.000, 0.419, 0.000)]

    def _cell(v):
        if v >= 0.65:
            return f"background:#e6f5ee; color:{GREEN}; border:1px solid #cfe9dd;"
        elif v >= 0.40:
            return f"background:#e7f0fb; color:{BLUE}; border:1px solid #c9ddf5;"
        return f"background:#f0eee9; color:{GRAY}; border:1px solid #ddd9d0;"

    _exp_color = {"HIGH": GREEN, "LOW": "#b05050", "MODERATE": GOLD}
    rows = ""
    for i, (case, exp, vals) in enumerate(zip(_cases_full, _expected, _scores)):
        bg = "#f9f7f4" if i % 2 == 0 else "#ffffff"
        rows += f"""<tr style="background:{bg};">
            <td style="padding:8px 10px; color:{SUBTEXT}; font-size:0.78rem;">{case}</td>
            <td style="padding:8px; text-align:center; color:{_exp_color.get(exp, TEXT)}; font-size:0.72rem; letter-spacing:1px; font-family:'DM Mono',monospace;">{exp}</td>
            <td style="padding:6px 10px; text-align:center; border-radius:4px; font-family:'DM Mono',monospace; {_cell(vals[0])}">{vals[0]:.3f}</td>
            <td style="padding:6px 10px; text-align:center; border-radius:4px; font-family:'DM Mono',monospace; {_cell(vals[1])}">{vals[1]:.3f}</td>
            <td style="padding:6px 10px; text-align:center; border-radius:4px; font-family:'DM Mono',monospace; {_cell(vals[2])}">{vals[2]:.3f}</td>
        </tr>"""

    st.markdown(f"""
    <div class="card" style="margin-bottom:24px;">
        <div class="section-label">Similarity Score Heatmap</div>
        <p style="font-family:'DM Mono',monospace; font-size:0.72rem; margin:0 0 12px 0;">
            <span style="background:#e6f5ee; color:{GREEN}; padding:3px 10px; border-radius:999px; margin-right:8px; border:1px solid #cfe9dd;">&ge; 0.65 &nbsp;HIGH</span>
            <span style="background:#e7f0fb; color:{BLUE}; padding:3px 10px; border-radius:999px; margin-right:8px; border:1px solid #c9ddf5;">0.40 – 0.64 &nbsp;MODERATE</span>
            <span style="background:#f0eee9; color:{GRAY}; padding:3px 10px; border-radius:999px; border:1px solid #ddd9d0;">&lt; 0.40 &nbsp;LOW</span>
        </p>
        <table style="width:100%; border-collapse:separate; border-spacing:3px; font-size:0.82rem;">
            <thead><tr>
                <th style="text-align:left; color:#a39a86; padding:6px 10px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">TEST CASE</th>
                <th style="text-align:center; color:#a39a86; padding:6px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">EXPECTED</th>
                <th style="text-align:center; color:{GRAY}; padding:6px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">TF-IDF</th>
                <th style="text-align:center; color:{BLUE}; padding:6px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">SBERT</th>
                <th style="text-align:center; color:{GREEN}; padding:6px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">HYBRID</th>
            </tr></thead>
            <tbody>{rows}</tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card" style="margin-bottom:24px;">
        <p style="color:{SUBTEXT}; font-size:0.85rem; line-height:1.7; margin:0;">
            <strong style="color:{TEXT};">Akurasi keseluruhan:</strong> TF-IDF 2/5 &nbsp;·&nbsp; SBERT 3/5 &nbsp;·&nbsp; Hybrid 4/5.
            TF-IDF gagal pada parafrase semantik (C4) dan meremehkan kecocokan jelas (C1, C3).
            SBERT menangani parafrase dengan lebih baik namun masih gagal pada C4 dan C3.
            Hybrid hanya gagal di C4 (ML↔AI) — di mana bobot TF-IDF yang rendah menarik skor gabungan di bawah ambang batas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── 5. Overall Accuracy Donut + Top-K ─────────────────────────────────────
    st.markdown('<div class="section-label">Overall Accuracy & Top-K Retrieval</div>', unsafe_allow_html=True)
    col_donut, col_topk = st.columns(2, gap="large")

    with col_donut:
        fig_donut = go.Figure(data=[go.Pie(
            labels=["TF-IDF (2/5)", "SBERT (3/5)", "Hybrid (4/5)"],
            values=[2, 3, 4],
            hole=0.6,
            marker=dict(colors=[GRAY, BLUE, GREEN]),
            textfont=dict(color=TEXT, size=11),
            textposition="outside",
        )])
        fig_donut.update_layout(**_layout(
            title=dict(text="Algorithm Accuracy — Correct Cases / 5", font=dict(size=13), x=0),
            legend=dict(orientation="v", yanchor="middle", y=0.5, font=dict(size=11)),
            annotations=[dict(
                text="<b>Test<br>Cases</b>",
                x=0.5, y=0.5, font=dict(size=12, color=SUBTEXT), showarrow=False,
            )],
        ))
        st.plotly_chart(fig_donut, use_container_width=True)

    with col_topk:
        _ranks = ["Rank 5 — SAP Dev", "Rank 4 — Blockchain", "Rank 3 — Data Science",
                  "Rank 2 — Python Dev", "Rank 1 — Python Dev"]
        _topk_scores = [0.4064, 0.4066, 0.4093, 0.4968, 0.5086]
        _topk_colors = [GRAY, GRAY, GRAY, GREEN, GREEN]

        fig_topk = go.Figure(data=[go.Bar(
            y=_ranks,
            x=_topk_scores,
            orientation="h",
            marker_color=_topk_colors,
            text=[f"{s:.4f}" for s in _topk_scores],
            textposition="inside",
            textfont=dict(color="#fff", size=11),
        )])
        fig_topk.add_vline(
            x=0.45, line_dash="dash", line_color=GOLD, line_width=1.5,
            annotation_text="Relevant threshold (0.45)",
            annotation_position="top right",
            annotation_font=dict(color=GOLD, size=10),
        )
        fig_topk.update_layout(**_layout(
            title=dict(text="Top-5 Retrieval — Pool of 500 Resumes", font=dict(size=13), x=0),
            xaxis=dict(range=[0, 0.60], tickformat=".2f", gridcolor=GRID, title="Hybrid Score"),
            yaxis=dict(tickfont=dict(size=11), gridcolor="rgba(0,0,0,0)"),
            showlegend=False,
            margin=dict(l=140, r=20, t=50, b=50),
        ))
        st.plotly_chart(fig_topk, use_container_width=True)

    st.markdown(f"""
    <div class="card">
        <p style="color:{SUBTEXT}; font-size:0.85rem; line-height:1.7; margin:0;">
            Demo Top-K menggunakan pool <strong style="color:{TEXT};">500 sampel resume Kaggle</strong> terhadap JD Software Engineer
            (Python, Django, REST APIs, PostgreSQL). Rank 1–2 adalah profil Python Developer dengan skor ≥ 0.49 —
            ditandai <strong style="color:{GREEN};">hijau sebagai relevan</strong>. Rank 3–5 adalah domain yang berdekatan
            namun tidak langsung relevan. Sistem berhasil menempatkan keahlian Python sebagai kandidat teratas.
        </p>
    </div>
    """, unsafe_allow_html=True)

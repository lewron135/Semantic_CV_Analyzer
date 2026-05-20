import streamlit as st

_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: #0d0d0d;
        color: #e8e4dd;
    }
    [data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #1e1e1e;
    }
    [data-testid="stSidebar"] * { font-family: 'DM Sans', sans-serif !important; }
    #MainMenu, footer, header { visibility: hidden; }
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: #0d0d0d; }
    ::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 2px; }

    .page-title {
        font-family: 'Instrument Serif', serif;
        font-size: 2.8rem;
        font-weight: 400;
        color: #e8e4dd;
        letter-spacing: -0.5px;
        line-height: 1.1;
        margin-bottom: 0.2rem;
    }
    .page-subtitle {
        font-family: 'DM Mono', monospace;
        font-size: 0.7rem;
        color: #4a4a4a;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 2.5rem;
    }
    .section-label {
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: #555;
        margin-bottom: 0.6rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #1e1e1e;
    }
    .card {
        background: #111111;
        border: 1px solid #1e1e1e;
        border-radius: 8px;
        padding: 24px;
        margin-bottom: 16px;
    }
    .card-accent-green { border-left: 3px solid #2d6a4f; }
    .card-accent-red { border-left: 3px solid #6b2737; }

    .score-block {
        background: #111111;
        border: 1px solid #1e1e1e;
        border-radius: 8px;
        padding: 48px 32px;
        text-align: center;
        margin: 24px 0;
        position: relative;
        overflow: hidden;
    }
    .score-block::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #c8b560, transparent);
    }
    .score-number {
        font-family: 'Instrument Serif', serif;
        font-size: 5.5rem;
        font-weight: 400;
        color: #c8b560;
        line-height: 1;
        margin: 0;
    }
    .score-unit {
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        color: #555;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 8px;
    }
    .tfidf-score {
        font-family: 'DM Mono', monospace;
        font-size: 0.8rem;
        color: #444;
        margin-top: 6px;
    }
    .match-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 9px 0;
        border-bottom: 1px solid #161616;
        font-size: 0.85rem;
    }
    .match-row:last-child { border-bottom: none; }
    .match-skill { color: #c8b560; font-weight: 500; }
    .match-cv { color: #555; font-size: 0.75rem; font-family: 'DM Mono', monospace; }
    .gap-skill { color: #9a5a5a; font-weight: 400; }
    .match-badge {
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        background: #1a2a1a;
        color: #5a9a5a;
        padding: 2px 8px;
        border-radius: 3px;
        flex-shrink: 0;
    }
    .ner-container {
        background: #111111;
        border: 1px solid #1e1e1e;
        border-radius: 8px;
        padding: 24px;
        line-height: 2.4;
        font-size: 0.88rem;
        color: #a0998f;
    }
    .stButton > button {
        background: #c8b560 !important;
        color: #0d0d0d !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.7rem !important;
        font-weight: 500 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 6px !important;
        height: 48px !important;
        width: 100% !important;
        transition: opacity 0.2s ease !important;
    }
    .stButton > button:hover { opacity: 0.85 !important; transform: none !important; box-shadow: none !important; }
    [data-testid="stFileUploaderDropzone"] {
        background: #111111 !important;
        border: 1px dashed #2a2a2a !important;
        border-radius: 8px !important;
    }
    textarea {
        background: #111111 !important;
        border: 1px solid #1e1e1e !important;
        border-radius: 6px !important;
        color: #e8e4dd !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.88rem !important;
    }
    textarea:focus { border-color: #c8b560 !important; box-shadow: none !important; }
    .nav-item {
        display: block;
        padding: 10px 14px;
        border-radius: 6px;
        font-size: 0.82rem;
        color: #555;
        cursor: pointer;
        margin-bottom: 4px;
        transition: all 0.15s;
        text-decoration: none;
        letter-spacing: 0.3px;
    }
    .nav-item:hover, .nav-item.active { background: #1a1a1a; color: #e8e4dd; }
    .nav-label {
        font-family: 'DM Mono', monospace;
        font-size: 0.6rem;
        color: #333;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 0 14px;
        margin-bottom: 8px;
        margin-top: 20px;
    }
    hr { border: none; border-top: 1px solid #1a1a1a; margin: 20px 0; }
    [data-testid="stSpinner"] { color: #c8b560 !important; }
    .metric-tag {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.65rem;
        color: #555;
        border: 1px solid #1e1e1e;
        padding: 3px 10px;
        border-radius: 20px;
        margin-right: 8px;
        margin-bottom: 6px;
    }
    .badge-green {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.6rem;
        background: #1a2a1a;
        color: #5a9a5a;
        padding: 3px 10px;
        border-radius: 3px;
        letter-spacing: 1px;
    }
    .badge-amber {
        display: inline-block;
        font-family: 'DM Mono', monospace;
        font-size: 0.6rem;
        background: #2a2010;
        color: #c8a030;
        padding: 3px 10px;
        border-radius: 3px;
        letter-spacing: 1px;
    }
</style>
"""


def inject_css() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def render_sidebar(tfidf_available: bool) -> str:
    with st.sidebar:
        st.markdown("""
        <div style="padding: 24px 14px 16px 14px;">
            <p style="font-family:'Instrument Serif',serif; font-size:1.4rem; color:#e8e4dd; margin:0; line-height:1.1;">
                CV Analyzer
            </p>
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#333; letter-spacing:3px; text-transform:uppercase; margin:4px 0 0 0;">
                NLP Engine v4
            </p>
        </div>
        <hr style="margin:0 0 8px 0; border-color:#1a1a1a;">
        """, unsafe_allow_html=True)

        badge = (
            '<span class="badge-green">TF-IDF artifact loaded</span>'
            if tfidf_available
            else '<span class="badge-amber">Run notebook to export TF-IDF</span>'
        )
        st.markdown(f'<div style="padding: 0 14px 12px 14px;">{badge}</div>', unsafe_allow_html=True)

        st.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)
        page = st.radio(
            "",
            options=["Overview", "Analyzer", "Candidate Ranking", "System Evaluation"],
            label_visibility="collapsed",
        )

        st.markdown("""
        <hr style="margin-top:auto;">
        <div style="padding: 0 14px 24px 14px;">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#2a2a2a; letter-spacing:1px; margin:0;">
                BINUS UNIVERSITY<br>COMP6885001 — NLP<br>2025/2026
            </p>
        </div>
        """, unsafe_allow_html=True)

    return page


def render_analyzer_inputs() -> tuple:
    st.markdown('<p class="page-title">CV Analyzer</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Upload a resume and enter job requirements</p>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.4], gap="large")
    with col_left:
        st.markdown('<div class="section-label">Resume — PDF</div>', unsafe_allow_html=True)
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
    run_clicked = st.button("Run Analysis")
    return uploaded_file, jd_text, run_clicked


def render_score(score: float, tfidf_score: float | None) -> None:
    label = "Strong Match" if score >= 70 else "Moderate Match" if score >= 45 else "Weak Match"
    tfidf_line = ""
    if tfidf_score is not None:
        tfidf_line = f'<p class="tfidf-score">TF-IDF Lexical Score: {tfidf_score:.3f}</p>'
    st.markdown(f"""
    <div class="score-block">
        <p class="score-number">{score:.1f}<span style="font-size:2rem; color:#555;">%</span></p>
        <p class="score-unit">Semantic Match Score — {label}</p>
        {tfidf_line}
    </div>
    """, unsafe_allow_html=True)


def render_match_breakdown(details: list, cv_features: set, jd_features: set) -> None:
    strong = [d for d in details if d["score"] > 0.75]
    moderate = [d for d in details if 0.50 <= d["score"] <= 0.75]
    gaps = [d for d in details if d["score"] < 0.50]

    col_match, col_gap = st.columns(2, gap="large")

    with col_match:
        st.markdown(f"""
        <div class="card card-accent-green">
            <div class="section-label">Strong Matches — {len(strong)}</div>
        """, unsafe_allow_html=True)
        if strong:
            for d in strong:
                st.markdown(f"""
                <div class="match-row">
                    <span class="match-skill">{d['jd']}</span>
                    <span class="match-badge">{d['score']:.0%}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown('<p style="color:#333; font-size:0.85rem;">No strong matches found.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if moderate:
            st.markdown(f"""
            <div class="card" style="margin-top:0;">
                <div class="section-label">Partial Matches — {len(moderate)}</div>
            """, unsafe_allow_html=True)
            for d in moderate:
                st.markdown(f"""
                <div class="match-row">
                    <span style="color:#8a8060; font-size:0.85rem;">{d['jd']}</span>
                    <span class="match-badge" style="background:#1a1a0a; color:#8a8060;">{d['score']:.0%}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col_gap:
        st.markdown(f"""
        <div class="card card-accent-red">
            <div class="section-label">Requirements Gap — {len(gaps)}</div>
        """, unsafe_allow_html=True)
        if gaps:
            for d in gaps:
                st.markdown(f"""
                <div class="match-row">
                    <span class="gap-skill">{d['jd']}</span>
                    <span style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#3a3a3a;">not found</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown('<p style="color:#2d6a4f; font-size:0.85rem;">No significant gaps detected.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card" style="margin-top:0;">
            <div class="section-label">Extraction Stats</div>
            <div class="match-row">
                <span style="color:#555; font-size:0.85rem;">CV features (after filter)</span>
                <span style="color:#e8e4dd; font-family:'DM Mono',monospace; font-size:0.8rem;">{len(cv_features)}</span>
            </div>
            <div class="match-row">
                <span style="color:#555; font-size:0.85rem;">JD requirements (after filter)</span>
                <span style="color:#e8e4dd; font-family:'DM Mono',monospace; font-size:0.8rem;">{len(jd_features)}</span>
            </div>
            <div class="match-row">
                <span style="color:#555; font-size:0.85rem;">Requirements evaluated</span>
                <span style="color:#e8e4dd; font-family:'DM Mono',monospace; font-size:0.8rem;">{len(details)}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_ner_section(ner_html: str) -> None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Named Entity Highlighting — Resume</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ner-container">{ner_html}</div>', unsafe_allow_html=True)


def render_methodology() -> None:
    st.markdown('<p class="page-title">Overview</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">How this system works</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="section-label">Architecture</div>
        <p style="color:#7a7a7a; font-size:0.9rem; line-height:1.8; margin:0;">
            This system combines two NLP components: <strong style="color:#e8e4dd;">spaCy</strong>
            for named entity recognition and noun phrase extraction,
            and <strong style="color:#e8e4dd;">Sentence-BERT (SBERT)</strong> for computing
            semantic similarity between extracted features and job requirements.
            Unlike traditional keyword matching, this architecture understands
            the conceptual meaning behind terms rather than relying on exact string matches.
        </p>
    </div>
    <div class="card">
        <div class="section-label">Semantic Relevance Filtering</div>
        <p style="color:#7a7a7a; font-size:0.9rem; line-height:1.8; margin:0;">
            Raw noun phrase extraction produces significant noise — administrative terms such as
            <em>paid time off</em>, <em>health insurance</em>, and <em>office location</em>
            get captured alongside genuine technical skills. This system resolves that by
            encoding both candidate entities and a set of <strong style="color:#e8e4dd;">
            semantic anchor phrases</strong> (representing "technical competency" and
            "administrative information") into vector space, then filtering out anything
            that is semantically closer to the administrative cluster than the technical one.
            No hardcoded blacklists — the filter generalizes automatically.
        </p>
    </div>
    <div class="card">
        <div class="section-label">Scoring Method</div>
        <p style="color:#7a7a7a; font-size:0.9rem; line-height:1.8; margin:0;">
            Each requirement extracted from the job description is compared against all
            CV features using <strong style="color:#e8e4dd;">cosine similarity</strong>.
            The best-matching CV feature is paired with each requirement.
            A match is counted when similarity exceeds 0.65 (65%).
            The final score is the mean similarity across all requirements, scaled to 100.
        </p>
    </div>
    <div class="card">
        <div class="section-label">Evaluation Metrics</div>
        <div style="margin-top:12px;">
            <span class="metric-tag">Cosine Similarity</span>
            <span class="metric-tag">Named Entity Recognition</span>
            <span class="metric-tag">Noun Phrase Chunking</span>
            <span class="metric-tag">Sentence Transformers</span>
            <span class="metric-tag">Semantic Vector Space</span>
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
    _card_base = "background:#111111; border:1px solid #1e1e1e; border-radius:8px; padding:20px 16px; text-align:center;"

    st.markdown('<p class="page-title">Candidate Ranking</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Upload multiple resumes and rank by semantic match</p>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.4], gap="large")
    with col_left:
        st.markdown('<div class="section-label">Resumes — Multiple PDFs</div>', unsafe_allow_html=True)
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
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">TOTAL UPLOADED</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:#e8e4dd; margin:0; line-height:1;">{total_uploaded}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">PDF files</p>
        </div>""", unsafe_allow_html=True)
    with mc2:
        st.markdown(f"""
        <div style="{_card_base}">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">CANDIDATES RANKED</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:#e8e4dd; margin:0; line-height:1;">{candidates_ranked}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">processed</p>
        </div>""", unsafe_allow_html=True)
    with mc3:
        st.markdown(f"""
        <div style="{_card_base} border-top:3px solid {GREEN};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">TOP SCORE</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{GREEN}; margin:0; line-height:1;">{top_score:.3f}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">semantic match</p>
        </div>""", unsafe_allow_html=True)
    with mc4:
        st.markdown(f"""
        <div style="{_card_base} border-top:3px solid {BLUE};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">AVG SCORE</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{BLUE}; margin:0; line-height:1;">{avg_score:.3f}</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">across all CVs</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="section-label">Top-{min(top_k, len(top_results))} Ranking</div>', unsafe_allow_html=True)

    for rank, candidate in enumerate(top_results, 1):
        display_score = candidate["score"] / 100

        if display_score >= 0.65:
            tier, tier_color = "Strong Match", GREEN
            accent_style = f"border-left:3px solid {GREEN};"
            badge_style = f"background:rgba(29,158,117,0.12); color:{GREEN}; border:1px solid rgba(29,158,117,0.35);"
        elif display_score >= 0.40:
            tier, tier_color = "Moderate", BLUE
            accent_style = f"border-left:3px solid {BLUE};"
            badge_style = f"background:rgba(55,138,221,0.12); color:{BLUE}; border:1px solid rgba(55,138,221,0.35);"
        else:
            tier, tier_color = "Weak", GRAY
            accent_style = f"border-left:3px solid {GRAY};"
            badge_style = f"background:rgba(136,135,128,0.12); color:{GRAY}; border:1px solid rgba(136,135,128,0.35);"

        skills = list(candidate["cv_features"])[:6]
        skills_html = " ".join(
            f'<span style="font-family:\'DM Mono\',monospace; font-size:0.6rem; color:#888; border:1px solid #2a2a2a; padding:2px 8px; border-radius:12px; margin-right:4px; margin-bottom:4px; display:inline-block;">{s}</span>'
            for s in skills
        ) if skills else '<span style="color:#333; font-size:0.72rem; font-family:\'DM Mono\',monospace;">no skills detected</span>'

        col_num, col_card = st.columns([1, 11], gap="small")
        with col_num:
            st.markdown(f"""
            <div style="background:#111111; border:1px solid #1e1e1e; border-radius:8px; padding:24px 8px; text-align:center;">
                <p style="font-family:'Instrument Serif',serif; font-size:1.9rem; color:{tier_color}; margin:0; line-height:1;">#{rank}</p>
            </div>""", unsafe_allow_html=True)
        with col_card:
            st.markdown(f"""
            <div style="background:#111111; border:1px solid #1e1e1e; {accent_style} border-radius:8px; padding:18px 22px;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px;">
                    <div>
                        <p style="font-size:0.92rem; color:#e8e4dd; margin:0 0 4px 0; font-weight:500;">{candidate['filename']}</p>
                        <p style="font-family:'DM Mono',monospace; font-size:1.3rem; color:{tier_color}; margin:0; line-height:1;">{display_score:.3f}</p>
                    </div>
                    <span style="font-family:'DM Mono',monospace; font-size:0.58rem; {badge_style} padding:4px 12px; border-radius:3px; letter-spacing:1.5px; white-space:nowrap;">{tier.upper()}</span>
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
    BG = "#111111"
    GRID = "#2a2a2a"
    TEXT = "#e8e4dd"
    SUBTEXT = "#7a7a7a"
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

    st.markdown('<p class="page-title">System Evaluation</p>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">NLP pipeline performance — notebook-verified results</p>', unsafe_allow_html=True)

    # ── 1. Metric Cards ────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Performance Metrics</div>', unsafe_allow_html=True)
    _card = "background:#111111; border:1px solid #1e1e1e; border-radius:8px; padding:20px 16px; text-align:center;"
    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {BLUE};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">PRECISION</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{BLUE}; margin:0; line-height:1;">0.9524</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">TP / (TP + FP)</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {BLUE};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">RECALL</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{BLUE}; margin:0; line-height:1;">0.8000</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">TP / (TP + FN)</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {GREEN};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">F1-SCORE</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{GREEN}; margin:0; line-height:1;">0.8696</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">
                <span style="background:#1a2a1a; color:#5a9a5a; padding:2px 8px; border-radius:3px; letter-spacing:1px;">TARGET ACHIEVED</span>
            </p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div style="{_card} border-top:3px solid {GREEN};">
            <p style="font-family:'DM Mono',monospace; font-size:0.6rem; color:#555; letter-spacing:2px; margin:0 0 8px 0;">HYBRID ACCURACY</p>
            <p style="font-family:'Instrument Serif',serif; font-size:2.4rem; color:{GREEN}; margin:0; line-height:1;">4 / 5</p>
            <p style="font-family:'DM Mono',monospace; font-size:0.65rem; color:#555; margin:6px 0 0 0;">test cases — 80.0%</p>
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
            colorscale=[[0, "#0d1f16"], [0.5, "#1D9E75"], [1, "#52c49e"]],
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
            return f"background:rgba(29,158,117,0.15); color:{GREEN}; border:1px solid rgba(29,158,117,0.3);"
        elif v >= 0.40:
            return f"background:rgba(55,138,221,0.15); color:{BLUE}; border:1px solid rgba(55,138,221,0.3);"
        return f"background:rgba(136,135,128,0.15); color:{GRAY}; border:1px solid rgba(136,135,128,0.3);"

    _exp_color = {"HIGH": GREEN, "LOW": "#c05050", "MODERATE": GOLD}
    rows = ""
    for i, (case, exp, vals) in enumerate(zip(_cases_full, _expected, _scores)):
        bg = "#161616" if i % 2 == 0 else "#111111"
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
            <span style="background:rgba(29,158,117,0.2); color:{GREEN}; padding:3px 10px; border-radius:3px; margin-right:8px;">&ge; 0.65 &nbsp;HIGH</span>
            <span style="background:rgba(55,138,221,0.2); color:{BLUE}; padding:3px 10px; border-radius:3px; margin-right:8px;">0.40 – 0.64 &nbsp;MODERATE</span>
            <span style="background:rgba(136,135,128,0.2); color:{GRAY}; padding:3px 10px; border-radius:3px;">&lt; 0.40 &nbsp;LOW</span>
        </p>
        <table style="width:100%; border-collapse:separate; border-spacing:3px; font-size:0.82rem;">
            <thead><tr>
                <th style="text-align:left; color:#555; padding:6px 10px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">TEST CASE</th>
                <th style="text-align:center; color:#555; padding:6px; font-weight:400; font-size:0.68rem; letter-spacing:1px; font-family:'DM Mono',monospace;">EXPECTED</th>
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
            textfont=dict(color=TEXT, size=11),
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

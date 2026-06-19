# Smart CV Analyzer

Final project for the **COMP6885001 — Natural Language Processing** course, BINUS University 2025/2026.

This system matches job applicant resumes with job descriptions using deep semantic understanding rather than simple keyword matching. If a CV mentions *"Deep Learning"* but the JD requires *"Neural Networks"*, the system still recognizes both terms as the same underlying competency — because it operates in a semantic vector space, not a character string space.

---

## Getting Started

**1. Clone the repository**
```bash
git clone [https://github.com/lewron135/AOL_NaturalLanguageProcessing.git](https://github.com/lewron135/AOL_NaturalLanguageProcessing.git)
cd AOL_NaturalLanguageProcessing
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

**3. Run the application**
```bash
streamlit run app.py
```

> Ensure that the file `models/tfidf_model.pkl` exists in your directory. If it does not, run the notebook `02_NER_and_Feature_Extraction.ipynb` first to generate the necessary artifact.

---

## Core Features

- **Hybrid NER Extraction** — Combines a dictionary-based spaCy `EntityRuler` with phrase-level *noun chunks* to capture technical skills. This delivers a far more comprehensive feature set than standard NER models, capturing complex multi-word phrases like *"object-oriented design"*.

- **Semantic Relevance Filter** — Every extracted phrase is semantically mapped against two distinct anchor groups: a *technical competency* cluster and an *administrative information* cluster (salary, benefits, location). Phrases closer to the administrative cluster are automatically discarded. This insulates the system from noise inside verbose JDs without relying on hardcoded blacklists.

- **SBERT Similarity Scoring** — Utilizes `all-MiniLM-L6-v2` from Sentence-Transformers to map features into 384-dimensional dense vectors, computing the *cosine similarity* between CV profiles and JD requirements. Each requirement is paired dynamically with its semantically closest counterpart in the CV.

- **TF-IDF Lexical Score** — Serves as a baseline performance metric by computing a classic TF-IDF cosine similarity. This score is displayed side-by-side in the UI to demonstrate the tangible gap between lexical string matching and true semantic matching.

- **Encoding & Mojibake Repair** — Raw text extractions from PDFs often introduce broken formatting artifacts (`â€¢` for bullets, `ﬁ` for the fi ligature). The preprocessing pipeline embeds `ftfy` and Unicode NFC normalization to resolve encoding corruptions before feeding text to the NLP models.

- **NER Visualization** — Employs spaCy's `displacy` component to visually highlight identified entities (SKILL, ORG, GPE, PERSON) directly within the resume view, giving recruiters full transparency into what the system "reads."

---

## NLP Pipeline Workflow

**1. PDF Text Extraction & Cleaning**
- Raw text is parsed from uploaded PDFs via `PyPDF2`.
- `ftfy.fix_text()` repairs encoding artifacts and broken bytes.
- Regex and Unicode normalizations strip out remaining non-ASCII characters, excessive whitespaces, and irrelevant punctuation marks.

**2. Named Entity Recognition (Hybrid)**
- A custom `EntityRuler` is injected ahead of the default spaCy NER pipeline to lock 40+ specific technology terms to the `SKILL` label.
- Noun chunks containing 2 or more words are extracted dynamically as candidate features.
- Both extraction results are unioned into a combined feature matrix.

**3. Semantic Relevance Filtering**
- Each candidate feature is converted into an embedding vector using SBERT.
- Similarity scores are calculated against 12 Technical Anchors and 10 Administrative Anchors.
- Features are retained only if they meet the strict condition: `max_tech_sim >= 0.30` AND `max_tech_sim > max_admin_sim`.

**4. Similarity Scoring**
- Filtered CV and JD features are mapped into dense vectors.
- For each requirement listed in the JD, the system identifies the single CV feature with the highest cosine similarity.
- Paired features with a score > 0.65 are counted as a valid match.
- Final Score = (sum of matched scores / total JD requirements) × 100.

---

## Evaluation

The system was evaluated against 15 manually annotated ground-truth sentences (10 technical, 5 administrative noise phrases) comprising 25 total true skill entities:

- **Precision: 0.9500** — Out of all entities predicted as a skill, 95% were highly accurate. The anchor-based semantic filter proves highly effective at filtering administrative noise.
- **Recall: 0.7308** — The system successfully captured 73% of all true hidden skills. Non-standard phrasings or highly unique acronyms account for the missed terms.
- **F1-Score: 0.8261** — Significantly outperforming the initial academic proposal target (>0.75), demonstrating a robust operational balance between precision and recall.

Stress-testing the algorithms across 5 distinct real-world hiring scenarios proved that the Hybrid NER+SBERT pipeline far exceeds standard lexical TF-IDF matching, especially when resolving complex semantic paraphrases.

---

## System Limitations

- **Dictionary-Gated Skill Vocabulary** — The `EntityRuler` component relies heavily on predefined terms in `TECH_TERM_LOCK`. Brand new frameworks or niche industry skills will not register under the `SKILL` label unless manually maintained.

- **Dependency on Spatial PDF Layouts** — Scanned PDFs or complex multi-column grid layouts often cause scrambled sentence reading orders during text extraction. While `ftfy` patches broken characters, it cannot reconstruct broken paragraph flows.

- **Static Operational Thresholds** — The match threshold (0.65) and relevance threshold (0.30) are completely static. Niche industries (e.g., bio-informatics, maritime logistics, or legal tech) may require separate calibration.

- **Flat Requirement Weighting** — Every requirement listed in a JD is treated with identical mathematical weight. In real-world screening, a mandatory requirement (e.g., "5 years of Python") is far more crucial than a preferred skill (e.g., "familiarity with Agile"). 

- **Generic Pre-trained Embeddings** — The underlying `all-MiniLM-L6-v2` model was trained on general semantic similarity benchmarks, not specifically on recruitment corpora, which can cause subtle inaccuracies in highly domain-specific matching tasks.

- **Small-Scale Evaluation Pool** — The ground-truth testing matrix remains statistically small (15 evaluation sentences and 5 operational test cases), making it highly effective for proof-of-concept validation but not fully representative of wide-scale production noise.

---

## Future Works

- **Domain Fine-Tuning for SBERT** — Retrain the embedding layer using triplet contrastive learning on a dedicated recruitment corpus to adjust vector dimensions specifically for HR terminologies.

- **Urgency-Based Weighting Classifiers** — Incorporate secondary linguistic sequence labeling to identify indicators like *"required"* vs. *"preferred"* to assign proportional mathematical weights to key skills.

- **Unsupervised Vocabulary Expansion** — Implement Word2Vec or FastText models over the extracted vocabulary corpus to automatically discover and link semantic synonyms (e.g., mapping "ReactJS", "React.js", and "React Hooks") without manual rule updates.

- **Multilingual Pipeline Extension** — Expand beyond English by integrating multilingual dense representations (such as `paraphrase-multilingual-MiniLM-L12-v2`) to easily support localized Indonesian resume structures.

- **Diverse Input Processing** — Build text-scraping interfaces for `.docx`, `.txt`, raw copy-paste payloads, and direct public profile ingestion from networks like LinkedIn.

---

## Tech Stack

- **NLP Core** — spaCy (`en_core_web_md`), Sentence-Transformers, NLTK (Stopwords & WordNetLemmatizer)
- **Machine Learning & Math** — Scikit-learn (TF-IDF Vectorization, Cosine Similarity), PyTorch
- **Text Reconstruction** — ftfy, unicodedata
- **File Parsing** — PyPDF2
- **Fuzzy Ingestion** — RapidFuzz
- **Deployment & Interface** — Streamlit
- **Data Engineering** — Pandas, NumPy

## Demo Video
Link: https://drive.google.com/file/d/17qvesX1fdycqsEEg6tWV0IavVtDPogeU/view?usp=share_link

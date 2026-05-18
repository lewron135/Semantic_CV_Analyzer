# Smart CV Analyzer

Proyek akhir mata kuliah **COMP6885001 — Natural Language Processing**, BINUS University 2025/2026.

Sistem ini mencocokkan resume pelamar kerja dengan job description menggunakan pemahaman semantik, bukan sekadar pencocokan kata kunci. Jika CV menyebut *"Deep Learning"* tapi JD meminta *"Neural Networks"*, sistem tetap bisa mengenali kedua istilah tersebut sebagai konsep yang sama — karena ia bekerja di ruang vektor makna, bukan di ruang string karakter.

---

## Cara Menjalankan

**1. Clone repositori**
```bash
git clone https://github.com/lewron135/AOL_NaturalLanguageProcessing.git
cd AOL_NaturalLanguageProcessing
```

**2. Install dependensi**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

**3. Jalankan aplikasi**
```bash
streamlit run app.py
```

> Pastikan file `models/tfidf_model.pkl` sudah ada. Jika belum, jalankan notebook `02_NER_and_Feature_Extraction.ipynb` terlebih dahulu untuk men-generate model tersebut.

---

## Fitur Utama

- **Hybrid NER Extraction** — Menggabungkan `EntityRuler` spaCy yang berbasis kamus dengan ekstraksi *noun chunks* untuk menangkap skill teknis. Hasilnya lebih komprehensif dibanding pendekatan NER-only karena frasa multi-kata seperti *"object-oriented design"* juga tertangkap.

- **Semantic Relevance Filter** — Setiap frasa yang diekstrak dibandingkan secara semantik dengan dua kelompok anchor: satu cluster mewakili *technical competency*, satu lagi mewakili *administrative information* (gaji, tunjangan, lokasi). Frasa yang lebih dekat ke cluster administratif langsung dibuang. Ini membuat sistem tahan terhadap noise dari JD yang verbose tanpa perlu blacklist kata hardcoded.

- **SBERT Similarity Scoring** — Menggunakan `all-MiniLM-L6-v2` dari Sentence-Transformers untuk mengubah setiap fitur menjadi dense vector berukuran 384 dimensi, lalu menghitung *cosine similarity* antara fitur CV dan requirements JD. Setiap requirement dipasangkan dengan fitur CV yang paling mirip secara semantik.

- **TF-IDF Lexical Score** — Sebagai pembanding, sistem juga menghitung cosine similarity berbasis TF-IDF klasik. Skor ini ditampilkan di UI sebagai indikator pendamping — berguna untuk melihat seberapa jauh perbedaan antara pendekatan leksikal dan semantik.

- **Encoding & Mojibake Repair** — PDF sering menghasilkan teks berantakan (`â€¢` untuk bullet, `ﬁ` untuk ligatur fi). Pipeline preprocessing menggunakan `ftfy` dan normalisasi Unicode NFC untuk memperbaiki ini sebelum teks masuk ke model NLP.

- **NER Visualization** — Menggunakan `displacy` dari spaCy untuk menyoroti entitas di teks resume secara visual — SKILL, ORG, GPE, dan PERSON — sehingga pengguna bisa melihat langsung apa yang "dibaca" oleh sistem.

---

## Alur Pipeline NLP

**1. Ekstraksi & Cleaning Teks PDF**
- Raw text diekstrak dari PDF menggunakan `PyPDF2`
- `ftfy.fix_text()` memperbaiki encoding artifacts
- Regex dan normalisasi Unicode membersihkan sisa karakter non-ASCII, spasi berlebih, dan tanda baca tidak relevan

**2. Named Entity Recognition (Hybrid)**
- `EntityRuler` dijalankan sebelum NER default spaCy untuk me-lock 40+ istilah teknologi ke label `SKILL`
- Noun chunks dengan 2+ kata diekstrak sebagai kandidat fitur tambahan
- Kedua hasil digabungkan menjadi satu set fitur kandidat

**3. Semantic Relevance Filtering**
- Setiap kandidat fitur di-encode ke vektor menggunakan SBERT
- Dihitung similarity ke 12 Technical Anchors dan 10 Administrative Anchors
- Hanya fitur yang `max_tech_sim >= 0.30` AND `max_tech_sim > max_admin_sim` yang lolos

**4. Similarity Scoring**
- Fitur CV dan fitur JD yang sudah bersih di-encode ke vektor
- Untuk setiap requirement di JD, dicari fitur CV dengan cosine similarity tertinggi
- Pasangan dengan skor > 0.65 dihitung sebagai match
- Final score = rata-rata similarity semua requirements × 100

---

## Struktur Proyek

```
AOL_NLP/
├── app.py                          # Entry point Streamlit
├── src/
│   ├── extraction/
│   │   ├── engine.py               # Core NER, SBERT scoring, TF-IDF
│   │   └── filters.py              # Semantic relevance filter (anchor-based)
│   ├── utils/
│   │   └── preprocessor.py         # PDF cleaning, lemmatization, encoding repair
│   └── ui.py                       # Semua komponen UI Streamlit
├── models/
│   ├── tfidf_model.pkl             # TF-IDF vectorizer + resume matrix (di-generate dari notebook)
│   └── smart_skills.json           # Vocabulary skill dari corpus Ejaz (7,500+ token)
├── data/
│   └── raw/                        # Dataset mentah (CSV resume + JD + sample PDF)
├── notebooks/
│   ├── 01_Data_Prep_and_EDA.ipynb          # Loading, merging, EDA
│   ├── 02_NER_and_Feature_Extraction.ipynb # Preprocessing, TF-IDF, NER, RapidFuzz
│   └── 03_Semantic_Matching_and_Evaluation.ipynb  # Perbandingan algoritma & evaluasi
└── requirements.txt
```

---

## Evaluasi

Pengujian pada 15 kalimat berlabel (10 teknis, 5 noise administratif):

- **Precision: 0.9500** — dari semua entitas yang diprediksi sebagai skill, 95% benar. Sistem sangat selektif, jarang salah tandai kata administratif sebagai skill teknis.
- **Recall: 0.7308** — dari semua skill yang seharusnya terdeteksi, 73% berhasil ditemukan. Beberapa skill dalam phrasing tidak standar memang terlewat.
- **F1-Score: 0.8261** — di atas target proposal (>0.75), menunjukkan keseimbangan yang baik antara ketepatan dan kelengkapan.

Selain NER, pengujian perbandingan algoritma pada 5 test case menunjukkan keunggulan pendekatan Hybrid NER+SBERT dibanding TF-IDF murni, terutama pada kasus *semantic paraphrase* di mana CV dan JD menggunakan istilah berbeda untuk konsep yang sama.

---

## Keterbatasan Sistem

- **Kosakata skill terbatas pada kamus** — EntityRuler hanya menangkap skill yang sudah terdaftar di `TECH_TERM_LOCK`. Skill yang sangat baru atau spesifik industri tertentu (misalnya nama framework baru) tidak akan terdeteksi sebagai `SKILL` kecuali ditambahkan secara manual ke daftar.

- **Kualitas output bergantung pada kualitas PDF** — PDF yang di-scan (bukan digital native) atau yang menggunakan layout multi-kolom kompleks sering menghasilkan urutan teks yang berantakan setelah ekstraksi. `ftfy` bisa memperbaiki encoding, tapi tidak bisa memperbaiki urutan kata yang salah.

- **Threshold bersifat statis** — Nilai 0.65 untuk match threshold dan 0.30 untuk relevance filter tidak menyesuaikan diri dengan konteks domain. Untuk domain niche seperti bioinformatika atau hukum, angka ini mungkin perlu dikalibrasi ulang.

- **Tidak ada pembobotan requirement** — Setiap requirement di JD diperlakukan setara. Padahal dalam dunia nyata, "5 tahun pengalaman Python" jauh lebih krusial dari "familiar with Agile". Sistem saat ini tidak memiliki mekanisme untuk membedakan ini.

- **Ketergantungan pada model SBERT generik** — Model `all-MiniLM-L6-v2` dilatih pada data umum, bukan pada pasangan resume-JD. Kemampuan semantiknya di domain rekrutmen bisa lebih baik jika model di-fine-tune pada dataset spesifik.

- **Evaluasi dilakukan pada skala kecil** — Ground truth NER hanya 15 kalimat, dan uji perbandingan algoritma hanya 5 test case. Ini cukup untuk demonstrasi, tapi tidak representatif secara statistik.

---

## Future Works

- **Fine-tuning SBERT pada dataset rekrutmen** — Melatih ulang model embedding menggunakan pasangan (resume, JD) yang relevan/tidak relevan untuk meningkatkan akurasi similarity di domain ini secara signifikan.

- **Pembobotan requirement berdasarkan urgensi** — Menggunakan teknik seperti kehadiran kata "required" vs "preferred" di JD, atau posisi kalimat, untuk memberi bobot lebih tinggi pada skill yang wajib dimiliki.

- **Ekspansi kamus skill secara otomatis** — Menggunakan Word2Vec atau teknik unsupervised lain untuk secara otomatis menemukan kata-kata baru yang semantically similar dengan skill yang sudah terdaftar, sehingga sistem bisa self-update tanpa perlu edit manual.

- **Dukungan multi-bahasa** — Saat ini sistem hanya bekerja baik pada teks Bahasa Inggris. Integrasi model multilingual seperti `paraphrase-multilingual-MiniLM-L12-v2` akan memungkinkan analisis CV dalam Bahasa Indonesia atau bahasa lain.

- **Input non-PDF** — Mendukung format `.docx`, `.txt`, dan paste teks langsung tanpa upload file, serta scraping otomatis dari platform seperti LinkedIn.

- **Explainability yang lebih baik** — Menampilkan tidak hanya skor akhir, tapi juga reasoning di balik setiap match — misalnya menunjukkan secara visual mengapa "TensorFlow" dipasangkan dengan "deep learning framework" dengan skor 87%.

- **Evaluasi skala besar** — Membangun ground truth dataset yang lebih besar (100+ pasangan CV-JD berlabel) untuk menghasilkan metrik evaluasi yang lebih robust dan dapat dipublikasikan.

---

## Tech Stack

- **NLP Core** — spaCy `en_core_web_md`, Sentence-Transformers, NLTK (stopwords, WordNetLemmatizer)
- **Machine Learning** — Scikit-learn (TF-IDF, cosine similarity), PyTorch
- **Text Repair** — ftfy, unicodedata
- **PDF Processing** — PyPDF2
- **Fuzzy Matching** — RapidFuzz
- **Interface** — Streamlit
- **Data** — Pandas, NumPy

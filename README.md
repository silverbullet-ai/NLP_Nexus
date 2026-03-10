
# 🧠 NLP Nexus

NLP Nexus is a **Natural Language Processing (NLP) web application** designed to simplify text analysis and document understanding.
It allows users to summarize large text documents, perform sentiment analysis, and visualize text data using word clouds.

The application provides a simple web interface where users can paste text or upload PDF documents and instantly analyze the content.

---

## 🚀 Features

### 📄 Text Summarization
Generate concise summaries from long documents by extracting the most important sentences.

### 😊 Sentiment Analysis
Analyze text to determine its emotional tone:
- Positive
- Negative
- Neutral

### 📊 Word Cloud Generation
Visualize frequently occurring words in the text to quickly understand key themes.

### 📑 PDF Text Extraction
Upload PDF documents and extract text automatically for further analysis.

### 🌐 Web Interface
A simple and interactive UI built with **Flask** for easy text analysis.

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask

**NLP Libraries**
- NLTK
- TextBlob

**Visualization**
- WordCloud
- Matplotlib

**Utilities**
- NumPy
- PyPDF2

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/silverbullet-ai/NLP_Nexus.git
cd NLP_Nexus
```
---

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS
```bash
source venv/bin/activate
```
---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
---

### 4️⃣ Download required NLTK resources

```bash
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
python -m nltk.downloader vader_lexicon
```
---

## ▶️ Running the Application

Start the Flask server:

```bash
python src/app.py
```

Then open your browser and go to:

```bash
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```bash
NLP_Nexus
│
├── src
│   ├── app.py                # Flask application
│   ├── summarizer.py         # NLP processing logic
│   ├── pdf_extractor.py      # PDF text extraction
│   │
│   ├── templates             # HTML templates
│   │   ├── index.html
│   │   ├── result.html
│   │   └── result1.html
│   │
│   └── static
│       ├── css
│       │   ├── style.css
│       │   └── styles.css
│       │
│       └── images
│           ├── bg.jpg
│           └── icons.jpg
│
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements (v2)

- Download generated word clouds
- Copy summary button
- Improved NLP models
- More visualizations
- Enhanced UI/UX

---

## 👨‍💻 Author

**Aahish**

GitHub: https://github.com/silverbullet-ai

---

⭐ If you like this project, consider giving it a star on GitHub!

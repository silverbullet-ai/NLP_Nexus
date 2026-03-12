
# 🧠 NLP Nexus

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-green)
![NLP](https://img.shields.io/badge/NLP-Text_Analysis-orange)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

NLP Nexus is a Natural Language Processing (NLP) web application designed to simplify text analysis and document understanding.

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
```

```bash
cd NLP_Nexus
```
---

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```
or

```bash
py -3.11 -m venv venv
```
Activate it:

Windows (PowerShell / Command Prompt / Windows Terminal)
```bash
venv\Scripts\activate
```

Git Bash
```bash
source venv/Scripts/activate
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
````

```bash
python -m nltk.downloader stopwords
```

```bash
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
├── src	                       # Application source code
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
├── .gitignore                # Git ignored files
├── LICENSE                   # MIT License
├── requirements.txt
└── README.md
```
---

## 👨‍💻 Author

**silverbullet-ai(Aahish)**

GitHub: https://github.com/silverbullet-ai

---
## 🐍 Python Version

This project was developed and tested using:

Python **3.11**

Using Python 3.11 is recommended for compatibility with the dependencies.

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub!

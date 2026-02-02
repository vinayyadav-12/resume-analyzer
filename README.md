# 🧠 AI Resume Analyzer & Job Matcher

A production‑ready **LLM‑powered application** that analyzes a resume against a job description and provides a **match score, skill gap analysis, ATS keyword insights, and improvement suggestions**.

This project demonstrates **real‑world use of Large Language Models (LLMs)** with clean frontend–backend separation, structured outputs, and prompt engineering best practices.

---

## 🚀 Features

* 📄 Resume upload (PDF / DOCX)
* 🧾 Job description analysis
* 📊 Match score (0–100)
* ✅ Matched skills extraction
* ❌ Missing skills detection
* 🏷️ Role level classification (Fresher / Junior / Senior)
* 🔑 ATS keyword gap analysis
* 🧠 AI‑generated resume improvement suggestions

---

## 🏗️ Architecture Overview

```
Frontend (Streamlit UI)
        ↓
Backend (Python Logic)
        ↓
Prompt Engineering + LLM
        ↓
Structured JSON Output (Pydantic)
```

The project follows **industry‑standard modular design** for scalability and maintainability.

---

## 🛠️ Tech Stack

| Layer             | Technology                   |
| ----------------- | ---------------------------- |
| Frontend          | Streamlit                    |
| Backend           | Python                       |
| LLM Orchestration | LangChain (v1.x)             |
| LLM Provider      | OpenAI / Groq (configurable) |
| Output Validation | Pydantic                     |
| File Parsing      | pdfplumber, python‑docx      |

---

## 📁 Project Structure

```
resume_analyzer/
│
├── app.py                     # Streamlit frontend (entry point)
├── requirements.txt
│
├── utils/
│   ├── extract_text.py        # PDF / DOCX text extraction
│   ├── cleaner.py             # Text preprocessing
│   ├── prompt.py              # System prompt
│   ├── llm_runner.py          # LLM invocation logic
│
├── models/
│   └── schema.py              # Pydantic output schema
│
├── sample/                    # Sample data for testing & demo
│   ├── resume.pdf
│   └── jd.txt
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

```bash
export OPENAI_API_KEY="your_api_key"
```

(Windows PowerShell)

```powershell
setx OPENAI_API_KEY "your_api_key"
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🧪 Testing Without UI (Backend‑Only)

You can test the backend logic directly using the `sample/` files:

```python
from utils.extract_text import extract_pdf_text
from utils.llm_runner import analyze_resume

resume = extract_pdf_text("sample/resume.pdf")
with open("sample/jd.txt") as f:
    jd = f.read()

result = analyze_resume(resume, jd)
print(result)
```

This helps in **faster debugging and reproducible results**.

---

## 📦 Example Output

```json
{
  "match_score": 82,
  "matched_skills": ["Python", "SQL", "Machine Learning"],
  "missing_skills": ["AWS", "Docker"],
  "role_level": "Junior",
  "resume_improvements": [
    "Add measurable achievements",
    "Include cloud‑related experience"
  ],
  "ats_keywords_missing": ["CI/CD", "Microservices"]
}
```

---

## 🧠 Key Engineering Highlights

* ✅ Prompt‑driven structured outputs (JSON‑safe)
* ✅ Pydantic schema validation
* ✅ Clean frontend–backend separation
* ✅ LangChain 1.x compatible (`invoke()` based)
* ✅ Easily extendable to RAG, embeddings, or APIs

---

## 🔮 Future Enhancements

* 🔢 Embedding‑based similarity scoring
* ✍️ Resume auto‑rewrite using JD keywords
* 📄 Export analysis report as PDF
* 🔐 User authentication
* 🌐 FastAPI backend + React frontend

---

## 💼 Use Cases

* Job seekers optimizing resumes
* Career portals
* HR tech tools
* EdTech platforms
* AI portfolio / final‑year project

---

## 📜 License

This project is open‑source and available under the MIT License.

---

## 🙌 Author

**Vinaykumar Yadav**
Engineering Student | AI & LLM Enthusiast

---

⭐ If you find this project useful, consider giving it a star!

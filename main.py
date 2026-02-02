import streamlit as st

from utils.extract_text import extract_pdf_text, extract_docx_text
from utils.cleaner import clean_text
from utils.llm_call import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("🧠 AI Resume Analyzer & Job Matcher")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and jd_text:
        if resume_file.name.endswith(".pdf"):
            resume_text = extract_pdf_text(resume_file)
        else:
            resume_text = extract_docx_text(resume_file)

        resume_text = clean_text(resume_text)
        jd_text = clean_text(jd_text)

        result = analyze_resume(resume_text, jd_text)

        st.metric("Match Score", f"{result.match_score}%")

        st.subheader("✅ Matched Skills")
        st.write(result.matched_skills)

        st.subheader("❌ Missing Skills")
        st.write(result.missing_skills)

        st.subheader("📌 Resume Improvements")
        st.write(result.resume_improvements)

        st.subheader("🔑 ATS Keywords Missing")
        st.write(result.ats_keywords_missing)
    else:
        st.warning("Please upload resume and paste job description")

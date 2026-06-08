import streamlit as st
from parser import extract_text_from_pdf
from llm_engine import analyze_resume
from embeddings import calculate_similarity

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and jd_text:

        resume_text = extract_text_from_pdf(uploaded_file)

        st.subheader("🔍 Similarity Score")
        score = calculate_similarity(resume_text, jd_text)
        st.write(f"{score}% match")

        st.subheader("🤖 AI Analysis")
        result = analyze_resume(resume_text, jd_text)
        st.write(result)

    else:
        st.warning("Please upload resume and enter JD")
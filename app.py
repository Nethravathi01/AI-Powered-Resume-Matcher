
import streamlit as st
from matcher_v3 import calculate_tfidf_score, calculate_sentence_similarity, extract_keywords, recommend_skills
from report_generator import generate_pdf_report
import PyPDF2

def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        try:
            text += page.extract_text()
        except:
            pass
    return text

st.title("Resume Matcher V3")
st.markdown("Features: TF-IDF Score | Sentence Similarity | Skill Gaps | PDF Report")

resume_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])
job_desc = st.text_area("Paste the Job Description")

if st.button("Match Now"):
    if resume_file and job_desc:
        if resume_file.type == "application/pdf":
            resume_text = read_pdf(resume_file)
        else:
            resume_text = resume_file.read().decode("utf-8")



        score = calculate_tfidf_score(resume_text, job_desc)
        sim_score = calculate_sentence_similarity(resume_text, job_desc)

        resume_keywords = extract_keywords(resume_text)
        jd_keywords = extract_keywords(job_desc)
        matched = list(set(resume_keywords) & set(jd_keywords))
        missing = recommend_skills(jd_keywords, resume_keywords)

        st.success(f"TF-IDF Match Score: {score}%")
        st.info(f"Sentence Similarity Score: {sim_score}%")

        st.markdown(f"**Resume Keywords:** {resume_keywords}")
        st.markdown(f"**JD Keywords:** {jd_keywords}")
        st.markdown(f"**Matched:** {matched}")
        st.markdown(f"**Missing Skills (Recommended):** {missing}")

        report_path = generate_pdf_report(score, sim_score, resume_keywords, jd_keywords, matched, missing)
        with open(report_path, "rb") as file:
           st.download_button("Download Match Report PDF", data=file, file_name="match_report.pdf")
    else:
           st.warning("Upload resume and paste job description")

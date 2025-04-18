# AI Powered Resume Matcher  
(Python | Streamlit | NLTK | scikit-learn | Sentence-BERT)

This project is a smart Resume Matcher tool designed to help job seekers evaluate how well their resume aligns with a specific job description.
Built using Python and Streamlit, the application leverages AI and NLP techniques like TF-IDF and Sentence-BERT to score and suggest improvements.

## Features
- TF-IDF Matching Score: Measures textual similarity between resume and JD.
- Sentence Similarity: Uses Sentence-BERT to analyze semantic similarity.
- Keyword Extraction: Identifies top keywords from both resume and JD.
- Skill Gap Analysis: Recommends missing skills based on JD comparison.
- PDF Match Report: Generates a downloadable summary report.

## Tech Stack
- Python
- Streamlit
- NLTK
- scikit-learn
- Sentence-Transformers
- FPDF
- PyPDF2

## How to Run
1. Clone or download the repository.
2. Install dependencies:pip install -r requirements.txt.
3. Run the app: streamlit run app.py.

## Project Files
- `app.py` – Streamlit UI and flow
- `matcher_v3.py` – Matching logic and keyword analysis
- `report_generator.py` – PDF report creation
- `requirements.txt` – Required libraries

## Use Case
Helpful for job seekers, resume reviewers, and career coaches to evaluate and improve resume relevance for a given role.

 

from fpdf import FPDF

def generate_pdf_report(score, sim_score, resume_keywords, jd_keywords, matched, missing):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Resume Match Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"TF-IDF Match Score: {score}%", ln=True)
    pdf.cell(200, 10, txt=f"Sentence Similarity Score: {sim_score}%", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Resume Keywords:", ln=True)
    pdf.multi_cell(0, 10, txt=", ".join(resume_keywords))

    pdf.cell(200, 10, txt="JD Keywords:", ln=True)
    pdf.multi_cell(0, 10, txt=", ".join(jd_keywords))

    pdf.cell(200, 10, txt="Matched Keywords:", ln=True)
    pdf.multi_cell(0, 10, txt=", ".join(matched))

    pdf.cell(200, 10, txt="Missing Skills (Recommended to Add):", ln=True)
    pdf.multi_cell(0, 10, txt=", ".join(missing))

    file_path = "match_report.pdf"
    pdf.output(file_path)
    return file_path

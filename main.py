import streamlit as st
import docx2txt
from fpdf import FPDF

def convert_to_pdf():
    f = open("data.txt", "r")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for x in f:
        pdf.multi_cell(190 ,10, x,align="L")
    pdf.output("example.pdf")
    with open("example.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    return PDFbyte

st.title("File Upload")
st.subheader("DocumentFiles")
docx_file = st.file_uploader("Upload Document", type=["docx"])
if docx_file is not None:
    file_name = docx_file.name
    size = len(file_name)
    file_name = file_name[:size-5]
    st.write(file_name)
    raw_text = docx2txt.process(docx_file)
    txt = st.text_area('Text in file', raw_text)
    hi = st.button("Convert to PDF")
    if hi:
        text = txt.encode('latin-1', 'replace').decode('latin-1')
        file = open("data.txt","w")
        file.write(text)
        file.close()
        pdf = convert_to_pdf()
        st.download_button(label="Download PDF", 
                data = pdf,
                file_name=file_name + ".pdf",
                mime='application/octet-stream')

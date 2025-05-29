import streamlit as st
from pdf_utils import extract_text_from_pdf
from gemini_api import get_insights_from_text

st.set_page_config(page_title="PDF Insight Bot", page_icon="📄")
st.title("📄 PDF Insight Bot - Mini Analyst")
st.caption("Upload a PDF to get smart summaries and insights using AI")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF loaded! Generating insights...")

    with st.spinner("Talking to Gemini AI..."):
        insights = get_insights_from_text(extracted_text)

    st.subheader("🔍 Insights from PDF:")
    st.markdown(insights)

    if st.button("Download Insights"):
        st.download_button(
            label="Download as .txt",
            data=insights,
            file_name="pdf_insights.txt",
            mime="text/plain"
        )

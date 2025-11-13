import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from extractor import extract_pollution_data

load_dotenv()

st.set_page_config(page_title="Pollution Data Extractor for UPSC Prep", layout="wide")
st.title("📰 Environmental Pollution Data Extractor for UPSC Prep")
st.write("Paste a news article about environmental pollution in India, or upload a `.txt`/`.pdf` file. The app will extract structured information and allow you to download the results as CSV for your notes.")

input_choice = st.radio("Choose input method:", ("Paste article text", "Upload file"))

article_text = ""
if input_choice == "Paste article text":
    article_text = st.text_area("Paste the full article text here:", height=300)
else:
    uploaded_file = st.file_uploader("Upload article file", type=["txt","pdf"])
    if uploaded_file is not None:
        try:
            if uploaded_file.type == "application/pdf":
                import PyPDF2
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                pages = [page.extract_text() for page in pdf_reader.pages]
                article_text = "\n".join(pages)
            else:
                article_text = uploaded_file.getvalue().decode("utf-8")
        except Exception as e:
            st.error(f"Could not read file: {e}")

if st.button("Extract Structured Data"):
    if not article_text.strip():
        st.warning("Please provide article text (via paste or upload) before clicking the button.")
    else:
        with st.spinner("Extracting…"):
            try:
                result = extract_pollution_data(article_text)
                st.subheader("Extracted JSON")
                st.json(result)

                df = pd.DataFrame([result])
                st.subheader("Tabular View")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download extracted data as CSV",
                    data=csv,
                    file_name="extracted_pollution_data.csv",
                    mime="text/csv"
                )

                st.subheader("Key Parts for UPSC Notes")
                for key, val in result.items():
                    st.write(f"**{key}:** {val}")

            except Exception as e:
                st.error(f"Extraction failed: {e}")

st.markdown("---")
st.write(
    "This tool helps you pick out key factual information from pollution-related news — location, pollutant, data values, impacts, policy actions — especially useful for your UPSC environment preparations."
)


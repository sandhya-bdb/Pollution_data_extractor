# 📰 Pollution Data Extractor for UPSC Preparation

A web-tool that takes any news article or PDF on environmental pollution in India, and transforms it into structured, exam-ready data — perfect for UPSC aspirants and environmental-policy enthusiasts.

## 🔍 Why This Project

During a previous project building a financial-data extractor app, I realised something: while we have many tools for finance and business, there were **no easy tools** tailored for extracting pollution and environment-related data aligned with UPSC preparation.  
As someone who studied for UPSC and also mentored aspirants, I created this tool to bridge that gap.

## 🎯 Features

- Paste or upload a news article / PDF about pollution in India  
- Extracted information includes: title, location, pollutant type, source, data values or standards, impacts, policy actions, key points  
- View the extracted data in JSON and table format  
- Download the structured result as CSV for your revision notes  
- Simple, clean interface made with Streamlit

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- The project uses packages such as: `streamlit`, `pandas`, `PyPDF2` (for PDF reading)  
- (Any other library you're using, e.g. langchain/groq etc.)

### Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   python -m venv venv
   source venv/bin/activate   # on Unix/macOS  
   venv\Scripts\activate      # on Windows
2. pip install -r requirements.txt
3. streamlit run app.py
### Project Structure
    /<repo-name>
    │
    ├── app.py            # Streamlit frontend
    ├── extractor.py      # Logic to extract pollution-data from text
    ├── requirements.txt  # Python dependencies
    ├── README.md         # This file
    └── …                 # (Any other modules, assets, docs)

### 🙌 Future Enhancements

Visualisation of pollution hotspots and trends

Multilingual support (e.g., Hindi, Assamese)

Integration with official datasets (e.g., CPCB, MoEFCC)

More refined policy-action extraction and summaries

### 🧑‍💼 Contribution

I welcome feedback, ideas and collaboration! If you find a bug or have a feature suggestion, feel free to open an issue or submit a pull request.

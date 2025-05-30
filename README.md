# PDF Insight Bot

PDF Insight Bot is a tool designed to extract, analyze, and summarize information from PDF documents using AI-powered techniques.
> **Note:** PDF Insight Bot uses the Gemini API for AI-powered PDF analysis and summarization. Make sure you have a valid Gemini API key to use all features.

## Features

- Extracts text and metadata from PDF files
- Summarizes document content
- Answers questions based on PDF content
- Supports batch processing of multiple PDFs

## Installation

```bash
git clone https://github.com/IamMoosa/pdf_insight_bot.git
cd pdf_insight_bot
pip install -r requirements.txt
```

## Configuration

Before running the app, create a `.env` file in the project root and add your API key:

```
GEMINI_API_KEY=your_openai_api_key_here
```
## Running the App

To launch the PDF Insight Bot using Streamlit, run:

```bash
streamlit run app.py
```

This will open the app in your default web browser.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
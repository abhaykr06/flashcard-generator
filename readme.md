# LLM-Powered Flashcard Generator

Generate flashcards (Q&A) from any educational material using LLMs.

## Features
- Upload .txt or .pdf
- Paste educational content
- Automatically generate flashcards using GPT-3.5

## Setup
```bash
git clone <repo-url>
cd flashcard-generator
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py

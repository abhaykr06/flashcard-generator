📚 LLM-Powered Flashcard Generator
A lightweight and intelligent flashcard generation tool that uses Gemini AI to convert educational content into question-answer flashcards. Designed for students, educators, and self-learners, this app helps break down learning materials into digestible pieces quickly and efficiently.

🚀 Features
✅ Upload .txt or .pdf educational files

✅ Paste custom text directly

✅ Choose subject type to tailor flashcards

✅ Generate 10–15 fact-based flashcards per input

✅ View and expand each Q&A

✅ Download flashcards as .json or .csv

✅ Gemini-powered LLM integration

✅ Clean and responsive Streamlit UI

🖼️ Demo Preview
Example coming soon (screenshot of output UI with flashcards)

🧠 How It Works
User Input: Upload a file or paste educational content.

Text Extraction: Extracts raw text from uploaded .txt or .pdf files.

LLM Integration: Sends the content to Gemini with a well-crafted prompt.

Output: Renders flashcards (Q&A) on the UI.

Export: Download results in preferred format.

🛠️ Tech Stack
Component	Tool / Framework
Language	Python
UI Framework	Streamlit
LLM API	Google Gemini (via google.generativeai)
PDF Handling	PyMuPDF (fitz)
Export Format	json, csv

📂 Project Structure
bash
Copy
Edit
flashcard-generator/
├── app.py
├── .env
├── requirements.txt
├── utils/
│   ├── llm_interface.py
│   └── text_extractor.py

🧪 Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/flashcard-generator.git
cd flashcard-generator
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add Gemini API Key

Create a .env file in the root:

bash
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
Run the App

bash
Copy
Edit
streamlit run app.py

📦 Example Output
json
Copy
Edit
[
  {
    "question": "What is the purpose of the operating system?",
    "answer": "The operating system manages hardware and software resources, providing services to computer programs."
  },
  ...
]

🏆 Deliverables
✅ Fully working app with Gemini integration

✅ Flashcard output preview

✅ JSON + CSV export functionality

✅ UI built with Streamlit

✅ Public GitHub repository

📌 Notes
This project uses Gemini API, which may require token limits or model access.

You can easily switch to other LLMs (e.g., HuggingFace Flan-T5) by replacing the llm_interface.py logic.

![alt text](image.png)

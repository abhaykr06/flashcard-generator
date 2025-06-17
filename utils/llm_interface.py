'''from transformers import pipeline

def generate_flashcards(text, subject="General"):
    prompt = f"Generate 10 question-answer flashcards for the following {subject} content:\n\n{text[:2000]}"

    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)
    result = qa_pipeline(prompt)[0]["generated_text"]

    flashcards = []
    lines = result.split('\n')
    for line in lines:
        if "Q:" in line and "A:" in line:
            try:
                q = line.split("Q:")[1].split("A:")[0].strip()
                a = line.split("A:")[1].strip()
                flashcards.append({"question": q, "answer": a})
            except:
                continue
    return flashcards'''
# llm_interface.py
import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_flashcards(text, subject):
    prompt = f"""
You are a helpful assistant that creates flashcards.

Generate 10-15 flashcards from the following {subject} text. 
Each flashcard must be in JSON format like this:
[
  {{
    "question": "What is X?",
    "answer": "X is ..."
  }},
  ...
]

Only return the JSON array. Text:
{text}
    """.strip()

    try:
        model = genai.GenerativeModel("models/gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Could not generate flashcards. Error: {str(e)}"

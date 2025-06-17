'''import streamlit as st
import json
from utils.text_extractor import extract_text_from_txt, extract_text_from_pdf
from utils.llm_interface import generate_flashcards
import pandas as pd

st.set_page_config(page_title="Flashcard Generator", layout="centered")

st.title("📚 Free LLM-Powered Flashcard Generator")
st.markdown("Generate smart flashcards from your notes using a completely free AI model (FLAN-T5)!")

subject = st.selectbox("📘 Choose Subject Type", ["General", "Biology", "Physics", "History", "Computer Science"])

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
text_input = st.text_area("✍️ Or paste your content here:")

# Extract text from file or textarea
if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        extracted_text = extract_text_from_txt(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(uploaded_file)
    else:
        extracted_text = "Unsupported file format."
elif text_input:
    extracted_text = text_input
else:
    extracted_text = ""

# Preview extracted text
if extracted_text:
    st.subheader("📄 Extracted Text Preview")
    st.text_area("Extracted Content", extracted_text[:3000], height=300)

if st.button("⚡ Generate Flashcards"):
    if not extracted_text:
        st.warning("Please upload or enter content.")
    else:
        with st.spinner("Generating flashcards using FLAN-T5..."):
            flashcards = generate_flashcards(extracted_text, subject)

            if not flashcards:
                st.error("❌ Could not generate flashcards. Try with more text.")
            else:
                st.subheader("📋 Generated Flashcards")
                for i, card in enumerate(flashcards, 1):
                    with st.expander(f"Flashcard {i}"):
                        st.markdown(f"**Q:** {card['question']}")
                        st.markdown(f"**A:** {card['answer']}")

                # Export options
                st.subheader("📥 Export Flashcards")

                st.download_button(
                    "Download as JSON",
                    data=json.dumps(flashcards, indent=2),
                    file_name="flashcards.json",
                    mime="application/json"
                )

                df = pd.DataFrame(flashcards)
                st.download_button(
                    "Download as CSV",
                    data=df.to_csv(index=False),
                    file_name="flashcards.csv",
                    mime="text/csv"
                )'''
import streamlit as st
import json
from utils.text_extractor import extract_text_from_txt, extract_text_from_pdf
from utils.llm_interface import generate_flashcards
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Flashcard Generator", layout="centered")

st.title("📚 LLM-Powered Flashcard Generator")
st.markdown("Upload your educational content or paste text to generate intelligent flashcards using Gemini AI.")

# Subject type for prompt conditioning
subject = st.selectbox("📘 Choose Subject Type", ["General", "Biology", "Physics", "History", "Computer Science"])

# Input: File Upload or Text
uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
text_input = st.text_area("✍️ Or paste your content here:")

# Extract text based on input method
if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        extracted_text = extract_text_from_txt(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(uploaded_file)
    else:
        extracted_text = "Unsupported file format."
elif text_input:
    extracted_text = text_input
else:
    extracted_text = ""

# Show extracted content preview
if extracted_text:
    st.subheader("📄 Extracted Text Preview")
    st.text_area("Extracted Content", extracted_text[:3000], height=300)

# Flashcard Generation Button
if st.button("⚡ Generate Flashcards"):
    if not extracted_text:
        st.warning("Please upload a file or paste some text.")
    else:
        with st.spinner("Generating flashcards using Gemini..."):
            flashcard_output = generate_flashcards(extracted_text, subject)

            try:
                flashcards = json.loads(flashcard_output)
                flashcards = flashcards[:15]  # Cap to 15 max
                st.subheader("📋 Generated Flashcards")

                for i, card in enumerate(flashcards, 1):
                    with st.expander(f"Flashcard {i}"):
                        st.markdown(f"**Q:** {card['question']}")
                        st.markdown(f"**A:** {card['answer']}")
                        st.checkbox("Mark this flashcard for edit", key=f"edit_{i}")

                # -------- EXPORT SECTION --------
                st.subheader("📥 Export Flashcards")

                # Convert to JSON
                json_data = json.dumps(flashcards, indent=2)
                st.download_button(
                    label="Download as JSON",
                    data=json_data,
                    file_name="flashcards.json",
                    mime="application/json"
                )

                # Convert to CSV
                import pandas as pd
                df = pd.DataFrame(flashcards)
                csv_data = df.to_csv(index=False)

                st.download_button(
                    label="Download as CSV",
                    data=csv_data,
                    file_name="flashcards.csv",
                    mime="text/csv"
                )

            except json.JSONDecodeError:
                st.error("❌ Gemini did not return valid JSON. Showing raw output:")
                st.text_area("Raw Output", flashcard_output, height=300)


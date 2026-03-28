# Academic-Humanizer
AI generated text humanizer
# 🏛️ The Scholar's Refiner: Theology & Philosophy Edition

An elite AI-powered text humanizer designed to transform sterile AI prose into authentic, PhD-level academic writing. Engineered specifically to bypass advanced detectors like **GPTZero** and **Turnitin**.

## 🧠 The Philosophy of the App
Standard AI (GPT-4, Claude) writes with "Mathematical Predictability." This app uses a multi-layered pipeline to disrupt that predictability:
1. **Linguistic Re-structuring:** Using PhD-level system prompts to vary sentence length (Burstiness).
2. **Lexical Scrambling:** Using NLTK and WordNet to swap predictable adjectives for rare academic synonyms (Perplexity).
3. **Deterministic Cleaning:** A regex-based "Cliche Sweeper" to remove AI fingerprints like "tapestry" or "delve."

## 🚀 Quick Start
1. **Install Dependencies:**
   ```bash
   pip install streamlit langchain_openai spacy nltk
   python -m spacy download en_core_web_sm

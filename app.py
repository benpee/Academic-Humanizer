---

### 📂 File 2: `app.py` (The Complete, Integrated Solution)

This script contains the UI, the Master Prompt, and the NLP Post-Processing Jitter.

```python
import streamlit as st
import os
import re
import random
import spacy
import nltk
from nltk.corpus import wordnet
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# --- 1. CONFIGURATION & NLP SETUP ---
try:
    nlp = spacy.load("en_core_web_sm")
except:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

nltk.download('wordnet')
nltk.download('omw-1.4')

# --- 2. THE "SECRET SAUCE" POST-PROCESSING ---

def regex_cliche_sweeper(text):
    """Deterministic removal of AI hallmarks."""
    cliche_map = {
        r'\bdelve\b': 'examine',
        r'\btapestry\b': 'interweaving',
        r'\bin conclusion\b': 'ultimately',
        r'\bmoreover\b': 'further',
        r'\bultimately\b': 'in the final analysis',
        r'\ba testament to\b': 'evidence of',
        r'\bcrucial\b': 'pivotal',
        r'\bvital\b': 'essential',
        r'\bnuanced\b': 'subtle',
        r'\blandscape\b': 'milieu'
    }
    for pattern, replacement in cliche_map.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def inject_perplexity(text, substitution_rate=0.04):
    """Randomly swaps adjectives for less predictable synonyms."""
    doc = nlp(text)
    words = []
    # Avoid swapping core technical terms to maintain academic integrity
    protected = {'god', 'being', 'essence', 'grace', 'faith', 'logic', 'ethics'}
    
    for token in doc:
        if (token.pos_ in ['ADJ', 'ADV'] and token.text.lower() not in protected and random.random() < substitution_rate):
            syns = wordnet.synsets(token.text)
            if syns:
                synonyms = [l.name() for l in syns[0].lemmas() if l.name().lower() != token.text.lower()]
                if synonyms:
                    words.append(random.choice(synonyms).replace('_', ' ') + token.whitespace_)
                    continue
        words.append(token.text_with_ws)
    return "".join(words)

def get_humanity_score(text):
    """Calculates Burstiness (Std Dev of sentence lengths)."""
    doc = nlp(text)
    lengths = [len(sent.text.split()) for sent in doc.sents]
    if len(lengths) < 2: return 0
    mean = sum(lengths) / len(lengths)
    std_dev = (sum((x - mean) ** 2 for x in lengths) / len(lengths)) ** 0.5
    return round(std_dev, 2)

# --- 3. THE LLM ORCHESTRATION ---

def humanize_prose(input_text, level, tone, api_key):
    llm = ChatOpenAI(temperature=0.88, model_name="gpt-4o", openai_api_key=api_key)
    
    # Master PhD-Level Prompt
    template = """
    You are an elite, PhD-level Academic Editor specializing in Theology and Philosophy. 
    Rewrite the text to read organically, reflecting the messy, nuanced cognitive processes of a human scholar.

    DIRECTIVES:
    - Maximize Burstiness: Radically vary sentence lengths (3-word punchy vs 30-word multi-clause).
    - Maximize Perplexity: Use high-level terminology. Avoid standard AI transitions.
    - Authentic Hedging: Use phrases like 'One might venture to suggest', 'There is a palpable tension'.
    
    CONSTRAINTS:
    - Level {level}: {level_desc}
    - Tone: {tone}
    - Forbidden words: delve, tapestry, moreover, furthermore, in conclusion.

    Original Text: {input_text}
    """
    
    descriptions = {
        "Diploma": "Clear terminology, sound grammar, basic power verbs.",
        "Degree": "Complex structures, standard jargon (epistemology, exegesis), advanced verbs.",
        "Master's": "Highly sophisticated, dense prose, expert power verbs, nested clauses."
    }

    prompt = PromptTemplate(input_variables=["level", "level_desc", "tone", "input_text"], template=template)
    chain = prompt | llm
    return chain.invoke({"level": level, "level_desc": descriptions[level], "tone": tone, "input_text": input_text}).content

# --- 4. STREAMLIT UI ---

st.set_page_config(page_title="Scholar Refiner", layout="wide")
st.title("🏛️ The Scholar's Refiner")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    jitter = st.slider("Jitter (Perplexity) Intensity", 0.0, 0.1, 0.04)
    st.info("High jitter increases perplexity but may slightly alter flow.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Source Text")
    user_input = st.text_area("Paste AI-Generated Text:", height=350)
    level = st.selectbox("Academic Level:", ["Diploma", "Degree", "Master's"])
    tone = st.selectbox("Tone:", ["Academic", "Polemical", "Personal", "Warm"])

with col2:
    st.subheader("Humanized Result")
    if st.button("Humanize & Scramble"):
        if not api_key: st.error("API Key Required")
        else:
            with st.spinner("Applying PhD-level humanization..."):
                # Phase 1: LLM Logic
                output = humanize_prose(user_input, level, tone, api_key)
                # Phase 2: Regex Clean
                output = regex_cliche_sweeper(output)
                # Phase 3: NLP Jitter
                output = inject_perplexity(output, substitution_rate=jitter)
                
                st.text_area("Final Output:", value=output, height=350)
                
                # Metrics
                score = get_humanity_score(output)
                st.metric("Burstiness Score", score)
                if score > 12: st.success("✅ High Burstiness: Statistically Human.")
                else: st.warning("⚠️ Low Burstiness: AI may be detected.")

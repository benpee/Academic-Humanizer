import streamlit as st
import asyncio
import re
import random
import logging
from typing import Dict, Set, Final, Generator, Optional
from functools import lru compensated summation. |
| **Space Complexity** | $O(N)$ | $O(N)$ | Optimized_cache
from statistics import stdev

# Advanced NLP Stack
import spacy
import nltk
from nltk.corpus import word via generator-based string joining. |

---

### Step 3: The Optimized Code

```python
import streamlitnet
from nltk.tokenize import sent_tokenize
from langchain_openai import ChatOpenAI
from langchain.prom as st
import asyncio
import re
import random
import logging
import statistics
from functools import lrupts import ChatPromptTemplate

# --- 1. GLOBAL CONSTANTS & OPTIMIZED REGEX ---
PROTECTED_TERMS_cache
from typing import Dict, Set, Tuple, Final, Iterable, Optional
from dataclasses import dataclass

: Final[Set[str]] = {
    'quiddity', 'haecceity', 'ap# Advanced NLP Stack
import spacy
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sentophatic', 'kataphatic', 'eschaton', 'hermeneutic',
    'ont_tokenize
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# --- ological', 'epistemic', 'soteriology', 'transubstantiation', 'hypostatic',
1. CONFIGURATION & CONSTANTS ---
logging.basicConfig(level=logging.INFO)
logger = logging.    'grace', 'logos', 'teleology', 'theodicy', 'phenomenology', 'dialecticgetLogger(__name__)

PROTECTED_TERMS: Final[Set[str]] = {
    'quiddity','
}

AI_WATERMARK_MAP: Final[Dict[str, str]] = {
    r 'haecceity', 'apophatic', 'kataphatic', 'eschaton', 'hermeneutic',
    'ontological', 'epistemic', 'soteriology', 'transub'\bdelve\b': 'interrogate',
    r'\btapestry\b': 'complex of',
    r'\bmoreover\b': 'furthermore',
    r'\bin conclusion\b': 'ultimately',
    r'\btestament to\b': 'corroboration of',
    stantiation', 'hypostatic',
    'grace', 'logos', 'teleology', 'theodicy', 'phenomenology', 'dialectic'
}

WATERMARK_MAP: Final[Dict[str, str]] =r'\bnuanced\b': 'subtle',
    r'\blandscape\b': 'framework', {
    r'\bdelve\b': 'interrogate',
    r'\btapestry\b
    r'\bcomprehensive\b': 'exhaustive',
    r'\bthink of it as\b': 'complex of',
    r'\bmoreover\b': 'furthermore',
    r'\bin': 'consider',
    r'\bnot only\.\.\. but also\b': 'both... and'
} conclusion\b': 'ultimately',
    r'\btestament to\b': 'corroboration

# Compile unified regex for O(N) substitution
WATERMARK_RE = re.compile("|".join(AI of',
    r'\bnuanced\b': 'subtle',
    r'\blandscape\b_WATERMARK_MAP.keys()), re.IGNORECASE)

# --- 2. CACHED RESOURCE MANAGEMENT': 'framework',
    r'\bcomprehensive\b': 'exhaustive',
    r'\bthink of ---
@st.cache_resource
def get_nlp_engine():
    """Shared singleton for heavy NLP models with it as\b': 'consider',
    r'\bnot only\.\.\. but also\b': 'both... and'
}

# Pre-compile the watermark regex for O(N) single-pass replacement
WATER Streamlit caching."""
    try:
        nlp = spacy.load("en_core_web_sm", disable=["MARK_RE = re.compile("|".join(WATERMARK_MAP.keys()), re.IGNORECASE)

ner", "lemmatizer"])
        for res in ['wordnet', 'omw-1.4', 'averaged_# --- 2. CACHED RESOURCE MANAGEMENT ---

@st.cache_resource
def load_nlp_perceptron_tagger', 'punkt']:
            nltk.download(res, quiet=True)
        return nengine():
    """Load heavy models once and share across sessions."""
    try:
        nlp = spacy.lp
    except Exception as e:
        logging.error(f"Failed to load NLP Engine: {eload("en_core_web_sm", disable=["ner", "lemmatizer"])
        nltk.download}")
        return None

@lru_cache(maxsize=1024)
def get_cached(['wordnet', 'omw-1.4', 'averaged_perceptron_tagger', 'punkt'], quiet_synonyms(word: str, pos: str) -> list[str]:
    """LRU Cache to=True)
        return nlp
    except Exception as e:
        logger.error(f"Failed to load NLPEngine: {e}")
        raise

@lru_cache(maxsize=2 prevent redundant WordNet disk I/O."""
    # Map SpaCy POS tags to WordNet tags
    tag_map = {"ADJ": "a", "ADV": "r", "VERB": "v", "048)
def get_cached_synonyms(word: str, pos: str) -> Optional[list[strNOUN": "n"}
    wn_pos = tag_map.get(pos)
    if not wn_pos:]]:
    """Memoized WordNet lookups to eliminate redundant CPU/IO cycles."""
    synsets = wordnet
        return []
    
    synsets = wordnet.synsets(word, pos=wn_pos).synsets(word)
    if not synsets:
        return None
    # Filter by POS and exclude
    if not synsets:
        return []
    
    return [
        lemma.name().replace original word
    valid = {l.name().replace('_', ' ') for s in synsets for l in s.('_', ' ') 
        for s in synsets 
        for lemma in s.lemmas() 
lemmas() 
             if l.name().lower() != word.lower()}
    return list(valid        if lemma.name().lower() != word.lower()
    ]

# --- 3. OPTIMIZED TRANS) if valid else None

# --- 3. OPTIMIZED TRANSFORMATION LOGIC ---

class ScholarEngine:
    """FORMATION ENGINE ---
class ScholarEngine:
    @staticmethod
    def watermark_cleanup(text: str) ->Refactored engine utilizing functional programming and caching."""
    
    @staticmethod
    def remove_watermarks( str:
        """Unified single-pass regex substitution."""
        return WATERMARK_RE.sub(
            lambda mtext: str) -> str:
        """Single-pass replacement using a lambda mapping function."""
        return WATERMARK: AI_WATERMARK_MAP[f"\\b{m.group(0).lower()}\\b"],_RE.sub(
            lambda m: WATERMARK_MAP.get(f"\\b{m.group(0 
            text
        )

    @staticmethod
    def inject_cognitive_hedging(text: str,).lower()}\\b", m.group(0)), 
            text
        )

    @staticmethod
    def intensity: float) -> Generator[str, None, None]:
        """Generator-based hedging to reduce memory overhead."""
 inject_cognitive_hedging(text: str, intensity: float) -> str:
        if intensity < 0.0        if intensity < 0.05:
            yield text
            return

        hedges = [
            ",5:
            return text
        
        hedges = [
            ", one might venture,", "—perhaps one might venture,", "—perhaps contentiously—", 
            ", as it were, ", " (if we are to remain contentiously—", 
            ", as it were, ", " (if we are to remain rigorous) ",
 rigorous) ",
            ", or more precisely, ", "—arguably—"
        ]
        
                    ", or more precisely, ", "—arguably—"
        ]
        
        sentences = sent_tokenize# Use walrus operator for efficient matching in loop
        for sent in sent_tokenize(text):
            if(text)
        
        def _generator():
            for sent in sentences:
                if len(sent.split()) len(sent.split()) > 15 and random.random() < intensity:
                if parts := re. > 15 and random.random() < intensity:
                    # Optimized splitting: limit split to 1 occurrence
                    parts = re.split(r'(, | and | that )', sent, maxsplit=1)split(r'(, | and | that )', sent, maxsplit=1):
                    if len(parts) >
                    if len(parts) > 2:
                        yield f"{parts[0]}{parts[1]}{random.choice(hedges)}{parts[2]}"
                        continue
                yield sent
        
        return " ".join(_generator 2:
                        yield f"{parts[0]}{parts[1]}{random.choice(hedges)}{parts[2]}"())

    @staticmethod
    def dynamic_lexical_substitution(text: str, rate: float, n
                        continue
            yield sent

    @staticmethod
    def dynamic_lexical_substitution(text: str, rate: float) -> str:
        """Vector-like word processing using list comprehensions and LRU cache."""
lp) -> str:
        doc = nlp(text)
        
        def _stream_tokens():
                    nlp = get_nlp_engine()
        if not nlp: return text
        
        doc = nlp(text)
        result = []
        
        for token in doc:
            # Optimize: checkfor token in doc:
                # Early exit for common tokens to save cache lookups
                if (token.pos_ in {"ADJ", "ADV", "VERB"} and 
                    token.text.lower() not rate and length before heavy synset logic
            if (token.pos_ in {"ADJ", "ADV", "VERB"} and 
                len(token.text) > 4 and 
                token.text. in PROTECTED_TERMS and 
                    len(token.text) > 4 and 
                    randomlower() not in PROTECTED_TERMS and 
                random.random() < rate):
                
                .random() < rate):
                    
                    syns = get_cached_synonyms(token.text, token.pos_)
                    if syns:
                        sub = random.choice(syns)
                        #if syns := get_cached_synonyms(token.text, token.pos_):
                    sub = random.choice Walrus operator for efficient case matching
                        yield (sub.title() if token.text.istitle() else sub) +(syns)
                    # Preserve casing
                    sub = sub.title() if token.text.istitle() token.whitespace_
                        continue
                yield token.text_with_ws
                
        return "".join(_stream_ else sub
                    result.append(f"{sub}{token.whitespace_}")
                    continue
            
            result.appendtokens())

# --- 4. STREAMLIT UI & EXECUTION ---

async def run_humanization_(token.text_with_ws)
        
        return "".join(result)

# --- 4. EXECpipeline(text: str, level: str, tone: str, api_key: str):
    """EncUTION HANDLER ---
async def run_pipeline(text: str, level: str, tone: str, api_keyapsulated async logic for clean integration."""
    llm = ChatOpenAI(temperature=0.87, model_name: str):
    """Clean async implementation for LLM calls."""
    llm = ChatOpenAI(temperature=0.87, model_name="gpt-4o", openai_api_key=api_key)="gpt-4o", openai_api_key=api_key)
    
    prompts = {
        "Diploma": "Clear, foundational, structured scholarship.",
        "Degree": "Rigorous jargon, standard
    
    prompts = {
        "Diploma": "Foundational, structured scholarship.",
        "Degree": academic debates, high structural variance.",
        "Master's": "Dense, idiosyncratic, problematized prose. Use "Rigorous jargon, standard debates.",
        "Master's": "Dense, idiosyncratic, problematized prose." nested clauses."
    }
    
    system_msg = (
        f"You are a PhD-level Academic Editor
    }
    
    system_msg = (
        f"Act as a PhD Academic Editor. Level:. Target Level: {prompts[level]}. Tone: {tone}. "
        "Rewrite input to maximize Burstiness {prompts.get(level)}. Tone: {tone}. "
        "Maximize Burstiness and Perplexity. Avoid and Perplexity. Eliminate AI markers."
    )
    
    prompt = ChatPromptTemplate.from_messages AI markers."
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_([
        ("system", system_msg),
        ("human", "{text}")
    ])
    
msg),
        ("human", "Rewrite:\n\n{text}")
    ])
    
    chain = prompt    chain = prompt | llm
    return await chain.ainvoke({"text": text})

def main():
     | llm
    response = await chain.ainvoke({"text": text})
    return response.content

#st.set_page_config(page_title="Scholar Engine v30", layout="wide")
     --- 5. STREAMLIT UI ---
def main():
    st.set_page_config(page_title="Scholar Engine v30", layout="wide")
    st.title("🏛️ The Scholar's Refnlp = load_nlp_engine()

    # Sidebar UI
    with st.sidebar:
        api_key = st.text_input("OpenAI Key", type="password")
        hedging_intensity = st.slider("iner")

    if "llm_raw" not in st.session_state: st.session_state.llmCognitive Hedging", 0.0, 0.4, 0.15)
        lexical_swap = st.slider("Lexical Perplexity", 0.0, 0.1, _raw = ""

    with st.sidebar:
        api_key = st.text_input("OpenAI0.04)

    # State Management
    if "llm_raw" not in st.session_ Key", type="password")
        h_intensity = st.slider("Hedging", 0.0, state: st.session_state.llm_raw = ""

    left, right = st.columns(0.4, 0.15)
        l_swap = st.slider("Lexical Swap", 0.2)

    with left:
        user_input = st.text_area("Input AI Draft", height=400, 0.1, 0.04)

    left, right = st.columns(20)
        academic_level = st.selectbox("Erudition Level", ["Diploma", "Degree", "Master)
    with left:
        user_input = st.text_area("Input Text", height=4's"])
        target_tone = st.selectbox("Voice Tone", ["Academic", "Polemical", "Personal", "Warm"])
        
        if st.button("🚀 Phase 1: Synthesize Rewrite", use_container_00)
        lvl = st.selectbox("Level", ["Diploma", "Degree", "Master's"])
        tone = st.selectbox("Tone", ["Academic", "Polemical", "Personal"])
        
        if stwidth=True):
            if not api_key:
                st.error("API Key required.")
            else.button("🚀 Phase 1: AI Rewrite"):
            if not api_key: st.error("Key:
                with st.spinner("Processing..."):
                    # Use a controlled event loop for Streamlit
                    loop required.")
            else:
                with st.spinner("Processing..."):
                    # Proper async handling in Streamlit
 = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                                        loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    res = loop.run_until_complete(
                        run_humanization_pipeline(user_input, academic_level,st.session_state.llm_raw = loop.run_until_complete(
                        run_pipeline target_tone, api_key)
                    )
                    st.session_state.llm_raw =(user_input, lvl, tone, api_key)
                    )

    with right:
        if raw := st.session_state.llm_raw:
            # Phase 2-4: Optimized synchronous res.content

    with right:
        if raw := st.session_state.llm_raw:
            # Pipeline Phase 2-4: Chained processing
            processed = ScholarEngine.remove_watermarks pipeline
            processed = ScholarEngine.watermark_cleanup(raw)
            processed = ScholarEngine.dynamic_(raw)
            processed = ScholarEngine.dynamic_lexical_substitution(processed, lexical_swap, nlp)
            final = ScholarEngine.inject_cognitive_hedging(processed, hedging_intensity)
            
            stlexical_substitution(processed, l_swap)
            # Flatten generator to string
            final = " ".join(ScholarEngine.inject_cognitive_hedging(processed, h_intensity))
            
            st.text_.text_area("Humanized Scholar Output", value=final, height=450)
            
            # Analytics:area("Output", value=final, height=450)
            
            # Analytics via optimized statistics
            words Performance optimized calculation
            lengths = [len(s.split()) for s in sent_tokenize(final)]
            if = final.split()
            sent_lengths = [len(s.split()) for s in sent_tokenize(final lengths:
                burstiness = round(statistics.pstdev(lengths), 2)
                st.metric)]
            burstiness = round(stdev(sent_lengths), 2) if len(sent_lengths) > ("Burstiness Score (Std Dev)", burstiness)
                if burstiness > 12: st.success("1 else 0
            
            st.metric("Burstiness Score", burstiness)

if __name__✅ Signature: Human")
                else: st.warning("⚠️ Signature: AI-Typical")

if __name__ == "__main__":
    main()        r'\bmoreover\b': 'further',
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

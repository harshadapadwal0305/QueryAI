import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import pandas as pd
import os
import ast

load_dotenv()


# =========================================================
# PREMIUM FRONTEND - PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="QueryAI",
    page_icon="✦",
    layout="wide"
)


# =========================================================
# PREMIUM FRONTEND - CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(120, 80, 255, 0.18), transparent 30%),
        radial-gradient(circle at 90% 15%, rgba(0, 180, 255, 0.12), transparent 30%),
        #080b14;
    color: white;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ================= HEADER ================= */

.logo {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1px;
}

.logo span {
    background: linear-gradient(90deg, #a78bfa, #60d5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.header-right {
    text-align: right;
    color: #7f879b;
    font-size: 12px;
    padding-top: 8px;
}


/* ================= HERO ================= */

.hero {
    text-align: center;
    padding: 70px 20px 45px;
}

.badge {
    display: inline-block;
    padding: 7px 15px;
    border-radius: 30px;
    background: rgba(130, 100, 255, 0.10);
    border: 1px solid rgba(150, 130, 255, 0.30);
    color: #b8a8ff;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 20px;
}

.hero-title {
    font-size: 54px;
    font-weight: 800;
    letter-spacing: -2.5px;
    margin: 0;
    background: linear-gradient(
        90deg,
        #ffffff,
        #aa96ff,
        #63d7ff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #8e96aa;
    font-size: 16px;
    margin-top: 16px;
    line-height: 1.7;
}


/* ================= CARDS ================= */

.card {
    background: rgba(18, 22, 36, 0.75);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 25px;
    backdrop-filter: blur(15px);
    margin-top: 20px;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 6px;
}

.card-subtitle {
    color: #858ca0;
    font-size: 13px;
}


/* ================= FILE UPLOADER ================= */

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.025);
    border: 1px dashed rgba(150,130,255,0.45);
    border-radius: 16px;
    padding: 15px;
    margin-top: 12px;
}


/* ================= TEXT INPUT ================= */

.stTextInput input {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 13px;
    color: white;
    padding: 14px;
    font-size: 14px;
}

.stTextInput input:focus {
    border-color: #917aff;
    box-shadow: 0 0 0 1px #917aff;
}


/* ================= BUTTON ================= */

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 13px;
    padding: 14px 20px;
    font-size: 15px;
    font-weight: 700;
    color: white;
    background: linear-gradient(
        90deg,
        #7657ff,
        #4daeff
    );
    box-shadow: 0 8px 25px rgba(100,80,255,0.25);
    transition: 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(100,80,255,0.40);
}


/* ================= ANSWER ================= */

.answer-card {
    background:
        linear-gradient(
            135deg,
            rgba(118,87,255,0.14),
            rgba(77,174,255,0.08)
        );
    border: 1px solid rgba(130,110,255,0.25);
    border-radius: 18px;
    padding: 25px;
    margin-top: 25px;
}

.answer-label {
    color: #a794ff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.answer-text {
    font-size: 25px;
    font-weight: 700;
    margin-top: 10px;
    color: white;
}


/* ================= EXPANDER ================= */

[data-testid="stExpander"] {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
}


/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #62697b;
    font-size: 12px;
    margin-top: 60px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PREMIUM HEADER
# =========================================================

col1, col2 = st.columns([3, 1])

with col1:

    st.markdown("""
<div class="logo">
✦ <span>QueryAI</span>
</div>
<div style="color:#858ca0;font-size:13px;">
Intelligent data analysis
</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="header-right">
POWERED BY GROQ ⚡
</div>
""", unsafe_allow_html=True)


# =========================================================
# PREMIUM HERO
# =========================================================

st.markdown("""
<div class="hero">
<div class="badge">✦ AI-POWERED DATA ANALYTICS</div>

<div class="hero-title">
Turn your data into answers.
</div>

<div class="hero-subtitle">
Upload your dataset and ask questions in plain English.
<br>
Let AI generate the analysis for you.
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# UPLOAD SECTION
# =========================================================

st.markdown("""
<div class="card">
<div class="card-title">
📁 Upload your dataset
</div>

<div class="card-subtitle">
Supported formats: CSV, Excel, TSV, Parquet and JSON
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# YOUR ORIGINAL FILE UPLOADER
# =========================================================

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["csv", "xlsx", "xls", "tsv", "parquet", "json"]
)


# =========================================================
# YOUR ORIGINAL FUNCTION
# =========================================================

def load_dataframe(file):

    filename = file.name.lower()

    if filename.endswith(".csv"):
        return pd.read_csv(file)

    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)

    elif filename.endswith(".tsv"):
        return pd.read_csv(file, sep="\t")

    elif filename.endswith(".parquet"):
        return pd.read_parquet(file)

    elif filename.endswith(".json"):
        return pd.read_json(file)

    return None


# =========================================================
# YOUR ORIGINAL GROQ MODEL
# =========================================================

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


# =========================================================
# QUESTION SECTION
# =========================================================

st.markdown("""
<div class="card">
<div class="card-title">
💬 Ask your data
</div>

<div class="card-subtitle">
Ask a question about your uploaded dataset using natural language.
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# YOUR ORIGINAL QUESTION INPUT
# =========================================================

question = st.text_input(
    'Enter Question:',
    placeholder="Example: What is the name of the employee with the highest salary?"
)


# =========================================================
# YOUR ORIGINAL LOGIC
# =========================================================

if st.button('✦  Get Answer'):
    if uploaded_file is None:
        st.warning("Please upload a file first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            df = load_dataframe(uploaded_file)
            if df is None:
                st.error("The uploaded file could not be read.")
            else:
                columns = list(df.columns)

                prompt = '''Role: Act as an experienced Python developer.
                Task: Write pandas code to find the answer to the question.
                Question: {}
                Context: DataFrame name is df and its column names are: {}
                Constraints: Sample data: {}
                Output format: Give executable Python code only.
                Do not provide any other information.
                Store the final answer in variable final_answer.
                Do not include import statements.
                If you don't know the answer, give output None'''.format(
                    question,
                    columns,
                    df.head(2)
                )

                response = llm.invoke(prompt)
                code = response.content.strip()

                # GENERATED CODE DISPLAY - original styling preserved
                st.markdown("""
                <div class="answer-card">
                <div class="answer-label">
                ✦ GENERATED CODE
                </div>
                </div>
                """, unsafe_allow_html=True)
                st.code(code, language="python")

                # BASIC CHECKS ONLY - NOT A SECURE SANDBOX
                ast.parse(code)
                forbidden = [
                    "import ", "open(", "eval(", "exec(",
                    "os.", "subprocess", "__"
                ]

                if any(word in code for word in forbidden):
                    st.error("Potentially unsafe code detected. Execution blocked.")
                else:
                    # Original execution workflow retained; execute only once.
                    execution_scope = {"df": df, "pd": pd}
                    exec(code, execution_scope, execution_scope)

                    if "final_answer" not in execution_scope:
                        st.error("The generated code did not create final_answer.")
                    else:
                        st.markdown("""
                        <div class="answer-card">
                        <div class="answer-label">
                        ✦ FINAL ANSWER
                        </div>
                        <div class="answer-text">
                        """, unsafe_allow_html=True)
                        st.write(execution_scope["final_answer"])
                        st.markdown("""
                        </div>
                        </div>
                        """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
✦ QueryAI &nbsp;•&nbsp;
Intelligent data analysis powered by AI
</div>
""", unsafe_allow_html=True)

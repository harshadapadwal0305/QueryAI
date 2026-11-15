# QueryAI – AI-Powered Natural Language to Pandas Query Generator

QueryAI is an AI-powered web application that converts natural language questions into Python Pandas code and generates answers from uploaded datasets.

Users can upload a dataset and ask questions in simple English. The application uses LangChain and Groq LLM to generate the required Pandas code and display the result.

## Features

- Upload datasets in CSV, Excel, TSV, Parquet, and JSON formats.
- Ask questions using natural language.
- Generate Python Pandas code using AI.
- Display generated code and query results.
- Simple and interactive Streamlit interface.

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq LLM
- Pandas
- python-dotenv

## Project Structure

```text
QueryAI/
│
├── app_qg.py
├── QUERY_GENERATOR.ipynb
├── employee_db.csv
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/harshadapadwal0305/QueryAI.git
```

2. Open the project folder:

```bash
cd QueryAI
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and add your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key
```

5. Run the application:

```bash
streamlit run app_qg.py
```

## How It Works

1. Upload a dataset.
2. Enter a question in natural language.
3. The AI generates the required Pandas code.
4. The application executes the generated code.
5. The result is displayed on the screen.

## Future Improvements

- Improve the safety of AI-generated code execution.
- Add better error handling and input validation.
- Deploy the application online.

## Author

**Harshada Padwal**

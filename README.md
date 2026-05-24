# 🎥 AI YouTube Insight Engine

An end-to-end NLP and Large Language Model application that extracts YouTube comments, performs sentiment analysis, and generates a comprehensive summary of viewer feedback. By leveraging the YouTube Data API, local Hugging Face transformer models, and Ollama, this tool provides instant qualitative insights into how audiences are reacting to any given video.

## 👁️ Demo

![YouTube Insight Engine Demo](path/to/your/demo.gif)
*(A quick look at the engine analyzing a YouTube video's comments in real-time.)*

## 🚀 Features
* **Automated Data Ingestion:** Fetches up to 500 top-level comments from any public YouTube video using the YouTube Data API v3.
* **Local Sentiment Analysis:** Utilizes a locally saved `distilbert-base-uncased-finetuned-sst-2-english` model to classify each comment as POSITIVE or NEGATIVE.
* **LLM Summarization:** Runs Llama 3.2 locally via Ollama to read through the classified comments and generate an intelligent, nuanced summary of viewer sentiment.
* **Interactive UI:** A custom, neo-brutalism styled web interface built with Flask, HTML, and CSS for easy URL submission and result viewing.

## 🛠️ Languages and Tools

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Hugging%20Face-F9AB00?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/Ollama-FFFFFF?style=for-the-badge&logo=ollama&logoColor=black" alt="Ollama" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
</p>

## 📋 Prerequisites

Before running the project, ensure you have the following installed:
* **Python 3.8+**
* **Ollama:** Installed and running locally on your machine.
* **YouTube Data API Key:** A valid API key from the Google Cloud Console.

## ⚙️ Installation & Setup

**1. Clone the repository**
\`\`\`bash
git clone https://github.com/nishant3937899/AI-youtube-insight-engine.git
cd AI-youtube-insight-engine
\`\`\`

**2. Set up a virtual environment (Recommended)**
\`\`\`bash
python -m venv youtubenv
source youtubenv/bin/activate  # On Windows use: youtubenv\Scripts\activate
\`\`\`

**3. Install dependencies**
\`\`\`bash
pip install -r requirements.txt
pip install google-api-python-client transformers ollama
\`\`\`

**4. Pull the local LLM via Ollama**
Ensure the Ollama application is running, then pull the Llama 3.2 model:
\`\`\`bash
ollama pull llama3.2
\`\`\`

**5. Configure the API Key**
Navigate to `app/models/commets_retrive.py` and replace the placeholder `API_KEY` with your actual YouTube Data API key. 

## 💻 Usage

Start the Flask application by running:
\`\`\`bash
python run.py
\`\`\`
* Open your browser and navigate to `http://127.0.0.1:5000`.
* Paste a YouTube video URL into the input field and click "Get Response".
* The engine will process the comments and display the LLM-generated sentiment summary in the response box.

## 📁 Project Structure

```
AI-youtube-insight-engine/
│
├── app/
│   ├── models/
│   │   ├── commets_retrive.py     # YouTube API data ingestion
│   │   ├── llm_process.py         # DistilBERT sentiment & Ollama integration
│   │   └── llm_ans.py             # Pipeline execution logic
│   ├── static/css/
│   │   └── style.css              # Web UI styling
│   ├── templates/
│   │   └── index.html             # Flask frontend
│   └── routes.py                  # Flask routing
│
├── tests/
│   └── trial.ipynb                # Jupyter notebook for model testing & EDA
│
├── requirements.txt               # Project dependencies
├── run.py                         # Application entry point
└── template.py                    # Script for generating folder structure
```

## 🌐 Connect with Me

<p align="left">
  <a href="https://linkedin.com/in/nishant-chandra-verma"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://github.com/nishant3937899"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://leetcode.com/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode"/></a>
</p>

**Author:** Nishant Chandra Verma

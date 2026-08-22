# 📄 AI Resume Analyser & Career Coach

An AI-powered Resume Analysis and Refinement tool built with **Streamlit** and **Groq Cloud LLMs**. This application parses PDF resumes and delivers detailed, recruiter-grade feedback across 6 core assessment pillars, along with an ATS score, actionable recommendations for Full Stack Developer roles, and a completely rewritten, modernized resume.

---

## 🌟 Features

- **⚡ Ultra-Fast Groq LLM Inference**: Powered by free-tier Groq models like `qwen-2.5-32b`, `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, and `mixtral-8x7b-32768`.
- **📑 PDF Text Extraction**: Uses `pypdf` to parse and count pages, words, and characters with instant preview.
- **🎯 6-Pillar Structured Evaluation**:
  1. **Content Clarity & Impact**: Action verbs, conciseness, metrics & quantified achievements.
  2. **Skills Presentation**: Grouped by Frontend, Backend, Database/Cloud, DevOps, Tools, and Soft Skills; pinpoints missing tech competencies.
  3. **Experience Descriptions**: STAR / Google XYZ framework review with before-and-after bullet point transformations.
  4. **Specific Recommendations for Full Stack Developers**: Architecture, system design, API design, DevOps, and portfolio project suggestions.
  5. **Overall Rating & Checklist**: ATS Compatibility score (out of 100), Role Fit score, and prioritized action checklist.
  6. **Refined Resume**: A complete, polished, ATS-optimized markdown rewrite ready to copy or download.
- **🎨 Sleek Streamlit UI**: Modern gradient hero, metric counters, expandable content viewer, and direct Markdown export.
- **🔐 Secure Key Management**: Configurable via `.env` file or directly in the application sidebar.

---

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    subgraph Client ["User Interface (Streamlit)"]
        A[User Uploads Resume PDF] --> B[PyPDF Parser]
        B --> C[Extracted Text & Metrics Preview]
        D[User Configures API Key, Model & Target Role] --> E[Click 'Run Full Resume Analysis']
    end

    subgraph Backend ["LLM Processing (Groq Cloud API)"]
        C --> F[Prompt Builder: 6 Pillars]
        E --> F
        F --> G[Groq Client API]
        G --> H["Groq Model (e.g., qwen-2.5-32b / llama-3.3-70b)"]
        H --> I[Structured Evaluation & Markdown Resume]
    end

    subgraph Output ["Results & Export"]
        I --> J[Display 6 Structured Assessment Sections]
        J --> K[Download Analysis Report (.md)]
        J --> L[Copy / Save Refined Resume]
    end
```

---

## 📂 Project Structure

```text
ai resume/
├── .streamlit/
│   ├── config.toml            # Streamlit theme & server configuration
│   └── secrets.toml.example   # Secrets template for Streamlit Cloud
├── .venv/                     # Python virtual environment
├── .env                       # (Optional) Local environment variables for GROQ_API_KEY
├── .env.example               # Template for environment variables
├── .gitignore                 # Git ignore file for secrets and cache
├── requirements.txt           # Python dependencies for local & cloud
├── main.py                    # Main Streamlit application
└── README.md                  # Comprehensive documentation
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone / Open Directory
Open a terminal in the project root directory:
```bash
cd "c:\Users\HP\Desktop\ai resume"
```

### 3. Initialize & Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**On Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Groq API Key
1. Get a free API key at [Groq Console](https://console.groq.com/keys).
2. Either create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
   ```
   *(Or you can enter the key directly into the sidebar in the web application).*

### 6. Run the Application
Launch the Streamlit web server:
```bash
streamlit run main.py
```

The app will open automatically in your default browser at `http://localhost:8501`.

---

## 🔍 How to Use the Application

1. **Upload Resume**: Drag and drop your resume in PDF format into the uploader.
2. **Review Extracted Text**: Inspect the page count, word count, and extracted text preview.
3. **Select Settings (Sidebar)**:
   - Enter or verify your Groq API Key.
   - Choose a model (Default: `qwen-2.5-32b` or `llama-3.3-70b-versatile`).
   - Specify your target job role (Default: `Full Stack Developer`).
4. **Run Analysis**: Click **"Run Full Resume Analysis"**.
5. **View Results & Export**:
   - Review each of the 6 structured assessment sections.
   - Check your ATS score and action checklist.
   - Copy or download the refined resume in Markdown format.

---

---

## ☁️ Deploying to Streamlit Community Cloud (Free Tier)

You can host this application completely free of charge on **Streamlit Community Cloud**:

### Step 1: Push Project to GitHub
1. Stage and commit all files:
   ```bash
   git add .
   git commit -m "feat: configure for streamlit cloud deployment"
   ```
2. Push your repository to your GitHub account:
   ```bash
   git push origin main
   ```

### Step 2: Deploy on Streamlit Cloud
1. Sign in to [share.streamlit.io](https://share.streamlit.io/) using your GitHub account.
2. Click **"New app"**.
3. Select your repository: `<your-username>/ai-resume`.
4. Set the **Main file path** to: `main.py`.
5. Under **Advanced settings** -> **Secrets**, paste your Groq API key:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
   ```
6. Click **Deploy!** 🚀

Your app will be live with a shareable public URL in under 2 minutes.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Engine**: [Groq Cloud](https://groq.com/) (`qwen-2.5-32b`, `llama-3.3-70b-versatile`)
- **PDF Extraction**: [pypdf](https://pypdf.readthedocs.io/)
- **Configuration**: [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

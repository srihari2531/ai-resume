# 📄 AI Resume Analyser & Career Coach

[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-Cloud_LLMs-F05A28?style=for-the-badge&logo=fastapi&logoColor=white)](https://groq.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

An intelligent, full-featured AI Resume Analysis & Refinement platform built with **Streamlit** and high-speed **Groq Cloud LLMs** (`qwen/qwen3.6-27b`, `openai/gpt-oss-120b`, `llama-3.3-70b-versatile`). 

Upload any PDF resume to receive recruiter-grade, ATS-calibrated feedback across **6 comprehensive pillars**, actionable development advice, and an instant markdown rewrite.

---

## 🌟 Key Features

- **⚡ Blazing-Fast Groq Inference**: Powered by active, high-throughput Groq models:
  - `qwen/qwen3.6-27b` *(Default & Free Tier - Fast, High-Quality Reasoning)*
  - `openai/gpt-oss-120b` *(High Intelligence)*
  - `openai/gpt-oss-20b` *(Lightweight & Efficient)*
  - `groq/compound`
- **🧠 Automatic Reasoning Sanitization**: Cleans internal `<think>` reasoning traces from chain-of-thought models so the output remains clean and presentation-ready.
- **📑 PDF Text Extraction & Metadata**: Extracts text with `pypdf`, displaying instant live previews, character counts, word counts, and page numbers.
- **🎯 6-Pillar Structured Evaluation Framework**:
  1. **Content Clarity & Impact**: Action verbs, conciseness, quantified achievements ($/%, metrics).
  2. **Skills Presentation**: Grouped into Frontend, Backend, Database/Cloud, DevOps, and Soft Skills with missing stack identification.
  3. **Experience Descriptions**: STAR / Google XYZ framework review with before-and-after bullet point transformations.
  4. **Target Role Recommendations**: System design, architecture, API design, testing, and portfolio recommendations.
  5. **Overall Rating & Checklist**: ATS compatibility score (/100), role alignment score, and prioritized action checklist.
  6. **Refined Resume**: Full ATS-ready markdown rewrite ready to copy or download.
- **🎨 Modern & Responsive UI**: Clean gradient styling, metric cards, collapsibles, and download utilities.
- **🔐 Flexible Secrets Management**: Automatically resolves `GROQ_API_KEY` from `.env`, `.venv/.env`, Streamlit Secrets (`secrets.toml`), or direct sidebar user input.

---

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    subgraph Client ["User Interface (Streamlit)"]
        A[User Uploads Resume PDF] --> B[PyPDF Parser]
        B --> C[Extracted Text & Metrics Preview]
        D[Configure API Key, Model & Target Role] --> E[Click 'Run Full Resume Analysis']
    end

    subgraph Backend ["LLM Processing (Groq Cloud API)"]
        C --> F[Structured Prompt Builder]
        E --> F
        F --> G[Groq Client API]
        G --> H["Groq Model (e.g., qwen/qwen3.6-27b)"]
        H --> I[Reasoning Sanitizer & Markdown Formatter]
    end

    subgraph Output ["Output & Export"]
        I --> J[Display 6 Structured Assessment Pillars]
        J --> K[Download Analysis Report (.md)]
        J --> L[Copy / Download Refined Resume]
    end
```

---

## 📂 Project Structure

```text
ai resume/
├── .devcontainer/             # Dev container configuration
├── .streamlit/
│   ├── config.toml            # Streamlit theme & UI settings
│   └── secrets.toml.example   # Streamlit secrets template
├── .venv/                     # Python virtual environment
├── .env                       # Local environment variables (GROQ_API_KEY)
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file for secrets, cache, and venv
├── requirements.txt           # Python package dependencies
├── main.py                    # Main Streamlit application
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+** installed on your machine.
- A free **Groq Cloud API Key** from [console.groq.com/keys](https://console.groq.com/keys).

---

### 2. Setup Virtual Environment & Dependencies

#### **Windows (PowerShell):**
```powershell
# 1. Open the project folder
cd "c:\Users\HP\Desktop\ai resume"

# 2. Activate existing .venv (or create one with: python -m venv .venv)
.\.venv\Scripts\Activate.ps1

# 3. Install required packages
.\.venv\Scripts\pip install -r requirements.txt
```

> **Note on PowerShell Execution Policy:** If you encounter a script execution error when running `Activate.ps1`, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

#### **Windows (Command Prompt):**
```cmd
cd "c:\Users\HP\Desktop\ai resume"
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

#### **Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Configure Your Groq API Key

Create a `.env` file in the project root:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```
*(Alternatively, you can paste the API key directly into the sidebar text field in the web app, or place it inside `.venv/.env` / `.streamlit/secrets.toml`).*

---

### 4. Run the Application

Using your virtual environment:
```powershell
.\.venv\Scripts\streamlit run main.py
```
Or with the active virtual environment:
```bash
streamlit run main.py
```

The application will launch in your browser at **`http://localhost:8501`**.

---

## 🔍 How to Use

1. **Upload Resume**: Drag and drop your resume (`.pdf`) into the upload area.
2. **Inspect Extracted Content**: Verify extracted text, page count, and word statistics.
3. **Configure Settings (Sidebar)**:
   - Verify/Enter your **Groq API Key**.
   - Choose your **Model** (Default: `qwen/qwen3.6-27b`).
   - Specify your **Target Job Role** (Default: *Full Stack Developer*).
4. **Analyze**: Click **"🚀 Run Full Resume Analysis"**.
5. **Review & Download**:
   - Explore the 6 assessment cards and ATS score checklist.
   - Click **"📥 Download Full Analysis (.md)"** to save your report.

---

## ☁️ Deployment to Streamlit Community Cloud (Free)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "feat: setup ai resume analyzer with qwen 3.6 27b"
   git push origin main
   ```
2. **Deploy on Streamlit**:
   - Go to [share.streamlit.io](https://share.streamlit.io/).
   - Select your repository, set the **Main file path** to `main.py`.
   - Under **Advanced settings ➔ Secrets**, paste:
     ```toml
     GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
     ```
   - Click **Deploy!** 🚀

---

## 🛠️ Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Model Decommissioned Error (400)** | Outdated model (e.g. `qwen-2.5-32b`) selected | Choose `qwen/qwen3.6-27b`, `openai/gpt-oss-120b`, or `llama-3.3-70b-versatile`. |
| **Missing API Key** | No `.env`, `.venv/.env`, or sidebar key provided | Add `GROQ_API_KEY` to `.env` or input it directly in the sidebar. |
| **PowerShell Script Execution Error** | Windows execution policy restricts script running | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`. |

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).

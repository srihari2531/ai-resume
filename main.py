import os
import io
import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env if present
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer & Refiner",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for modern, polished UI
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Header Gradient */
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2563eb 0%, #7c3aed 50%, #db2777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    .hero-subtitle {
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    
    /* Card design */
    .metric-card {
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        background-color: #e0e7ff;
        color: #3730a3;
        margin-right: 0.5rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        opacity: 0.92;
        transform: translateY(-1px);
        box-shadow: 0 6px 12px -2px rgba(99, 102, 241, 0.3);
    }
</style>
""", unsafe_allow_html=True)


def extract_text_from_pdf(pdf_file) -> str:
    """Extract and sanitize text from an uploaded PDF file."""
    reader = PdfReader(pdf_file)
    extracted_text = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            extracted_text.append(f"--- Page {page_num + 1} ---\n" + text.strip())
    return "\n\n".join(extracted_text)


def analyze_resume_with_groq(api_key: str, model_name: str, resume_text: str, target_role: str) -> str:
    """Call Groq API to analyze the resume across the 6 structured pillars."""
    client = Groq(api_key=api_key)
    
    system_prompt = f"""You are an elite Senior Technical Recruiter, Career Coach, and Hiring Manager specializing in evaluating candidates for the role of '{target_role}'.
Your task is to provide an in-depth, honest, constructive, and highly actionable analysis of the provided resume.

You MUST structure your response into the following 6 distinct and comprehensive sections using clear Markdown headings (H2/H3), bullet points, and callout blocks:

## 1. Content Clarity & Impact
- Evaluate the clarity of communication, conciseness, and readability.
- Assess the use of strong action verbs and active vs. passive voice.
- Check for quantifiable metrics (e.g., percentages, revenue, latency improvements, user scale).
- Highlight specific sentences that need rewording and provide improved examples.

## 2. Skills Presentation
- Categorize identified skills into: Frontend, Backend, Database/Cloud, DevOps, Tools, and Soft Skills.
- Identify strengths in the current skill set.
- Pinpoint critical missing skills, outdated technologies, or gaps relevant to the '{target_role}' role.
- Recommend better ways to group and highlight core competencies.

## 3. Experience Descriptions
- Evaluate how effectively previous roles and projects are described.
- Assess adherence to the STAR (Situation, Task, Action, Result) or Google XYZ framework.
- Identify weak or generic bullet points and provide side-by-side "Before vs. After" transformations.

## 4. Specific Recommendations for {target_role}
- Provide actionable advice tailored specifically to succeeding as a top-tier {target_role}.
- Architecture, system design, API design, security, performance optimization, and testing recommendations.
- Suggested portfolio projects or open-source contributions to add maximum credibility.

## 5. Overall Rating & Checklist
- **ATS Compatibility Score**: Give an ATS score out of 100 with justification.
- **Role Fit Score**: Give a role readiness score out of 100 for '{target_role}'.
- **Actionable Checklist**:
  - [ ] Critical Fixes (Must change immediately)
  - [ ] Recommended Enhancements (High value additions)
  - [ ] Polish & Formatting items

## 6. Refined Resume
- Provide a complete, polished, and professionally rewritten version of the resume formatted in clean, modern Markdown.
- Incorporate strong action verbs, quantifiable achievements, structured skill sections, and impactful bullet points tailored for the '{target_role}' position.
"""

    user_prompt = f"""Target Role: {target_role}

Resume Content:
\"\"\"
{resume_text}
\"\"\"

Please perform the full 6-pillar analysis and provide the refined resume version now."""

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=4096,
    )
    
    return completion.choices[0].message.content


# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/resume.png", width=64)
    st.title("Settings & Config")
    
    # API Key Resolution (Supports Streamlit Cloud Secrets, .env, and direct sidebar input)
    def get_configured_api_key():
        try:
            if "GROQ_API_KEY" in st.secrets and st.secrets["GROQ_API_KEY"]:
                return st.secrets["GROQ_API_KEY"]
        except Exception:
            pass
        return os.getenv("GROQ_API_KEY", "")

    env_api_key = get_configured_api_key()
    api_key_input = st.text_input(
        "Groq API Key",
        value=env_api_key,
        type="password",
        help="Get your free API key at https://console.groq.com/keys. When hosted on Streamlit Cloud, you can also store this under App Secrets."
    )
    if env_api_key:
        st.caption("🔒 *API Key detected from environment / Streamlit Secrets*")
    
    # Model Selection
    model_options = [
        "qwen-2.5-32b",
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it"
    ]
    selected_model = st.selectbox(
        "Groq LLM Model",
        options=model_options,
        index=0,
        help="Select a fast, high-accuracy Groq model for resume evaluation."
    )
    
    # Target Role
    target_role = st.text_input(
        "Target Job Role",
        value="Full Stack Developer",
        help="The specific role against which the resume will be benchmarked."
    )
    
    st.markdown("---")
    st.markdown("### 📌 Analysis Criteria")
    st.markdown("""
    1. **Content Clarity & Impact**
    2. **Skills Presentation**
    3. **Experience Descriptions**
    4. **Role Recommendations**
    5. **Rating & Checklist**
    6. **Refined Resume**
    """)
    
    st.markdown("---")
    st.caption("Powered by Groq Free Tier LLMs & Streamlit")


# --- MAIN CONTENT AREA ---
st.markdown('<div class="hero-title">AI Resume Analyser & Career Coach</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="hero-subtitle">Optimize your resume for <b>{target_role}</b> roles using ultra-fast Groq AI models.</div>',
    unsafe_allow_html=True
)

# File Uploader
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF format)",
    type=["pdf"],
    help="Upload your resume in PDF format to extract content and start analysis."
)

if uploaded_file is not None:
    try:
        with st.spinner("Extracting text from PDF..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            page_count = len(PdfReader(uploaded_file).pages)
            char_count = len(resume_text)
            word_count = len(resume_text.split())
        
        # Display extraction metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Pages", page_count)
        with col2:
            st.metric("Word Count", word_count)
        with col3:
            st.metric("Character Count", char_count)
            
        with st.expander("👁️ Preview Extracted Resume Text"):
            st.text_area("Extracted Content", resume_text, height=200, disabled=True)
            
        # Analysis trigger button
        st.markdown("### 🚀 Ready to Analyze?")
        if st.button("🔍 Run Full Resume Analysis", key="btn_analyze"):
            active_api_key = api_key_input.strip() or env_api_key.strip()
            
            if not active_api_key:
                st.error("⚠️ Please provide a valid Groq API Key in the sidebar, via Streamlit Secrets, or in your .env file to proceed.")
            elif not resume_text.strip():
                st.error("⚠️ Could not extract any readable text from the uploaded PDF. Please verify the file is not scanned or empty.")
            else:
                with st.spinner(f"Analyzing resume with Groq ({selected_model}) for {target_role}..."):
                    try:
                        analysis_output = analyze_resume_with_groq(
                            api_key=active_api_key,
                            model_name=selected_model,
                            resume_text=resume_text,
                            target_role=target_role
                        )
                        st.session_state["analysis_result"] = analysis_output
                        st.success("✅ Analysis completed successfully!")
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
                        st.info("Tip: Double-check your Groq API key and selected model availability.")

    except Exception as e:
        st.error(f"Error reading PDF file: {str(e)}")

# Display Analysis Results
if "analysis_result" in st.session_state and st.session_state["analysis_result"]:
    result_text = st.session_state["analysis_result"]
    
    st.markdown("---")
    st.markdown("## 📊 Comprehensive Resume Assessment")
    
    # Download actions
    download_col1, download_col2 = st.columns([1, 1])
    with download_col1:
        st.download_button(
            label="📥 Download Full Report (Markdown)",
            data=result_text,
            file_name=f"resume_analysis_{target_role.lower().replace(' ', '_')}.md",
            mime="text/markdown"
        )
    with download_col2:
        # Extract refined resume if separable, or provide full report
        st.info("💡 You can copy or download the refined resume directly from Section 6 below.")
        
    # Render Full Analysis
    st.markdown(result_text)

else:
    if not uploaded_file:
        # Guidance card when no file is uploaded
        st.info("👋 Upload your resume PDF above and click **Run Full Resume Analysis** to get started!")

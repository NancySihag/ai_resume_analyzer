import streamlit as st
import PyPDF2
from analyzer import ResumeAnalyzer


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🎯",
    layout="wide"
)


# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------
def parse_pdf_stream(file_stream) -> str:
    """Extract text from an uploaded PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(file_stream)

        extracted_text = ""

        for page in pdf_reader.pages:
            extracted_text += page.extract_text() or ""

        return extracted_text

    except Exception as e:
        st.error(f"Failed to process the PDF: {str(e)}")
        return ""


# -----------------------------
# JOB ROLE TEMPLATES
# -----------------------------
ROLE_TEMPLATES = {
    "Custom (Paste your own Job Description)": "",

    "Data Analyst Intern":
        "Looking for an intern skilled in Python, SQL, Tableau, Excel, "
        "data cleaning, and statistical analysis. Great communication "
        "and teamwork required.",

    "Frontend Developer Intern":
        "Seeking a developer intern fluent in JavaScript, React, HTML, CSS, "
        "Git, and responsive engineering layout. Experience working in "
        "an Agile environment is a plus.",

    "Cloud/DevOps Intern":
        "Position requires knowledge of AWS cloud technologies, Linux "
        "architecture, Docker containers, basic API systems, and "
        "problem-solving skills."
}


# -----------------------------
# MAIN APPLICATION
# -----------------------------
st.title("AI Resume Analyzer 🎯")

st.caption(
    "Analyze your resume, compare it with a job description, "
    "and discover keywords you may be missing."
)

st.markdown("---")


# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.header("1. Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF format)",
        type=["pdf"]
    )

    st.header("2. Target Job")

    selected_role = st.selectbox(
        "Select Target Role:",
        list(ROLE_TEMPLATES.keys())
    )

    jd_input = st.text_area(
        label="Job Description:",
        value=(
            ROLE_TEMPLATES[selected_role]
            if selected_role != "Custom (Paste your own Job Description)"
            else ""
        ),
        height=200
    )


# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("Analyze My Resume", type="primary"):

    if not uploaded_file or not jd_input.strip():

        st.warning(
            "Please upload a PDF resume and provide a job description."
        )

    else:

        with st.spinner("Analyzing your resume..."):

            # -----------------------------
            # STEP 1: EXTRACT RESUME TEXT
            # -----------------------------
            extracted_text = parse_pdf_stream(uploaded_file)

            if extracted_text.strip():

                # -----------------------------
                # STEP 2: ANALYZE RESUME
                # -----------------------------
                engine = ResumeAnalyzer(
                    extracted_text,
                    jd_input
                )

                match_score = engine.calculate_match_score()

                missing_hard, missing_soft = (
                    engine.extract_keyword_gaps()
                )

                compliance_checks = (
                    engine.check_structural_compliance()
                )

                tone_status, verb_count = (
                    engine.evaluate_phrasing_tone()
                )

                density_msg, density_color = (
                    engine.get_readability_metrics()
                )

                blueprints = (
                    engine.generate_project_roadmaps(
                        missing_hard
                    )
                )

                # -----------------------------
                # SUCCESS MESSAGE
                # -----------------------------
                st.success(
                    "Resume analysis completed successfully!"
                )

                # -----------------------------
                # CORE METRICS
                # -----------------------------
                st.subheader("📊 Resume Analysis")

                m_col1, m_col2, m_col3 = st.columns(3)

                m_col1.metric(
                    "Job Match Score",
                    f"{match_score}%"
                )

                m_col2.metric(
                    "Action Verb Tone",
                    tone_status
                )

                m_col3.metric(
                    "Detected Action Words",
                    f"{verb_count}"
                )

                # -----------------------------
                # ATS PAGE DENSITY
                # -----------------------------
                if density_color == "green":

                    st.info(
                        f"📊 **ATS Page Density:** {density_msg}"
                    )

                elif density_color == "orange":

                    st.warning(
                        f"⚠️ **ATS Page Density:** {density_msg}"
                    )

                else:

                    st.error(
                        f"🚨 **ATS Page Density:** {density_msg}"
                    )

                st.markdown("---")

                # -----------------------------
                # RESUME SECTION CHECK
                # -----------------------------
                st.subheader("📋 Resume Section Check")

                comp_cols = st.columns(
                    len(compliance_checks)
                )

                for idx, (section, exists) in enumerate(
                    compliance_checks.items()
                ):

                    if exists:

                        comp_cols[idx].success(
                            f"✅ {section}"
                        )

                    else:

                        comp_cols[idx].error(
                            f"❌ {section}"
                        )

                st.markdown("---")

                # -----------------------------
                # KEYWORD GAPS
                # -----------------------------
                st.subheader("🔎 Keyword Analysis")

                g_col1, g_col2 = st.columns(2)

                # Technical skills
                with

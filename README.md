# 🤖 AI Resume Analyzer

An AI-powered resume analysis dashboard that helps users evaluate their resumes against different job roles and identify areas for improvement.

## 🌐 Live Demo

https://nancy-ai-resume-analyzer.streamlit.app

## ✨ Features

- 📄 Upload a PDF resume
- 🤖 Analyze resume content with AI
- 🎯 Compare resume with different job roles
- 📊 Identify relevant skills and keywords
- 💡 Generate actionable resume improvement suggestions
- 🔍 Analyze resume-job alignment
- 🖥️ Simple Streamlit dashboard

## 🎯 Supported Job Roles

The application currently includes templates for:

- Data Analyst Intern
- Frontend Developer Intern
- Cloud / DevOps Intern

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF2
- AI / LLM integration
- Git & GitHub

## 📂 Project Structure


ai_resume_analyzer/
│
├── app.py
├── ResumeAnalyzer.py
├── requirements.txt
├── README.md
└── ...

⚙️ How to Run Locally
1. Clone the repository

   git clone https://github.com/NancySihag/ai_resume_analyzer.git

   cd ai_resume_analyzer

2. Create a virtual environment

    python -m venv venv

 3.Activate the environment

    macOS / Linux:

    source venv/bin/activate

   Windows:
 
    venv\Scripts\activate

4. Install dependencies

    pip install -r requirements.txt
 

5. Run the application

   streamlit run app.py

The application will open in your browser.

**🔐 Privacy**
Resume files may contain sensitive personal information.
For safety, avoid uploading resumes containing unnecessary private information when testing the application.

**🚀 Future Improvements**
- Support more job roles
- Add ATS-style scoring
- Improve skill extraction
- Add detailed keyword analysis
- Add downloadable analysis reports
- Improve resume-job matching

**👩‍💻 Author**
Nancy Sihag
Python Developer | AI & Automation | Web Development
- GitHub: https://github.com/NancySihag
- LinkedIn: https://www.linkedin.com/in/nancy-sihag

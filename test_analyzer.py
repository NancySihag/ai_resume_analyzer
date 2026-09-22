from analyzer import analyze_resume


def test_analyze_resume():
    resume = "Python developer with experience in Flask and Streamlit."
    job_description = "Looking for a Python developer with Flask experience."

    result = analyze_resume(resume, job_description)

    assert result is not None

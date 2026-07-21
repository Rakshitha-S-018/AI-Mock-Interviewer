from modules.ai_client import ask_ai
import PyPDF2


# ==========================================
# EXTRACT TEXT FROM PDF
# ==========================================

def extract_resume_text(uploaded_file):

    """
    Extract text from an uploaded PDF resume.
    """

    # Move to the beginning of the uploaded file
    uploaded_file.seek(0)

    pdf_reader = PyPDF2.PdfReader(
        uploaded_file
    )

    text = ""

    for page in pdf_reader.pages:

        extracted_text = page.extract_text()

        if extracted_text:

            text += extracted_text + "\n"

    return text


# ==========================================
# ANALYZE RESUME
# ==========================================

def analyze_resume(

    uploaded_file,

    target_role=None

):

    """
    Analyze an uploaded PDF resume using AI.
    """

    # --------------------------------------
    # Extract text ONLY HERE
    # --------------------------------------

    resume_text = extract_resume_text(

        uploaded_file

    )


    # --------------------------------------
    # Check extracted text
    # --------------------------------------

    if not resume_text.strip():

        return (

            "❌ Could not extract text from this PDF.\n\n"

            "The PDF may contain scanned images instead of selectable text."

        )


    # --------------------------------------
    # Default role
    # --------------------------------------

    if not target_role:

        target_role = "Software Developer"


    # --------------------------------------
    # AI Prompt
    # --------------------------------------

    prompt = f"""

You are an expert HR Recruiter and Technical Career Coach.

Analyze this resume for the following target role:

TARGET ROLE:
{target_role}


RESUME CONTENT:

{resume_text}


Provide a detailed professional resume analysis.

Use the following format:


Resume Score: xx/100


Summary

Give a concise summary of the candidate's profile.


Strengths

List the strongest aspects of the resume.


Weaknesses

List areas that need improvement.


Technical Skills

List all technical skills found in the resume.


Soft Skills

List the soft skills found in the resume.


Missing Skills

List important skills missing for the target role.


Projects Feedback

Evaluate the projects.

Mention whether the projects are technically strong and relevant.


Certifications Feedback

Evaluate existing certifications.

Suggest relevant certifications if appropriate.


Final Suggestions

Give clear and actionable suggestions to improve the resume.


"""


    # --------------------------------------
    # Call AI
    # --------------------------------------

    analysis = ask_ai(

        prompt

    )


    return analysis
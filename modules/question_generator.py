from modules.ai_client import ask_ai


def generate_questions(role, difficulty, interview_type):
    """
    Generate 5 interview questions using Groq AI.
    """

    prompt = f"""
You are an experienced interviewer.

Generate exactly 5 interview questions.

Role:
{role}

Difficulty:
{difficulty}

Interview Type:
{interview_type}

Rules:

- Number the questions.
- Only return the questions.
- Do not include answers.
"""

    response = ask_ai(prompt)

    questions = []

    for line in response.split("\n"):

        line = line.strip()

        if line:

            if line[0].isdigit():

                question = line.split(".", 1)[-1].strip()

                questions.append(question)

    return questions[:5]
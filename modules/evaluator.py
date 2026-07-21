from modules.ai_client import ask_ai


def evaluate_answer(question, answer):
    """
    Evaluate a candidate's answer using Groq AI.
    """

    prompt = f"""
You are a senior technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return ONLY in this format:

Score: x/10

Strengths:
- point
- point

Weaknesses:
- point
- point

Suggestions:
- point
"""

    return ask_ai(prompt)
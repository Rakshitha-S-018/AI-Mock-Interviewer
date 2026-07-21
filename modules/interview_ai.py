from modules.ai_client import ask_ai


def interview_chat(history, user):

    prompt = f"""
You are InterviewIQ AI.

Continue this interview naturally.

Conversation:

{history}

Candidate:

{user}

Reply as an interviewer.
"""

    return ask_ai(prompt)
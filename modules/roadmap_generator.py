from modules.ai_client import ask_ai


def generate_roadmap(target_role, current_skills):
    """
    Generate a personalized learning roadmap.
    """

    prompt = f"""
You are an expert Career Mentor.

Target Role:
{target_role}

Current Skills:
{current_skills}

Generate a detailed 8-week learning roadmap.

Return in this format:

Week 1
Topics
Resources
Mini Project

Week 2
Topics
Resources
Mini Project

Continue until Week 8.

Finally provide:

Interview Preparation Tips

Recommended Certifications

Final Motivation
"""

    return ask_ai(prompt)
from modules.ai_client import ask_ai


def analyze_skill_gap(resume_analysis, target_role):
    """
    Analyze the candidate's skill gap based on the resume analysis
    and target role.
    """

    prompt = f"""
You are an expert Career Coach.

Candidate Resume Analysis:

{resume_analysis}

Target Role:

{target_role}

Analyze the skill gap.

Return ONLY in the following format.

Skill Match : xx%

Current Skills

- Skill 1
- Skill 2
- Skill 3

Missing Skills

- Skill 1
- Skill 2
- Skill 3

Priority Skills

- High
- Medium
- Low

Recommended Courses

- Course 1
- Course 2
- Course 3

Final Advice

Give detailed suggestions to improve employability.
"""

    return ask_ai(prompt)
import re
from jobs.models import Skill
import os
from google import genai
from django.conf import settings



def identify_resume_skills(resume_text):

    all_skills = Skill.objects.all()

    matched_skills = []

    for skill in all_skills:

        pattern = r'(?<!\w)' + re.escape(skill.name) + r'(?!\w)'

        if re.search(pattern, resume_text, re.IGNORECASE):
            matched_skills.append(skill.name)

    return matched_skills

def calculate_job_match(resume_skills, required_skills):

    resume_skills = {
        skill.lower() for skill in resume_skills
    }

    required_skills = {
        skill.lower() for skill in required_skills
    }

    if not required_skills:
        return {
            "match_score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched_skills = resume_skills.intersection(
        required_skills
    )

    missing_skills = required_skills - resume_skills

    match_score = (
        len(matched_skills) / len(required_skills)
    ) * 100

    return {
        "match_score": round(match_score, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }


def generate_ai_suggestions(resume_text):

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    prompt = f"""
Analyze this resume briefly.

Give:
1. Resume strengths
2. Weaknesses
3. Missing technical skills
4. Improvements
5. Suitable career options

Keep the response simple and under 300 words.

Resume:
{resume_text}
"""

    response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "http_options": {
            "timeout": 30000
        }
    }
)
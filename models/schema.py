from pydantic import BaseModel
from typing import List

class ResumeMatch(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    role_level: str
    resume_improvements: List[str]
    ats_keywords_missing: List[str]

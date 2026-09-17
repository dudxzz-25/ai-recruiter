import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python","sql","postgresql","mysql","power bi","tableau","excel","pandas","numpy",
    "scikit-learn","machine learning","deep learning","nlp","git","docker","aws","azure",
    "java","javascript","html","css","c","linux","spark","airflow","etl","api","flask"
]

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zà-ú0-9+#.\- ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_skills(text: str) -> set[str]:
    text = normalize(text)
    return {skill for skill in SKILLS if re.search(rf"(?<!\w){re.escape(skill)}(?!\w)", text)}


def calculate_score(resume: str, job: str) -> dict:
    resume_n, job_n = normalize(resume), normalize(job)
    if not resume_n or not job_n:
        return {"score": 0, "semantic_score": 0, "skill_score": 0, "matched": [], "missing": []}
    matrix = TfidfVectorizer(ngram_range=(1, 2), stop_words=None).fit_transform([resume_n, job_n])
    semantic = float(cosine_similarity(matrix[0:1], matrix[1:2])[0, 0])
    resume_skills, job_skills = extract_skills(resume_n), extract_skills(job_n)
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    skill_score = len(matched) / len(job_skills) if job_skills else semantic
    final = 100 * (0.55 * semantic + 0.45 * skill_score)
    return {
        "score": round(final, 1),
        "semantic_score": round(semantic * 100, 1),
        "skill_score": round(skill_score * 100, 1),
        "matched": matched,
        "missing": missing,
    }

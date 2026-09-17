from pathlib import Path
import io
import sqlite3
from flask import Flask, render_template, request
from pypdf import PdfReader
from scoring import calculate_score

BASE = Path(__file__).resolve().parent
DB = BASE / "recruiter.db"
app = Flask(__name__)


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            score REAL NOT NULL,
            semantic_score REAL NOT NULL,
            skill_score REAL NOT NULL,
            matched_skills TEXT,
            missing_skills TEXT
        )""")


def read_resume(file):
    if not file or not file.filename:
        return ""
    if file.filename.lower().endswith(".pdf"):
        reader = PdfReader(io.BytesIO(file.read()))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return file.read().decode("utf-8", errors="ignore")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        resume_text = request.form.get("resume_text", "")
        uploaded = read_resume(request.files.get("resume_file"))
        job = request.form.get("job_description", "")
        result = calculate_score((resume_text + "\n" + uploaded).strip(), job)
        with sqlite3.connect(DB) as conn:
            conn.execute("""INSERT INTO analyses(score, semantic_score, skill_score, matched_skills, missing_skills)
                          VALUES (?, ?, ?, ?, ?)""",
                         (result["score"], result["semantic_score"], result["skill_score"],
                          ", ".join(result["matched"]), ", ".join(result["missing"])))
    return render_template("index.html", result=result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

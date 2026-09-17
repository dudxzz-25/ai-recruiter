import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
from scoring import calculate_score, extract_skills

class TestScoring(unittest.TestCase):
    def test_skill_extraction(self):
        self.assertEqual(extract_skills("Python e SQL"), {"python", "sql"})
    def test_good_match_scores_above_bad_match(self):
        job = "Python SQL pandas machine learning Git ETL"
        good = calculate_score("Python SQL pandas machine learning Git ETL", job)["score"]
        bad = calculate_score("design fotografia atendimento", job)["score"]
        self.assertGreater(good, bad)

if __name__ == "__main__": unittest.main()

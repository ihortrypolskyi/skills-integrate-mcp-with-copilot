import unittest

from src.app import activities


class GitHubSkillsActivityTest(unittest.TestCase):
    def test_github_skills_activity_exists(self):
        self.assertIn("GitHub Skills", activities)
        self.assertIn("Learn practical coding and collaboration skills", activities["GitHub Skills"]["description"])
        self.assertIsInstance(activities["GitHub Skills"]["participants"], list)


if __name__ == "__main__":
    unittest.main()

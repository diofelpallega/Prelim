import unittest

class ScoreTest(unittest.TestCase): 
    def score_can_view_score(self):
        score = Score()
        total = score.show()
        self.assertEqual(total, [])


if __name__ == "__main__":
	unittest.main()

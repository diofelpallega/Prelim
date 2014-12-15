import unittest
from score.score import *

score  = Score()

class SolveTest(unittest.TestCase):
    def test_if_can_show(self): 
        result = score.show()
        self.assertEqual(result,[0,0])

    def test_if_score_can_add_team1(self): 
        result = score.addteam1(2)
        self.assertEqual(result,2)

    def test_if_score_can_add_team2(self): 
        result = score.addteam2(2)
        self.assertEqual(result,2)    

    def test_if_score_cant_add_more_than_3(self):
        result = score.addteam1(4)
        self.assertEqual(result, "not possible")
        self.assertEqual(score.team1,2)

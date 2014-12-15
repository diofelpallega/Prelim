class Score(object):
    def __init__(self):
        self.result = [0,0]
        self.team1 = 0
        self.team2 = 0

    def show(self):
        return self.result
   
    def addteam1(self,score):
        if (score <= 3):
            self.team1 = self.team1 + score   
            return self.team1
        else:
            return "not possible"  

    def addteam2(self,score):
        if (score <= 3):
            self.team2 = self.team2 + score   
            return self.team2   
        else:
            return "not possible"
from flask import render_template,request,Flask,redirect
from score.score import *

APP = Flask(__name__)
score = Score()

@APP.route("/")
def index():
	"""Renders the score html"""
	return render_template('score.html')

@APP.route("/score1/")
def solve1():
    """return scoreboard"""
    x = request.args.get('team1') 
    if x.isalpha():
        return render_template('warning3.html')
    if int(x) > 3 :
        return render_template('warning.html')
    if int(x) < 1:
        return render_template('warning2.html')

    else:
        result = score.addteam1(int(x)) 
        return render_template('score.html')

@APP.route("/score2/")
def solve2():
    """return scoreboard"""
    y = request.args.get('team2') 
    if y.isalpha():
        return render_template('warning3.html')
    if int(y) > 3:
        return render_template('warning.html')
    if int(y) < 1:
        return render_template('warning2.html')

    else:
        result = score.addteam2(int(y))
        return render_template('score.html')

@APP.route("/scoreboard/")
def solve3():
    """return scoreboard"""
    result1 = score.team1
    result2 = score.team2 
    return render_template('scoreboard.html', result1=result1, result2=result2)

if __name__ == "__main__":
    import cProfile
    APP.run(debug=True)
    cProfile.run('APP.run(debug=True)', sort='time')

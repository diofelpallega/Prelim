"""DOCSTRING"""
from flask import render_template, request, Flask
from score.score import Score

APP = Flask(__name__)
SCORE = Score()

@APP.route("/")
def index():
    """Renders the score html"""
    return render_template('score.html')

@APP.route("/score1/")
def solve1():
    """return scoreboard"""
    team1score = request.args.get('team1')
    if team1score.isalpha():
        return render_template('warning3.html')
    if int(team1score) > 3:
        return render_template('warning.html')
    if int(team1score) < 1:
        return render_template('warning2.html')

    else:
        SCORE.addteam1(int(team1score))
        return render_template('score.html')

@APP.route("/score2/")
def solve2():
    """return scoreboard"""
    team2score = request.args.get('team2')
    if team2score.isalpha():
        return render_template('warning3.html')
    if int(team2score) > 3:
        return render_template('warning.html')
    if int(team2score) < 1:
        return render_template('warning2.html')

    else:
        SCORE.addteam2(int(team2score))
        return render_template('score.html')

@APP.route("/scoreboard/")
def solve3():
    """return scoreboard"""
    result1 = SCORE.team1
    result2 = SCORE.team2
    return render_template('scoreboard.html', result1=result1, result2=result2)

if __name__ == "__main__":
    import cProfile
    APP.run(debug=True)
    cProfile.run('APP.run(debug=True)', sort='time')

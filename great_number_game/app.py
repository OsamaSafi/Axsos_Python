import random

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "keep_it_safe"

leaderboard = []

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('index.html', leaderboard=leaderboard)

@app.route('/compair-num', methods=['POST'])
def compair():
    if 'num' not in session or 'attempts' not in session:
        return redirect('/')

    session['attempts'] += 1
    guess = int(request.form['number'])
    target = session['num']
    
    result = ""
    status = "playing"

    if guess > target:
        result = "Too high!"
    elif guess < target:
        result = "Too low!"
    else:
        result = f"{session['num']} was the number!"
        status = "win"
    if session['attempts'] >= 5 and status != "win":
        result = "You Lose! You've used all 5 attempts."
        status = "lose"

    return render_template('index.html', result=result, status=status)

@app.route('/submit-winner', methods=['POST'])
def submit_winner():
    name = request.form['name']
    leaderboard.append({'name': name, 'attempts': session['attempts']})
    leaderboard.sort(key=lambda x: x['attempts'])
    return redirect('/reset')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
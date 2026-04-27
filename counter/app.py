from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep_it_safe"

@app.route('/')
def index():
    if 'visible' not in session:
        session['visible'] = 0
    session['visible'] += 1

    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    if 'counter' in session:
        session['counter'] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
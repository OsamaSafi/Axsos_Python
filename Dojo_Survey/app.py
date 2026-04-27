from flask import Flask,request,session,render_template,redirect

app = Flask(__name__)

app.secret_key = "keep_it_safe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=["POST"])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
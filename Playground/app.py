from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<int:number>')
def play(number):
    return render_template('play_x.html',times = number)

@app.route('/play/<int:number>/<color>')
def play_color(number,color):
    return render_template('play_color.html',times = number,color=color)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
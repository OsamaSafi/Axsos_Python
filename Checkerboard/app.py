from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4')
def board():
    return render_template('board_four.html')

@app.route('/<int:x>/<int:y>')
def board_xy(x, y):
    return render_template("board.html", rows=x, cols=y,color1='red',color2='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def board_color(x, y,color1,color2):
    return render_template("board.html", rows=x, cols=y,colr1=color1,colr2=color2)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
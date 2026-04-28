from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world!'

@app.route('/champion')
def champion():
    return 'Champion!'

@app.route('/say/<name>')
def say(name):
    return f'Hi {name}!'

@app.route('/repeat/<number>/<name>')
def repeat_name(number,name):
    num = int(number)
    result = ''
    for i in range(num):
        result += f'<p>{name}</p>'
    return result

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
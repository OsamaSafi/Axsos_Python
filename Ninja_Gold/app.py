from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_ninja_key' 

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form.get('building')
    gold_change = 0
    action = 'earned'
    
    if building == 'farm':
        gold_change = random.randint(10, 20)
    elif building == 'cave':
        gold_change = random.randint(5, 10)
    elif building == 'house':
        gold_change = random.randint(2, 5)
    elif building == 'casino':
        gold_change = random.randint(-50, 50) 
        if gold_change < 0:
            action = 'lost'
    session['gold'] += gold_change
    timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    
    if action == 'earned':
        activity_text = f"Earned {gold_change} golds from the {building}! ({timestamp})"
    else:
        activity_text = f"Entered a casino and lost {abs(gold_change)} golds... Ouch! ({timestamp})"
    
    session['activities'].insert(0, activity_text)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True ,port=5001)
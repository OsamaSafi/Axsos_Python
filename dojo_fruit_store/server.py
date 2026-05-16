from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = 'osama safi haker'
all_orders = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    session['first_name'] = request.form['first_name']
    current_order = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'student_id': request.form['student_id'],
        'strawberry': int(request.form.get('strawberry', 0)),
        'raspberry': int(request.form.get('raspberry', 0)),
        'apple': int(request.form.get('apple', 0))
    }
    all_orders.append(current_order)
    return redirect("/checkout-temb")

@app.route('/checkout-temb')
def checkoutTemb():
    return render_template('checkout.html',order = all_orders[len(all_orders)-1])


@app.route('/fruits')
def fruits():
    return render_template("fruits.html",orders=all_orders)

if __name__=="__main__":
    app.run(debug=True, port=5001)
from flask import Flask, render_template, request

app = Flask(__name__)

# Exchange rates
rates = {"USD": 1, "EUR": 0.99, "SAR": 3.75}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exchange', methods=['POST'])
def exchange():
    from_currency = request.form['from'].upper()
    to_currency = request.form['to'].upper()
    amount = float(request.form['amount'])
    
    if from_currency not in rates or to_currency not in rates:
        return render_template('result.html', result="Invalid currency input!")
    
    if from_currency == to_currency:
        result_text = f"You will keep your amount as it is: {amount} {from_currency}"
    else:
        new_amount = amount * (rates[to_currency] / rates[from_currency])
        result_text = f"You will give: {amount} {from_currency}, and you will take: {new_amount:.2f} {to_currency}"

    return render_template('result.html', result=result_text)
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form method="POST" action="/multiply">
        Enter First Number: <input type="number" name="num1"><br><br>
        Enter Second Number: <input type="number" name="num2"><br><br>
        <input type="submit" value="Multiply">
    </form>
    '''

@app.route('/multiply', methods=['POST'])
def multiply():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    product = num1 * num2

    return f"Product = {product}"

if __name__ == '__main__':
    app.run(debug=True)
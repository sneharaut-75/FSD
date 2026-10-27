from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        return f"Addition = {a+b}"
    return '''
    <form method="POST">
    Number 1: <input name="a"><br>
    Number 2: <input name="b"><br>
    <input type="submit">
    </form>
    '''
app.run(debug=True)

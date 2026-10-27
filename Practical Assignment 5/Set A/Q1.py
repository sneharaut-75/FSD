from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name = request.form['name']
        return f"Student Name: {name}"

    return '''
    <form method="POST">
    Name: <input name="name">
    <input type="submit">
    </form>
    '''

app.run(debug=True)

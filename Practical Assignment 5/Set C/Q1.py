from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        if name == 'admin':
            return "Login Successful"
        return "Invalid Username"

    return '''
    <form method="POST">
    Username: <input name="username">
    <input type="submit">
    </form>
    '''

app.run(debug=True)

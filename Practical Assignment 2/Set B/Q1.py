from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def login_form():
    return '''
    <form method="POST" action="/login">
        Username: <input type="text" name="username">
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    return f"Welcome {username}"

if __name__ == '__main__':
    app.run(debug=True)
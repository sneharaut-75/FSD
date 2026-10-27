from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            return "Login Successful"
        else:
            return "Invalid Username or Password"

    return '''
    <h2>Login Form</h2>
    <form method="POST">
        Username:
        <input type="text" name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <input type="submit" value="Login">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
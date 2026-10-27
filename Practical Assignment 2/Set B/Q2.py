from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        return "Submitted Student Name: " + name

    return '''
    <h2>Student Name Form</h2>
    <form method="POST">
        Enter Name:
        <input type="text" name="name">
        <input type="submit" value="Submit">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
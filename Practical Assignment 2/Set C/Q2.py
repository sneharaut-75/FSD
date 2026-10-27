from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        name = request.form["name"]
        return "Search Result: " + name

    return '''
    <h2>Student Search</h2>
    <form method="POST">
        Enter Student Name:
        <input type="text" name="name">
        <input type="submit" value="Search">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
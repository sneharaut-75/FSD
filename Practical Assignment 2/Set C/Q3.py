from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def library():
    if request.method == "POST":
        book = request.form["book"]
        return "Search Result: " + book

    return '''
    <h2>Library Search System</h2>
    <form method="POST">
        Enter Book Name:
        <input type="text" name="book">
        <input type="submit" value="Search">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
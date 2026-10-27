from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        comments = request.form['comments']
        return f"Name: {name}, Rating: {rating}, Comments: {comments}"
    return '''
    <form method="POST">
    Name: <input name="name"><br>
    Rating: <input name="rating"><br>
    Comments: <input name="comments"><br>
    <input type="submit">
    </form>
    '''
app.run(debug=True)

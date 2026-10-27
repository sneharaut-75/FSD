from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        name = request.form['name']
        eid = request.form['eid']
        salary = request.form['salary']
        return f"Name: {name}, ID: {eid}, Salary: {salary}"
    return '''
    <form method="POST">
    Name: <input name="name"><br>
    ID: <input name="eid"><br>
    Salary: <input name="salary"><br>
    <input type="submit">
    </form>
    '''
app.run(debug=True)

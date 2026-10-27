from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def employee():
    emp = [
        {"id": 1, "name": "Sujit", "salary": 30000},
        {"id": 2, "name": "Manisha", "salary": 35000},
        {"id": 3, "name": "Aarti", "salary": 26000},
        {"id": 4, "name": "Sneha", "salary": 23000},
        {"id": 5, "name": "Mona", "salary": 29000}
    ]
    return render_template("employee.html", emp=emp)

if __name__ == '__main__':
    app.run(debug=True)

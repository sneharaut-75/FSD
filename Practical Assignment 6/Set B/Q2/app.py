from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def employees():
    emp = [
        {"id": 1, "name": "Sneha", "salary": 20000},
        {"id": 2, "name": "Reva", "salary": 25000},
        {"id": 3, "name": "Sanu", "salary": 22000},
        {"id": 4, "name": "Namita", "salary": 30000},
        {"id": 5, "name": "Aaru", "salary": 28000}
    ]
    return render_template("employees.html", emp=emp)

if __name__ == '__main__':
    app.run(debug=True)

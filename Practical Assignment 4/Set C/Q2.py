from flask import Flask

app = Flask(__name__)

@app.route('/employee/<name>')
def employee(name):
    return f"Welcome {name}, have a nice day!"

if __name__ == '__main__':
    app.run(debug=True)
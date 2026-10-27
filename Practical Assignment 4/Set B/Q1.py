from flask import Flask

app = Flask(__name__)

@app.route('/student/<name>')
def student(name):
    return f"Student Name: {name}"

if __name__ == '__main__':
    app.run(debug=True)
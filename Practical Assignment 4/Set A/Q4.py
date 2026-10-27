from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to College Home Page"

@app.route('/student')
def student():
    return "Welcome Students"

@app.route('/faculty')
def faculty():
    return "Welcome Faculty Members"

if __name__ == '__main__':
    app.run(debug=True)
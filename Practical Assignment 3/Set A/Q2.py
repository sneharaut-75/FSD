from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    return "Name: Sneha Shivaji Raut<br>Roll No: 54"

app.run(debug=True)
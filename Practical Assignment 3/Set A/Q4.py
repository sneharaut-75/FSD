from flask import Flask

app = Flask(__name__)

@app.route('/')
def students():
    return "Hello, Students"

app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def department():
    return "Welcome to the B.Sc. Information Technology Department."

if __name__ == '__main__':
    app.run(debug=True)
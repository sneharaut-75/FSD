from flask import Flask

app = Flask(__name__)

@app.route('/contact')
def contact():
    return "Contact Us: college@gmail.com"

@app.route('/services')
def services():
    return "Our Services Page"

if __name__ == '__main__':
    app.run(debug=True)
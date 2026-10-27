from flask import Flask

app = Flask(__name__)

@app.route('/course/<coursename>')
def course(coursename):
    return f"Information about {coursename} course"

if __name__ == '__main__':
    app.run(debug=True)
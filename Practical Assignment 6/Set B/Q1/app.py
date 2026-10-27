
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student():
    student = {
        "name": "Sneha",
        "rollno": 101,
        "course": "BSc IT",
        "marks": 85
    }
    return render_template("student.html", student=student)

if __name__ == '__main__':
    app.run(debug=True)

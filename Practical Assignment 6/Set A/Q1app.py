from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def student():
    name = "Sneha"
    marks = [80, 85, 90]

    total = sum(marks)
    average = total / len(marks)

    return render_template("student.html",
                           name=name,
                           marks=marks,
                           total=total,
                           average=average)

if __name__ == '__main__':
    app.run(debug=True)

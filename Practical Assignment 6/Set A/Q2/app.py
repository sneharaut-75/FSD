from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    names = ["Sneha", "Sonu", "Ravi", "Manu", "Reva"]
    return render_template("student.html", names=names)

if __name__ == '__main__':
    app.run(debug=True)

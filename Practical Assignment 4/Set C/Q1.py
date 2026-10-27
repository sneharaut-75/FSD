from flask import Flask

app = Flask(__name__)

@app.route('/product/<int:id>')
def product(id):
    return f"Product Details for Product ID: {id}"

if __name__ == '__main__':
    app.run(debug=True)
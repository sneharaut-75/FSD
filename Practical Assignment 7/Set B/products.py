from flask import Flask, request, jsonify
app = Flask(__name__)
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 15000},
    {"name": "Keyboard", "price": 1000}
]
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/addproduct', methods=['POST'])
def add_product():
    data = request.get_json()
    products.append(data)

    return jsonify({
        "message": "Product added successfully",
        "product": data
    })

if __name__ == '__main__':
    app.run(debug=True)
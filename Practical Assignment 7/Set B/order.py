from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()

    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    total = price * quantity

    return jsonify({
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total
    })

if __name__ == '__main__':
    app.run(debug=True)
    
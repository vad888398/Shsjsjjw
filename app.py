from flask import Flask, render_template, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Товары
products = [
    {"id": 1, "name": "Электронная книга", "price": 500, "description": "Удобная книга в электронном формате.", "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Музыкальный альбом", "price": 300, "description": "Лучшие треки вашего любимого исполнителя.", "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Программное обеспечение", "price": 1200, "description": "Полезная программа для вашего устройства.", "image": "https://via.placeholder.com/150"},
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total_price = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total_price=total_price)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = int(request.json["id"])
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart = session.get("cart", [])
        cart.append(product)
        session["cart"] = cart
    return jsonify({"status": "success"})

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        session["theme"] = request.json.get("theme", "light")
        return jsonify({"status": "success"})
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)

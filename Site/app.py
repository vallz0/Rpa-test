from flask import Flask, render_template, request, jsonify
from product_manager import ProductManager
import os

app = Flask(__name__)

DATA_FILE = os.path.join("data", "products.json")

product_manager = ProductManager(DATA_FILE)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/api/products", methods=["POST"])
def add_product():
    product = request.json
    response = product_manager.add_product(product)
    return jsonify(response), 201

@app.route("/api/products", methods=["DELETE"])
def clear_products():
    response = product_manager.clear_products()
    return jsonify(response), 200

@app.route("/api/products", methods=["GET"])
def get_products():
    products = product_manager.get_products()
    return jsonify(products)

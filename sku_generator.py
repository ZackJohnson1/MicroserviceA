from flask import Flask, request, jsonify
import random
import string


app = Flask(__name__)


generated_skus = set()


def generate_unique_sku(prefix=""):
    """This function generates a unique SKU (optional prefix)."""
    while True:
        sku = prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8 - len(prefix)))
        if sku not in generated_skus:
            generated_skus.add(sku)
            return sku


@app.route('/')
def home():
    """This function defines a simple GET endpoint to ensure uptime."""
    return "SKU Generator Microservice is running. Use /generateSKU with a POST request to generate SKUs."


@app.route('/generateSKU', methods=['POST'])
def generate_sku():
    """This function is the API endpoint for the SKU."""
    data = request.get_json()   
    if data is None:
        return jsonify({"error": "Invalid or missing JSON data"}), 400
    prefix = data.get("prefix", "")
    if len(prefix) >= 8:
        return jsonify({"error": "Prefix too long"}), 400
    sku = generate_unique_sku(prefix)
    return jsonify({"sku": sku})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)

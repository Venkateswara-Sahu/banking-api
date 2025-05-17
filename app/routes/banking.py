from flask import Blueprint, jsonify, request

banking_bp = Blueprint("banking", __name__)

@banking_bp.route("/balance", methods=["GET"])
def get_balance():
    return jsonify({"balance": 5000.00}), 200

@banking_bp.route("/deposit", methods=["POST"])
def deposit():
    amount = request.json.get("amount")
    if not amount or amount <= 0:
        return jsonify({"error": "Invalid deposit amount"}), 400
    return jsonify({"message": f"Deposited {amount} successfully"}), 200

@banking_bp.route("/withdraw", methods=["POST"])
def withdraw():
    amount = request.json.get("amount")
    if not amount or amount <= 0:
        return jsonify({"error": "Invalid withdrawal amount"}), 400
    if amount > 5000:
        return jsonify({"error": "Insufficient balance"}), 400
    return jsonify({"message": f"Withdrew {amount} successfully"}), 200

# New route for /accounts
@banking_bp.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json()
    name = data.get("name")
    balance = data.get("balance")

    if not name or not isinstance(balance, (int, float)) or balance < 0:
        return jsonify({"error": "Invalid account data"}), 400

    # In real app, you'd save to DB. Here we just return the data.
    new_account = {
        "name": name,
        "balance": balance,
        "id": 1  # You can generate or auto increment this if needed
    }
    return jsonify(new_account), 201


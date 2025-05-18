from flask import Flask, jsonify
from banking_api.app.routes.banking import banking_bp

app = Flask(__name__)

app.register_blueprint(banking_bp)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "message": "Banking API is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
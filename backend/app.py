from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "🚀 NoirPent API is running."

@app.route('/recon', methods=['POST', 'GET'])
def recon():
    return jsonify({"status": "Recon started"}), 200

@app.route('/vulnscan', methods=['POST', 'GET'])
def vulnscan():
    return jsonify({"status": "Vulnerability scan started"}), 200

@app.route('/attack', methods=['POST', 'GET'])
def attack():
    return jsonify({"status": "Attack launched"}), 200

@app.route('/payload', methods=['POST', 'GET'])
def payload():
    return jsonify({"status": "Payload generated"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


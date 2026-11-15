from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def home():
    return "ROHIT AUTO FORWARDER backend starter is running."

@app.get("/api/status")
def status():
    return jsonify(status="not_configured", message="Connect a secured forwarding worker first.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

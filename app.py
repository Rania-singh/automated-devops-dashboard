from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"project": "CloudDevOps CI/CD Demo", "status": "running", "message": "Python application is healthy"})

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

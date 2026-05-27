from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "Application running successfully on EKS"
    })

@app.route("/health")
def health():
    return jsonify({
        "health": "ok"
    })

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", "5432")
        )

        conn.close()

        return jsonify({
            "database": "connected successfully"
        })

    except Exception as e:
        return jsonify({
            "database": "connection failed",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
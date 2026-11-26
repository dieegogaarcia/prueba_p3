import os
import socket
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

#Lo hace automáticamente el navegador al entrar a la web
@app.route("/")
def inicio():
    return send_from_directory(".", "index.html")

#Se hace en comprobarEntorno en index.html
@app.route("/api/status")
def status():
    return jsonify({
        "entorno": "Flask (Python)",
        "host": socket.gethostname()
    })

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
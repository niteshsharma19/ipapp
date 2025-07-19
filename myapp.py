from flask import Flask
import socket

app = Flask(__name__)

@app.route("/home")
def lwguest():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)  # ✅ corrected variable
    return f"Welcome to linuxworld <br /> My hostname : {hostname} <br /> My IP : {IPAddr}"

app.run(host="0.0.0.0", port=5000)


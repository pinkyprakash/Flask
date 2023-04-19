import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Request sent to server and Server responded with message '\n' Welcome to python world"

@app.route("/hi")
def hello():
    return 'Hello!,'

if __name__ == "__main__":
    app.run()


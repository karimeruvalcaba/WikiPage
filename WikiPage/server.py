from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/getTest", methods=["GET"])
def get_text_file():
    return send_file('data.txt', mimetype='text/plain')

if __name__ == "__main__":
    app.run()

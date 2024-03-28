from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/getTest", methods=["GET"])
def get_text_file():
    return send_file('data.txt', mimetype='text/plain')


from flask import request, jsonify

@app.route("/postTest", methods=["POST"])
def test_post():
    if request.method == "POST":
        favorite_character = request.json.get('favorite_character')  # Assuming JSON data
        if favorite_character:
            if favorite_character.lower() == "sherlock":
                response = {"message": "Your favorite character is Sherlock."}
            elif favorite_character.lower() == "moriarty":
                response = {"message": "Your favorite character is Moriarty."}
            else:
                return jsonify({"message": "error", "reason": "Invalid option provided"}), 400
            print("Received POST request with favorite character:", favorite_character)  # Print received data
            return jsonify(response)
        else:
            return jsonify({"message": "error", "reason": "favorite_character is missing"}), 400
    else:
        return jsonify({"message": "error", "reason": "Method Not Allowed"}), 405


if __name__ == "__main__":
    app.run()

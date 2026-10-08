
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "response": "Please send a valid question."
        }), 400

    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({
            "response": "The question must be text."
        }), 400

    if len(message) > 2000:
        return jsonify({
            "response": "Please shorten your question."
        }), 400

    response = get_response(message)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)

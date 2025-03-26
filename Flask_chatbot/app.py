from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["msg"]
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

def generate_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there!",
        "how are you": "I'm a bot, so I'm always fine!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure how to respond to that."
    }

    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

if __name__ == "__main__":
    app.run(debug=True)
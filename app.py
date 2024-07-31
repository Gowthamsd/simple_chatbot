from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Chatbot:
    def __init__(self):
        self.context = {}

    def remember(self, key, value):
        self.context[key] = value

    def recall(self, key):
        return self.context.get(key, None)

    def greet(self):
        return "Hello! How can I help you today?"

    def respond_to_question(self, question):
        responses = {
            "hi":"hello Boz",
            "how are you?": "I'm just a chatbot, but I'm here to help you!",
            "what is your name?": "I'm your friendly chatbot.",
            "what can you do?": "I can chat with you and remember our previous conversations.",
            "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "what's the weather like?": "I can't check the weather, but I hope it's nice where you are!"
        }
        return responses.get(question.lower(), "I'm sorry, I don't understand that question.")

    def farewell(self):
        return "Goodbye! Have a great day!"

    def handle_error(self, input_text):
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

chatbot = Chatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond_to_question(user_input)
    if response == "I'm sorry, I don't understand that question.":
        response = chatbot.handle_error(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

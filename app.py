from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import chart_generator

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
cors = CORS(app, resources={r"/api/chat": {"origins": "http://localhost:3000/"}})

def generate_bot_response(user_input):
    # Add your logic here to generate a response based on user input
    # Replace this with the desired behavior of your chatbot
    if user_input.lower() == 'hello':
        return "Hello! How can I help you?"
    elif user_input.lower() == 'bye':
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '').strip()

    if user_input:
        bot_response = generate_bot_response(user_input)
        return jsonify({"message": bot_response})
    else:
        return jsonify({"message": "Please provide a valid input."})

if __name__ == '__main__':
    app.run(debug=True)

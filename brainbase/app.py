from doctest import debug
from flask import Flask, jsonify, request
from src.chatbot import query_openai, call_api
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/call_chatbot', methods=["GET"])
def call_chatbot():
    user_input = request.args.get("messages")
    if user_input:
        messages = json.loads(user_input)
        text_contents = []
        for message in messages:
            if message["role"] == "user":
                for content in message["content"]:
                    if content["type"] == "text":
                        text_contents.append(content["text"])
                        
        intent, params = query_openai(text_contents[-1])
        result = call_api(intent, params)
        return jsonify(result), 200
    else:
        return "No user input detected", 400
    
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

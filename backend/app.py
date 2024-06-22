from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from llms import get_gpt_response, get_llama_response, get_claude_response

app = Flask(__name__)
CORS(app)

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res

@app.route('/get-responses', methods=['POST'])
def get_responses():
    data = request.json
    prompt = data['prompt']
    
    # Get initial responses
    gpt_response = get_gpt_response(prompt)
    llama_response = get_llama_response(prompt)
    claude_response = get_claude_response(prompt)
    
    responses = {
        'GPT': gpt_response,
        'LLaMa': llama_response,
        'Claude': claude_response
    }
    
    # Collect votes
    votes = {'GPT': 0, 'LLaMa': 0, 'Gemini': 0}
    
    for model_name, model_response in responses.items():
        combined_prompt = f"Original prompt: {prompt}\n\nResponses:\n1. {gpt_response}\n2. {llama_response}\n3. {claude_response}\n\nWhich is the best response?"
        if model_name == 'GPT':
            vote = get_gpt_response(combined_prompt)
        elif model_name == 'LLaMa':
            vote = get_llama_response(combined_prompt)
        elif model_name == 'Gemini':
            vote = get_claude_response(combined_prompt)
        
        votes['GPT'] += 1
    
    # Determine the winner
    winner = max(votes, key=votes.get)
    
    return jsonify({'winner': winner, 'response': responses[winner]})

if __name__ == '__main__':
    app.run(debug=True)
"""
Flask Web Application for FAQ Chatbot
Provides a web interface for the chatbot with modern UI
"""

from flask import Flask, render_template, request, jsonify, session
from chatbot import FAQChatbot
import json
import os
import numpy as np

app = Flask(__name__)
app.secret_key = 'faq_chatbot_secret_key_2024'

class NumpyEncoder(json.JSONEncoder):
    """Custom JSON encoder for numpy data types"""
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

app.json_encoder = NumpyEncoder

# Initialize chatbot
try:
    chatbot = FAQChatbot()
    print("✅ Chatbot initialized successfully")
except Exception as e:
    print(f"❌ Error initializing chatbot: {e}")
    import traceback
    traceback.print_exc()
    chatbot = None

@app.route('/')
def index():
    """Main page with chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and return responses"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'message': 'Please enter a message'
            })
        
        if chatbot is None:
            return jsonify({
                'success': False,
                'message': 'Chatbot is not available. Please restart the server.'
            })
        
        # Get chatbot response
        response = chatbot.get_response(user_message)
        
        # Ensure all values are JSON serializable
        processed_response = {
            'success': True,
            'response': str(response['answer']),
            'confidence': float(response['confidence']),
            'matched_question': str(response['matched_question']) if response['matched_question'] else None,
            'is_match': bool(response['is_match']),
            'debug_info': {
                'processed_question': str(response['debug_info']['processed_question']),
                'similarity_threshold': float(response['debug_info']['similarity_threshold']),
                'top_matches': [
                    {
                        'question': str(match['question']),
                        'similarity': float(match['similarity']),
                        'index': int(match['index'])
                    }
                    for match in response['debug_info'].get('top_matches', [])
                ]
            }
        }
        
        return jsonify(processed_response)
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'message': f'Error processing message: {str(e)}'
        })

# ... [rest of your routes remain unchanged] ...

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
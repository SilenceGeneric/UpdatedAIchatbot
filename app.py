import os
import json
import logging
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Flask app setup
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Default GPT model parameters
DEFAULT_PROMPT = "Hello, how can I help you today?"
DEFAULT_TEMPERATURE = 0.5
DEFAULT_MAX_TOKENS = 50
DEFAULT_ENGINE = "davinci"

# Load or create configuration
CONFIG_FILE = "static/config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "prompt": DEFAULT_PROMPT,
            "temperature": DEFAULT_TEMPERATURE,
            "max_tokens": DEFAULT_MAX_TOKENS,
            "engine": DEFAULT_ENGINE
        }

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

config = load_config()

# Routes
@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/generate-response', methods=['POST'])
def generate_response():
    try:
        input_text = request.json['input']
        logging.info(f"Received input: {input_text}")
        
        response = openai.Completion.create(
            engine=config["engine"],
            prompt=config["prompt"] + "\n" + input_text,
            temperature=config["temperature"],
            max_tokens=config["max_tokens"]
        )
        
        output_text = response.choices[0].text.strip()
        logging.info(f"Generated response: {output_text}")
        return jsonify({'response': output_text})
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/set-config', methods=['POST'])
def set_config():
    try:
        new_config = request.json
        config.update(new_config)
        save_config(config)
        logging.info(f"Configuration updated: {config}")
        return jsonify({'status': 'success'})
    except Exception as e:
        logging.error(f"Error updating config: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/get-config', methods=['GET'])
def get_config():
    return jsonify(config)

@app.route('/help', methods=['GET'])
def help():
    help_text = """
    Welcome to the AI Chatbot! Here are the available commands:
    - /generate-response (POST): Generate a response from the chatbot.
        Required data: {'input': 'your input text'}
    - /set-config (POST): Set configuration parameters.
        Required data: {'prompt': '...', 'temperature': 0.5, 'max_tokens': 50}
    - /get-config (GET): Get the current configuration.
    - /help (GET): Get this help message.
    """
    return help_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

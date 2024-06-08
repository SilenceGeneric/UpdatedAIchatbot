# UpdatedAIchatbot
# AI Chatbot Application

This is an AI Chatbot application built using Flask and OpenAI's GPT models. It allows users to interact with a chatbot and adjust its settings.

## Installation

### Prerequisites

- Python 3.x installed on your system
- OpenAI API key

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```
OPENAI_API_KEY=your-openai-api-key
```

### Set Up File Structure

```
project/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── config.json
├── templates/
│   └── index.html
└── app.py
```

### Run the Application

```bash
python app.py
```

The application should now be running on http://localhost:5000.

## Usage

- Open your web browser and go to http://localhost:5000.
- Adjust chatbot settings (prompt, temperature, max tokens, engine).
- Interact with the chatbot by entering text in the input field and clicking "Get Response".

## Features

- Adjust chatbot settings dynamically through the web interface.
- Generate responses from the chatbot based on user input.
- Save configuration settings for future use.


# LLM Chatbot Hipster

## Prerequisites

- Python version 3.9.13.

## Setup Instructions

1. **Clone the repository:**

   git clone https://github.com/faisalirulam/llm_chat_bot.git

2. **Navigate to the project directory:**

   cd hipster_chatbot_project

3. **Create and activate a virtual environment** (optional but recommended):

   python -m venv venv
   # For Windows
   venv\Scripts\activate
   # For Mac/Linux
   source venv/bin/activate

4. **Install the required dependencies:**

   pip install -r requirements.txt

5. **Run the server:**

   python manage.py runserver

6. **Access the application:**

   Open your browser and navigate to http://127.0.0.1:8000/ to see the application in action.

## Notes

- Ensure your Python version is correct by running python --version.
- Make sure .env present. Which wil be inside hipster_chatbot_project. In .env file one credential is using for groq llm call. Replace with yours for perfect running
- If the chatbot getting any irrelevant response please install sentence-transformers using **pip install sentence-transformers**

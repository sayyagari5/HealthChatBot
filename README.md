# AI-Powered Health Chatbot

A Python-based web application using Flask, OpenAI API (ChatGPT), pandas, MongoDB, and PubMed API
to provide personalized health advice. Deployed on Azure for scalability.

## Features
- Chatbot delivers health advice using ChatGPT, informed by user inputs and PubMed data.
 - Processes medical datasets with pandas for keyword extraction.
 - Stores user interactions securely in MongoDB.
 - Tested APIs with Postman and pytest for 98% uptime.
 ## Prerequisites
Python 3.10+
- MongoDB (local or MongoDB Atlas)
- OpenAI API Key (https://platform.openai.com)
- PubMed API Key (optional, https://www.ncbi.nlm.nih.gov/account/)
- Azure account for deployment
-  Postman for manual API testing
-  Git for version control
## Setup
1. Clone the repository:
```bash
 git clone https://github.com/sayyagari5/ai-health-chatbot.git
 cd ai-health-chatbot
 ```
2. Create a virtual environment and install dependencies:
 ```bash
 python -m venv venv
 source venv/bin/activate # On Windows: venv\Scripts\activate
 pip install -r requirements.txt
 ```
 3. Set up environment variables in `.env`:
 ```plaintext
 OPENAI_API_KEY=your_openai_api_key
 PUBMED_API_KEY=your_pubmed_api_key
 MONGODB_URI=your_mongodb_connection_string
 FLASK_SECRET_KEY=your_flask_secret_key
 ```
4. Run the application:
 ```bash
 python app.py
 ```
 5. Access at `http://localhost:5000`.
 6. Run tests:
 ```bash
 pytest tests/test_api.py
 ```
 7. Deploy to Azure:
 - Create an Azure App Service.
 - Configure deployment from GitHub via Azure Portal.
 - Set environment variables in Azure App Service configuration.

 ## Testing
 - Use Postman to test POST `/` with `user_input` and `user_id`.
 - Run `pytest` for automated API tests.
 ## GitHub
 Push updates to your GitHub repository:
 ```bash
 git add .
 git commit -m "Initial commit"
 git push origin main
 ```

 ## License
 MIT License

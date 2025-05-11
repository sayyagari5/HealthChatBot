from flask import Flask, request, render_template, jsonify
 from openai import OpenAI
 from pymongo import MongoClient
 from dotenv import load_dotenv
 import os
 import requests
 from utils.data_processor import process_user_input
 import pandas as pd

 app = Flask(__name__)
 load_dotenv()

 # Initialize OpenAI client
 openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

 # Initialize MongoDB client
 mongo_client = MongoClient(os.getenv("MONGODB_URI"))
 db = mongo_client["health_chatbot"]
 users_collection = db["users"]

 # PubMed API base URL
 PUBMED_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

 @app.route("/", methods=["GET", "POST"])
 def index():
 if request.method == "POST":
 user_input = request.form.get("user_input")
 user_id = request.form.get("user_id", "anonymous")

 # Process input with pandas
 processed_data = process_user_input(user_input)

 # Query PubMed for relevant articles
 pubmed_params = {
 "db": "pubmed",
 "term": processed_data["keywords"],
 "retmax": 3,
 "api_key": os.getenv("PUBMED_API_KEY"),
 "retmode": "json"
 }
 pubmed_response = requests.get(PUBMED_API, params=pubmed_params)
 pubmed_data = pubmed_response.json().get("esearchresult", {})
 article_ids = pubmed_data.get("idlist", [])

 # Generate ChatGPT response
 prompt = f"Based on user input: {user_input}, and PubMed articles {article_ids}, provide
health advice."
 chatgpt_response = openai_client.chat.completions.create(
 model="gpt-4o-mini",
 messages=[{"role": "user", "content": prompt}],
 max_tokens=200
 )
 advice = chatgpt_response.choices[0].message.content
   # Store user interaction in MongoDB
 users_collection.insert_one({
 "user_id": user_id,
 "input": user_input,
 "advice": advice,
 "timestamp": pd.Timestamp.now()
 })

 return jsonify({"advice": advice, "articles": article_ids})
 return render_template("index.html")

 if __name__ == "__main__":
 app.run(debug=True)

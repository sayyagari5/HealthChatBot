 import pytest
 from app import app

 @pytest.fixture
 def client():
 app.config["TESTING"] = True
 with app.test_client() as client:
 yield client

 def test_index_get(client):
 response = client.get("/")
 assert response.status_code == 200

 def test_index_post(client):
 response = client.post("/", data={"user_input": "headache", "user_id": "test_user"})
 assert response.status_code == 200
 assert "advice" in response.json

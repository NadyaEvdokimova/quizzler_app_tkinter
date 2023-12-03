import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
# Create a new list of questions
question_data = response.json()["results"]



import requests

# URL of your Flask app
url = "http://127.0.0.1:5000/predict"

# Data to send (JSON format)
data = {
    "Pclass": 2,
    "Sex": 1,
    "Age": 30,
    "Fare": 25.5
}

# Send POST request
response = requests.post(url, json=data)

# Print result
print("Prediction(1 = Survived || 0 = Did not survived):", response.json())


import requests


question_data = []
parameter = {
    "amount":10,
    "type":"boolean"
}

with requests.get("https://opentdb.com/api.php", params=parameter) as response:
    response.raise_for_status()
    data = response.json()["results"]
    for question in data:
        question_data.append(question)

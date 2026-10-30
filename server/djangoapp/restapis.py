
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    response = requests.get(
        backend_url + endpoint,
        params=kwargs
    )
    return response.json()


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    response = requests.get(request_url)
    return response.json()


def post_review(data_dict):
    response = requests.post(
        backend_url + "/insert_review",
        json=data_dict
    )
    return response.json()

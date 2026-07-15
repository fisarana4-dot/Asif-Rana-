import requests
import json
import os

API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateCon
 tent?key={API_KEY}"

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Hello from NEXRA V16000"
                }
            ]
        }
    ]
}

response = requests.post(url, json=data)
print(response.text)

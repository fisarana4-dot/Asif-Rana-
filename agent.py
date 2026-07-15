import requests
import os

API_KEY = os.getenv("GEMINI_API_KEY")

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + API_KEY
Then do nothing else for now
def ask_gemini(prompt):

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                

import google.generativeai as gemai
from dotenv import load_dotenv
import os

from flask import jsonify

load_dotenv()


gemai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = gemai.GenerativeModel(os.getenv("GEMINI_MODEL"))

class Gemini:
    def __init__(self, prompt):
        self.prompt = prompt

    def get_response(self):
        try:
            response = model.generate_content(self.prompt)

            if hasattr(response, "text"):
                return {"content": response.text}
            else:
                return {"content": str(response)}
        except Exception as e:
            return jsonify({"error": f"Something went wrong. {str(e)}"})
        return None



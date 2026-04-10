import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_openai_usage():
    try:
        # Dummy call just to check API status
        response = client.models.list()

        return {
            "status": "success",
            "message": "API reachable",
            "models_available": len(response.data)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

from fastapi import FastAPI
from app.services.openai_service import get_openai_usage
from app.services.tts_service import get_tts_usage
from app.services.stt_service import get_stt_usage

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Working"}

@app.get("/dashboard")
def dashboard():
    return {
        "openai": get_openai_usage(),
        "tts": get_tts_usage(),
        "stt": get_stt_usage()
    }
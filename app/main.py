from fastapi import FastAPI, Request, Form
from fastapi.responses import PlainTextResponse
import os
from dotenv import load_dotenv
from app.whatsapp import send_whatsapp_message
from app.ai import get_eco_tip

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Eco-Chatbot is running!"}

@app.get("/eco-tip")
def eco_tip():
    tip = get_eco_tip()
    return {"eco_tip": tip}

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    from_number = form.get("From")
    body = form.get("Body")
    if from_number and body:
        if body.strip().lower() in ["tip", "eco-tip", "eco tip", "daily tip", "eco"]:
            reply = get_eco_tip()
        else:
            reply = f"You said: {body}"
        send_whatsapp_message(from_number, reply)
    return PlainTextResponse("OK")

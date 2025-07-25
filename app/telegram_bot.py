import os
from fastapi import APIRouter, Request
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.constants import ParseMode

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_BOT_TOKEN)
router = APIRouter()

def get_eco_tip():
    # Replace with your actual eco-tip logic or AI call
    return "🌱 Eco Tip: Turn off lights when not in use to save energy!"

@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot)
    chat_id = update.message.chat.id if update.message else None
    text = update.message.text.lower() if update.message and update.message.text else ""

    if chat_id:
        if text in ["tip", "eco-tip", "eco tip", "daily tip", "eco"]:
            tip = get_eco_tip()
            await bot.send_message(chat_id=chat_id, text=tip, parse_mode=ParseMode.HTML)
        else:
            await bot.send_message(chat_id=chat_id, text="Send 'tip' or 'eco tip' for a daily eco-tip!")

    return {"ok": True}

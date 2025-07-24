# Eco-Chatbot (Python + FastAPI + WhatsApp)

## Overview
This project is an AI-powered chatbot that delivers daily eco-tips and promotes sustainable living, integrated with WhatsApp using Twilio and built with FastAPI.

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file in the root directory with your Twilio credentials and any other secrets:
     ```env
     TWILIO_ACCOUNT_SID=your_account_sid
     TWILIO_AUTH_TOKEN=your_auth_token
     TWILIO_WHATSAPP_NUMBER=whatsapp:+1234567890
     ```

4. **Run the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Expose your local server to the internet** (for Twilio webhooks)
   - Use [ngrok](https://ngrok.com/) or similar:
     ```bash
     ngrok http 8000
     ```
   - Set the webhook URL in your Twilio console to `https://<ngrok-url>/webhook`

6. **Test WhatsApp integration**
   - Send a message to your Twilio WhatsApp sandbox number and check the server logs.

## Next Steps
- Implement Twilio webhook logic in `app/main.py`
- Add AI/NLP integration for eco-tips and Q&A
- Set up a scheduler for daily tips
- Connect a database for user data 
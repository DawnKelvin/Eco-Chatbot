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

---

# Project Roadmap & Guidance

## 1. Project Roadmap

### Phase 1: Planning & Requirements
- Define chatbot goals: daily eco-tips, green choice promotion, sustainable living guidance.
- Identify target platforms: Web, Mobile, WhatsApp, Telegram, etc.
- List core features:  
  - Daily eco-tip delivery  
  - Q&A on eco-friendly habits  
  - Personalized suggestions  
  - User engagement (reminders, streaks, quizzes)  
  - Feedback collection

### Phase 2: Design
- Design conversation flows (greetings, tips, Q&A, fallback, etc.)
- Create eco-tip content database (curate or generate tips)
- Plan user data handling (privacy, personalization)

### Phase 3: Development
#### 3.1 Backend
- Set up server (Node.js/Express, Python/FastAPI, or similar)
- Integrate AI/NLP (OpenAI GPT, Google Dialogflow, Rasa, or Hugging Face)
- Build eco-tip scheduler and delivery logic
- Set up database (MongoDB, PostgreSQL, Firebase, etc.)

#### 3.2 Frontend / Chat Interface
- Web: React.js, Vue.js, or plain HTML/CSS/JS
- Messaging: Integrate with WhatsApp (Twilio), Telegram, Messenger, etc.
- Mobile: React Native, Flutter (optional)

#### 3.3 AI/NLP Integration
- Use pre-trained models (OpenAI GPT-3.5/4, Hugging Face Transformers)
- Fine-tune for eco-domain (optional)
- Intent recognition for Q&A and guidance

#### 3.4 Personalization & Engagement
- User profiles (preferences, history)
- Tip customization
- Gamification (badges, streaks)

### Phase 4: Testing
- Unit and integration tests
- User testing for conversation quality
- Feedback loop for improvement

### Phase 5: Deployment
- Deploy backend (Heroku, AWS, Azure, Vercel, etc.)
- Deploy frontend/chat interface
- Set up monitoring and analytics

### Phase 6: Maintenance & Iteration
- Regularly update eco-tips
- Improve AI responses based on feedback
- Add new features (e.g., eco challenges, community features)

---

## 2. Recommended Tools & Frameworks

| Purpose                | Tool/Framework                |
|------------------------|------------------------------|
| Backend API            | FastAPI or Flask             |
| Database               | MongoDB, PostgreSQL, SQLite  |
| Scheduler              | APScheduler, Celery          |
| WhatsApp Integration   | Twilio API for WhatsApp      |
| AI/NLP                 | OpenAI API, Hugging Face     |
| Testing                | pytest                       |
| Deployment             | Heroku, Railway, AWS, Azure  |
| Environment Variables  | python-dotenv                |

---

## 3. Example Architecture Diagram

```
graph TD
  User("User (WhatsApp)") -->|Message| Twilio
  Twilio -->|Webhook| FastAPI
  FastAPI -->|Query| OpenAI
  FastAPI -->|DB| MongoDB
  FastAPI -->|Send| Twilio
  FastAPI -->|Scheduler| APScheduler
```

---

## 4. .env File Example

```
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Twilio Credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_WHATSAPP_NUMBER=whatsapp:+1234567890
```

---

## 5. Deployment Instructions

### 1. Choose a Hosting Platform
Popular options for FastAPI apps:
- Railway (easy, free tier, supports background tasks)
- Render (easy, free tier)
- Heroku (classic, but free tier is limited)
- AWS (EC2, Elastic Beanstalk)
- Azure App Service
- Google Cloud Run
- DigitalOcean App Platform

For most users, Railway or Render is the easiest.

### 2. Prepare Your Project for Deployment
- Ensure your code is in a GitHub repo.
- Your `requirements.txt` is up to date.
- Your `.env` file is ready (but do not commit it to GitHub! Set env vars in the platform dashboard).
- Your FastAPI app is exposed as `app` in `app/main.py`.

### 3. Deploying on Railway (Recommended for Beginners)
1. Sign up at [Railway](https://railway.app/) and link your GitHub repo.
2. Create a new project and select your repo.
3. Set environment variables in the Railway dashboard (`OPENAI_API_KEY`, `TWILIO_ACCOUNT_SID`, etc.).
4. Configure the start command (Railway auto-detects FastAPI, but you can set it manually):
   ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
5. Deploy! Railway will build and run your app. You’ll get a public URL.

### 4. Expose Your Webhook to Twilio
- Twilio needs a public HTTPS endpoint for webhooks.
- Use your Railway/Render/Heroku public URL, e.g.:
  ```
  https://your-app-name.up.railway.app/webhook
  ```
- Set this as your WhatsApp webhook in the Twilio console.

### 5. Set Environment Variables
- In your hosting platform’s dashboard, add all required environment variables from your `.env` file.

### 6. Test Your Bot
- Send a WhatsApp message to your Twilio sandbox number.
- Check logs in your hosting platform for errors or confirmation.

### 7. (Optional) Custom Domain
- Most platforms let you add a custom domain if you want a branded URL.

### Summary Table

| Step                | What to Do                                      |
|---------------------|-------------------------------------------------|
| 1. Choose Host      | Railway, Render, Heroku, etc.                   |
| 2. Prepare Code     | requirements.txt, .env, FastAPI app             |
| 3. Deploy           | Connect repo, set env vars, deploy              |
| 4. Webhook          | Set Twilio webhook to your deployed URL         |
| 5. Test             | Send WhatsApp message, check logs               |

---

## 6. AI-Powered Eco-Tips Integration
- The `/eco-tip` endpoint returns an AI-generated eco-tip.
- WhatsApp users can text "tip", "eco-tip", "eco tip", "daily tip", or "eco" to receive a fresh AI-generated eco-tip.
- All other messages are echoed back.

---

## 7. Next Steps
- Add your OpenAI API key to your `.env` file.
- Install dependencies: `pip install -r requirements.txt`
- Run the server: `uvicorn app.main:app --reload`
- Use ngrok to expose your local server and set the webhook URL in Twilio.
- Test the WhatsApp echo and eco-tip functionality.
- Expand with features like daily scheduled tips or user personalization as needed.

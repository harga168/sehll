from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return "Bot kamu sudah aktif!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text == "/start":
            reply = "🔥 Bot kamu sudah aktif!"
        elif text == "/insightdaily":
            reply = "📊 Insight crypto & saham akan tampil di sini!"
        else:
            reply = "❓ Perintah tidak dikenali."

        requests.post(URL, json={"chat_id": chat_id, "text": reply})
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

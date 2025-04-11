from flask import Flask, request
import requests
import os
import threading
from datetime import datetime

# Import modul data fetcher
from fetch_unlocks import get_unlocks
from fetch_news import get_crypto_news
from fetch_macro import get_macro_news
from fetch_coingecko import get_token_price

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# =====================
# 🔁 AUTO PUSH setiap 6 jam
# =====================
def push_insight():
    now = datetime.now().strftime("%d-%m-%Y %H:%M")
    message = (
        f"📊 [AUTO INSIGHT] ({now})\n"
        "🔥 Trending: $TIA, $ARB, $LDO\n"
        "🔓 Unlock Aktif: ARB, LDO\n"
        "🧠 Narrative: Modular, Restaking, AI\n"
        "📈 Whale inflow: +$2.3M ($LDO)"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    threading.Timer(21600, push_insight).start()

push_insight()

@app.route('/')
def home():
    return "✅ BOT CRYPTO OTOMATIS AKTIF!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()
        print("✅ Chat ID =>", chat_id)

        # === Command handler
        if text in ["/start", "/start@risetdatacrypto_bot"]:
            reply = (
                "✅ Bot Crypto 24/7 AKTIF!\n\n"
                "📌 Commands:\n"
                "/insightdaily\n/score ETH\n/wallet BTC\n"
                "/unlocktoday\n/news\n/macro\n/price ETH\n/btcsource\n/push"
            )

        elif text in ["/insightdaily", "/insightdaily@risetdatacrypto_bot"]:
            reply = (
                "📊 Insight Hari Ini:\n"
                "🔥 $TIA, $ARB, $OP trending\n"
                "🔓 Unlock ARB 5.1% besok\n"
                "📈 Whale inflow: $LDO\n"
                "🧠 Narrative: Modular + AI"
            )

        elif text.startswith("/score"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📈 Skor {token}:\nTA: 86 | FA: 84 | Narrative: Modular"

        elif text.startswith("/wallet"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📡 Wallet {token}:\nWhale inflow +$1.5M\nNew holders naik +3%"

        elif text in ["/unlocktoday", "/unlocktoday@risetdatacrypto_bot"]:
            reply = get_unlocks()

        elif text in ["/news", "/news@risetdatacrypto_bot"]:
            reply = get_crypto_news()

        elif text in ["/macro", "/macro@risetdatacrypto_bot"]:
            reply = get_macro_news()

        elif text.startswith("/price"):
            token = text.split(" ")[1].lower() if len(text.split()) > 1 else "ethereum"
            reply = get_token_price(symbol=token)

        elif text in ["/btcsource", "/btcsource@risetdatacrypto_bot"]:
            reply = (
                "📘 BTC Resource:\n"
                "- mempool.space\n- blockchair.com\n"
                "- rainbow chart\n- halving: bitcoinblockhalf.com\n- bitbo.io"
            )

        elif text == "/push":
            reply = (
                "🚀 Push Manual:\n"
                "📊 Token: $TIA breakout\n"
                "🔓 Unlock aktif: ARB, OP\n"
                "🧠 Trending: Modular + ZK"
            )

        else:
            reply = "❓ Command tidak dikenali. Ketik /start untuk daftar lengkap."

        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

# === Endpoint manual ping
@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 PUSH:\n📊 $TIA breakout\n🔓 MANTA unlock besok\n🧠 Narrative: Modular + RWA"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Push terkirim!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

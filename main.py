from flask import Flask, request
import requests
import os
import threading

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")  # Ganti secara manual jika belum pakai .env
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# 🔁 Fungsi push insight otomatis tiap 6 jam
def push_insight():
    message = (
        "📊 AUTO PUSH – Insight Harian:\n"
        "🔥 Top Token: TIA, OP, MANTA\n"
        "🔓 Unlock Alert: ARB besok 4.5%\n"
        "🧠 Narrative Aktif: Modular, AI, Restaking\n"
        "📈 Rekomendasi: Swing Zone ARB $1.12 – Target $1.45"
    )
    requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    # Ulangi setiap 6 jam
    threading.Timer(21600, push_insight).start()

# 🚀 Aktifkan auto-push saat server hidup
push_insight()

@app.route('/')
def home():
    return "✅ Bot Telegram kamu AKTIF!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()

        if text == "/start":
            reply = (
                "✅ Bot Siap Digunakan!\n"
                "/insightdaily – Insight harian\n"
                "/score ETH – Skor token\n"
                "/wallet BTC – Whale tracker\n"
                "/airdropwatch – Airdrop aktif\n"
                "/unlockrisk – Unlock token mingguan"
            )

        elif text == "/insightdaily":
            reply = (
                "📊 Insight Hari Ini:\n"
                "🔥 TIA, OP, LDO trending\n"
                "📈 Whale masuk: $LDO, $FET\n"
                "🧠 Narrative aktif: AI, Modular"
            )

        elif text.startswith("/score"):
            token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
            reply = f"📈 Skor Analisis {token}:\nTA: 85 | FA: 88 | Narrative: Modular"

        elif text.startswith("/wallet"):
            token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
            reply = f"📡 Whale Tracker {token}:\nNew Wallets +4.2% | Whale inflow: +$1.8M"

        elif text == "/airdropwatch":
            reply = (
                "🎁 Airdrop Radar:\n"
                "- zkSync\n"
                "- AltLayer\n"
                "- LayerZero"
            )

        elif text == "/unlockrisk":
            reply = (
                "🔓 Unlock Watch:\n"
                "- $ARB: 5.1% unlock besok\n"
                "- $MANTA: vesting schedule aktif"
            )

        elif text == "/btcsource":
            reply = (
                "📘 Bitcoin Toolkit:\n"
                "- mempool.space\n"
                "- blockchain.com\n"
                "- bitbo.io\n"
                "- bitcoinblockhalf.com"
            )

        else:
            reply = "❓ Perintah tidak dikenali. Coba ketik /start"

        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 PUSH MANUAL:\n"
        "📊 TIA breakout MA200\n"
        "🔓 MANTA unlock besok\n"
        "🧠 AI Narrative +19% volume"
    )
    requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Pushed to Telegram!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

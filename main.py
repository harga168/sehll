from flask import Flask, request
import requests
import os
import threading

app = Flask(__name__)

# Ambil token bot dari environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
# Ganti dengan chat_id kamu sendiri untuk auto-push (contoh: -1001234567890 atau user ID kamu)
CHAT_ID = os.environ.get("CHAT_ID")  # → kamu bisa set ini di Render environment

# =========================
# AUTO PUSH FUNGSIONAL
# =========================
def push_insight():
    message = (
        "📊 AUTO PUSH – Insight Harian:\n"
        "🔥 Top Token: TIA, OP, MANTA\n"
        "🔓 Unlock Alert: ARB besok 4.5%\n"
        "🧠 Narrative Aktif: Modular, AI, Restaking\n"
        "📈 Rekomendasi: Swing Zone ARB $1.12 – Target $1.45"
    )
    requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    # Jadwalkan ulang setiap 6 jam (3600*6 = 21600 detik)
    threading.Timer(21600, push_insight).start()

# Jalankan otomatis saat bot start
push_insight()

# =========================
# HALAMAN UTAMA & WEBHOOK
# =========================
@app.route('/')
def home():
    return "Bot Telegram kamu aktif & jalan otomatis!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()

        if text == "/start":
            reply = (
                "✅ Bot Siap Digunakan!\n"
                "Perintah yang tersedia:\n"
                "/insightdaily – Insight otomatis harian\n"
                "/score ETH – Skor token\n"
                "/wallet BTC – Whale tracker\n"
                "/airdropwatch – Potensi airdrop\n"
                "/unlockrisk – Token unlock terdekat"
            )

        elif text == "/insightdaily":
            reply = (
                "📊 Insight Harian:\n"
                "🔥 TIA – Modular boom\n"
                "🔍 MANTA – Unlock selesai\n"
                "💼 LDO – Whale inflow +$2M"
            )

        elif text.startswith("/score"):
            token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
            reply = f"📈 Skor Analisis {token}:\nTA: 86 | FA: 84 | VC Score: 92"

        elif text.startswith("/wallet"):
            token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
            reply = f"📡 Whale Tracker {token}:\nHolder aktif naik +3.2%, whale masuk $1.1M"

        elif text == "/airdropwatch":
            reply = (
                "🎁 Airdrop Aktif:\n"
                "- zkSync\n"
                "- LayerZero\n"
                "- AltLayer"
            )

        elif text == "/unlockrisk":
            reply = (
                "🔓 Unlock Token:\n"
                "- ARB: 4.5% besok\n"
                "- LAVA: 3.2% hari ini"
            )

        elif text == "/btcsource":
            reply = (
                "📘 Sumber Data Bitcoin:\n"
                "- mempool.space\n"
                "- blockchain.com\n"
                "- Clark Moody dashboard\n"
                "- Rainbow chart\n"
                "- Bitcoin whitepaper"
            )

        else:
            reply = "❓ Perintah tidak dikenali. Coba /start"

        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

# =========================
# PUSH MANUAL – /push ENDPOINT
# =========================
@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 Push Manual:\n"
        "📊 TIA breakout MA200\n"
        "🔓 MANTA unlock besok\n"
        "🧠 AI Narrative naik +19% mention"
    )
    requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Pushed!", 200

# =========================
# JALANKAN APLIKASI
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

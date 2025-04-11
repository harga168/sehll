from flask import Flask, request
import requests
import os
import threading

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")  # Wajib isi di Render env
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# ======================
# 🔁 AUTO PUSH SETIAP 6 JAM
# ======================
def push_insight():
    message = (
        "📊 AUTO PUSH – Insight Harian:\n"
        "🔥 TIA, OP, MANTA trending\n"
        "🔓 ARB unlock besok\n"
        "📈 LDO whale inflow +$1.6M\n"
        "🧠 Narrative: Modular, ZK, Restaking"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    threading.Timer(21600, push_insight).start()  # setiap 6 jam

push_insight()  # Aktifkan auto push saat bot hidup

# ======================
# ✅ HOME PAGE
# ======================
@app.route('/')
def home():
    return "Bot Telegram kamu aktif 24/7!"

# ======================
# ✅ WEBHOOK HANDLER
# ======================
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()

        print("✅ Chat ID =>", chat_id)  # Cetak ke log agar bisa copy

        if text == "/start":
            reply = (
                "✅ Bot Siap!\n"
                "Perintah utama:\n"
                "/insightdaily\n"
                "/score ETH\n"
                "/wallet BTC\n"
                "/airdropwatch\n"
                "/unlockrisk\n"
                "/btcsource"
            )

        elif text == "/insightdaily":
            reply = (
                "📊 Insight Harian:\n"
                "🔥 TIA, MANTA, LDO\n"
                "📈 Whale inflow: $OP\n"
                "🧠 Modular + AI + RWA trending"
            )

        elif text.startswith("/score"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📈 Skor {token}:\nTA: 86 | FA: 85 | VC inflow: ✅"

        elif text.startswith("/wallet"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📡 Wallet {token}:\nNew wallet: +3.1%, Whale inflow: $2.1M"

        elif text == "/airdropwatch":
            reply = (
                "🎁 Airdrop Potensial:\n"
                "- zkSync\n"
                "- AltLayer\n"
                "- LayerZero\n"
                "- EigenLayer"
            )

        elif text == "/unlockrisk":
            reply = (
                "🔓 Unlock Minggu Ini:\n"
                "- ARB 5.1%\n"
                "- OP 3.2%\n"
                "- MANTA (VC vesting)"
            )

        elif text == "/btcsource":
            reply = (
                "📘 BTC Toolkit:\n"
                "- Explorer: blockchain.com\n"
                "- Mempool: mempool.space\n"
                "- Dashboard: bitbo.io\n"
                "- Rainbow: blockchaincenter.net\n"
                "- Halving: bitcoinblockhalf.com"
            )

        else:
            reply = "❓ Command tidak dikenali. Coba /start untuk melihat menu."

        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

# ======================
# ✅ PUSH MANUAL (via /push atau UptimeRobot)
# ======================
@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 PUSH MANUAL:\n"
        "📊 LDO breakout RSI 69\n"
        "🔓 MANTA unlock dalam 2 hari\n"
        "🧠 AI narrative +12.3% mention rate"
    )
    requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Push sent!", 200

# ======================
# ✅ START FLASK APP
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

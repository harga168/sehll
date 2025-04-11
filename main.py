from flask import Flask, request
import requests
import os
import threading

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")  # Set di environment Render
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# 🔁 AUTO PUSH INSIGHT TIAP 6 JAM
def push_insight():
    message = (
        "📊 [AUTO PUSH – Insight Harian]\n"
        "🔥 Trending: TIA, OP, MANTA\n"
        "🔓 Unlock Alert: ARB (5.1%)\n"
        "🧠 Narrative: Modular, Restaking, AI\n"
        "✅ Rekomendasi: Pantau support swing zone"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    threading.Timer(21600, push_insight).start()  # setiap 6 jam

push_insight()

# ✅ HALAMAN UTAMA
@app.route('/')
def home():
    return "Bot Telegram kamu aktif 24/7 dan autopush ON!"

# ✅ HANDLER WEBHOOK
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()

        print("✅ Chat ID =>", chat_id)  # Tampilkan di log

        # Mulai parsing perintah
        if text in ["/start", "/start@risetdatacrypto_bot"]:
            reply = (
                "✅ Bot Siap Digunakan!\n\n"
                "/insightdaily – Insight otomatis harian\n"
                "/score ETH – Skor token\n"
                "/wallet BTC – Whale tracker\n"
                "/airdropwatch – Airdrop potensial\n"
                "/unlockrisk – Unlock mingguan\n"
                "/btcsource – Toolkit Bitcoin"
            )

        elif text in ["/insightdaily", "/insightdaily@risetdatacrypto_bot"]:
            reply = (
                "📊 Insight Hari Ini:\n"
                "🔥 TIA, OP, LDO trending\n"
                "📈 Whale inflow: $LDO +$1.6M\n"
                "🧠 Modular & Restaking aktif"
            )

        elif text.startswith("/score") or text.startswith("/score@risetdatacrypto_bot"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📈 Skor Analisis {token}:\nTA: 87 | FA: 84 | Narrative: ZK/Modular"

        elif text.startswith("/wallet") or text.startswith("/wallet@risetdatacrypto_bot"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📡 Wallet {token}:\nWhale +$1.2M | New Wallets: +4.5%"

        elif text in ["/airdropwatch", "/airdropwatch@risetdatacrypto_bot"]:
            reply = (
                "🎁 Airdrop Radar:\n"
                "- zkSync\n"
                "- AltLayer\n"
                "- LayerZero\n"
                "- EigenLayer"
            )

        elif text in ["/unlockrisk", "/unlockrisk@risetdatacrypto_bot"]:
            reply = (
                "🔓 Unlock Minggu Ini:\n"
                "- ARB 5.1% (besok)\n"
                "- OP 3.2% (hari ini)\n"
                "- MANTA vesting aktif"
            )

        elif text in ["/btcsource", "/btcsource@risetdatacrypto_bot"]:
            reply = (
                "📘 Bitcoin Tools:\n"
                "- Explorer: blockchain.com\n"
                "- Mempool: mempool.space\n"
                "- Stats: bitbo.io, Rainbow Chart\n"
                "- Halving: bitcoinblockhalf.com\n"
                "- Whitepaper: bitcoin.org"
            )

        else:
            reply = "❓ Perintah tidak dikenali. Coba /start"

        # Kirim ke Telegram
        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

# ✅ PUSH MANUAL (PING /push)
@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 Manual Push:\n"
        "📊 $TIA breakout MA50\n"
        "🔓 Unlock MANTA besok\n"
        "🧠 Narrative ZK naik +14% volume"
    )
    requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Push berhasil!", 200

# ✅ START APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

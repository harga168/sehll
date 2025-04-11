from flask import Flask, request
import requests
import os
import threading
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")  # Chat ID grup
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# =====================
# 🔁 AUTO PUSH SETIAP 6 JAM
# =====================
def push_insight():
    now = datetime.now().strftime("%d-%m-%Y %H:%M")
    message = (
        f"📊 [AUTO INSIGHT] ({now})\n"
        "🔥 Top Token: $TIA, $OP, $MANTA\n"
        "🔓 Unlock Alert: $ARB besok (5.1%)\n"
        "🧠 Narrative: Modular, Restaking, ZK\n"
        "✅ Rekomendasi: Pantau zona beli swing"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    threading.Timer(21600, push_insight).start()  # 6 jam = 21600 detik

push_insight()

# =====================
# ✅ HOMEPAGE
# =====================
@app.route('/')
def home():
    return "✅ Bot Crypto kamu aktif & Auto Insight hidup!"

# =====================
# ✅ TELEGRAM WEBHOOK
# =====================
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()

        print("✅ Chat ID =>", chat_id)

        if text in ["/start", "/start@risetdatacrypto_bot"]:
            reply = (
                "✅ Bot Crypto AKTIF!\n\n"
                "📌 Command tersedia:\n"
                "/insightdaily – Insight harian\n"
                "/score ETH – Skor token\n"
                "/wallet BTC – Whale tracker\n"
                "/airdropwatch – Potensi airdrop\n"
                "/unlockrisk – Token unlock\n"
                "/btcsource – Toolkit Bitcoin\n"
                "/news – Berita crypto\n"
                "/macro – Data makro ekonomi\n"
                "/vcnews – Narrative VC"
            )

        elif text in ["/insightdaily", "/insightdaily@risetdatacrypto_bot"]:
            reply = (
                "📊 Insight Hari Ini:\n"
                "🔥 TIA, OP, MANTA trending\n"
                "🔓 Unlock ARB besok 5.1%\n"
                "📈 Whale inflow: LDO +$1.2M\n"
                "🧠 Narrative: Modular, AI, ZK"
            )

        elif text.startswith("/score"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📈 Skor {token}:\nTA: 85 | FA: 84 | VC inflow: ✅"

        elif text.startswith("/wallet"):
            token = text.split(" ")[1].upper() if len(text.split()) > 1 else "?"
            reply = f"📡 Wallet {token}:\nWhale inflow +$1.5M | Holder naik +3.1%"

        elif text in ["/airdropwatch", "/airdropwatch@risetdatacrypto_bot"]:
            reply = (
                "🎁 Airdrop Radar:\n"
                "- zkSync\n"
                "- LayerZero\n"
                "- AltLayer\n"
                "- EigenLayer"
            )

        elif text in ["/unlockrisk", "/unlockrisk@risetdatacrypto_bot"]:
            reply = (
                "🔓 Unlock Mingguan:\n"
                "- ARB 5.1% besok\n"
                "- MANTA 3.2% hari ini\n"
                "- Saran: pantau inflow wallet"
            )

        elif text in ["/btcsource", "/btcsource@risetdatacrypto_bot"]:
            reply = (
                "📘 BTC Tools:\n"
                "- Explorer: blockchain.com\n"
                "- Mempool: mempool.space\n"
                "- Rainbow Chart: blockchaincenter.net\n"
                "- S2F: 100trillionusd.github.io\n"
                "- Halving: bitcoinblockhalf.com"
            )

        elif text in ["/news", "/news@risetdatacrypto_bot"]:
            reply = (
                "📰 Crypto News:\n"
                "- CoinDesk: ETF inflow $500M\n"
                "- TheBlock: Arbitrum DAO aktifkan staking\n"
                "- Messari: Modular narrative dominasi"
            )

        elif text in ["/macro", "/macro@risetdatacrypto_bot"]:
            reply = (
                "🌍 Makro Global:\n"
                "- CPI AS: 3.1%\n"
                "- FOMC rate: 5.25%\n"
                "- USD Index melemah – risk-on sentiment"
            )

        elif text in ["/vcnews", "/vcnews@risetdatacrypto_bot"]:
            reply = (
                "🧠 VC Thesis:\n"
                "- a16z: Restaking, AppChain infra\n"
                "- Delphi: ZK infra & RWA\n"
                "- Pantera: LayerZero, AltLayer, Pendle"
            )

        else:
            reply = "❓ Command tidak dikenali. Coba /start untuk daftar lengkap."

        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

# =====================
# ✅ MANUAL PUSH ENDPOINT
# =====================
@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 PUSH MANUAL:\n"
        "📊 $TIA breakout MA200\n"
        "🔓 MANTA unlock besok\n"
        "🧠 AI & RWA narrative trending"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Push terkirim ke Telegram!", 200

# =====================
# ✅ RUN FLASK APP
# =====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

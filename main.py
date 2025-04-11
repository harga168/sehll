from flask import Flask, request
import requests
import os
import threading
from datetime import datetime
import feedparser

app = Flask(__name__)

# === Konfigurasi
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# === Fetch Harga dari CoinGecko
def get_token_price(symbol="ethereum"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_market_cap=true"
        r = requests.get(url)
        d = r.json()
        usd = d[symbol]["usd"]
        mc = d[symbol]["usd_market_cap"]
        return f"💰 Harga {symbol.upper()}: ${usd:,} | MarketCap: ${int(mc):,}"
    except:
        return "⚠️ Gagal ambil harga dari CoinGecko"

# === Fetch Unlock dari TokenUnlocks (public API)
def get_unlocks():
    try:
        r = requests.get("https://api-v2.tokenunlocks.app/api/v1/token/nextUnlocks")
        d = r.json()
        message = "🔓 Token Unlock Terdekat:\n"
        for i in range(3):
            token = d["data"][i]
            message += f"• {token['tokenName']} – {token['unlockAmount']} {token['symbol']}\n  Tanggal: {token['date'][:10]}\n"
        return message
    except:
        return "⚠️ Gagal ambil data unlock."

# === Fetch Crypto News dari CoinDesk
def get_crypto_news():
    try:
        feed = feedparser.parse("https://www.coindesk.com/arc/outboundfeeds/rss/")
        msg = "📰 Berita Crypto:\n"
        for entry in feed.entries[:3]:
            msg += f"• {entry.title}\n{entry.link}\n"
        return msg
    except:
        return "⚠️ Gagal ambil berita crypto."

# === Fetch Macro News dari IMF
def get_macro_news():
    try:
        feed = feedparser.parse("https://www.imf.org/en/News/rss")
        msg = "🌍 Berita Makro IMF:\n"
        for entry in feed.entries[:3]:
            msg += f"• {entry.title}\n{entry.link}\n"
        return msg
    except:
        return "⚠️ Gagal ambil data makro."

# === Auto-Push setiap 6 jam
def push_insight():
    now = datetime.now().strftime("%d-%m-%Y %H:%M")
    message = (
        f"📊 [AUTO INSIGHT] ({now})\n"
        "🔥 TIA, ARB, MANTA trending\n"
        "🔓 Unlock Aktif: ARB, LDO\n"
        "🧠 Narrative: Modular, Restaking, ZK\n"
        "📈 Whale inflow: +$2M ($LDO)"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    threading.Timer(21600, push_insight).start()

push_insight()

# === Home
@app.route('/')
def home():
    return "✅ BOT CRYPTO OTOMATIS AKTIF!"

# === Webhook Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"].strip().lower()
        print("✅ Chat ID =>", chat_id)

        if text in ["/start", "/start@risetdatacrypto_bot"]:
            reply = (
                "✅ Bot Crypto 24/7 Aktif!\n\n"
                "/insightdaily\n/score ETH\n/wallet BTC\n"
                "/unlocktoday\n/news\n/macro\n/price ETH\n/btcsource\n/push"
            )
        elif text in ["/insightdaily", "/insightdaily@risetdatacrypto_bot"]:
            reply = "📊 Insight Hari Ini:\n🔥 TIA, ARB, LDO trending\n🔓 Unlock ARB besok\n🧠 Modular narrative naik"
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
                "📘 BTC Toolkit:\n"
                "- mempool.space\n- blockchair.com\n"
                "- rainbow chart\n- bitcoinblockhalf.com\n- bitbo.io"
            )
        elif text == "/push":
            reply = "🚀 Manual Push:\n📊 Unlock ARB +5.1% besok\n🧠 Modular & RWA trending"

        else:
            reply = "❓ Perintah tidak dikenali. Ketik /start untuk daftar lengkap."

        requests.post(URL, json={"chat_id": chat_id, "text": reply})
    return "ok", 200

# === Endpoint manual /push
@app.route('/push', methods=['GET'])
def autopush():
    message = (
        "🚀 PUSH:\n📊 $TIA breakout MA200\n🔓 MANTA unlock aktif\n🧠 RWA + Modular trending"
    )
    if CHAT_ID:
        requests.post(URL, json={"chat_id": CHAT_ID, "text": message})
    return "Push success", 200

# === Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

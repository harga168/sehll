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
        text = data["message"]["text"].strip()

        # ✅ /start
        if text == "/start":
            reply = (
                "✅ Bot Riset Crypto AKTIF!\n\n"
                "📍 Command tersedia:\n"
                "/insightdaily – insight harian\n"
                "/score ETH – analisa token\n"
                "/wallet BTC – pantau whale\n"
                "/airdropwatch – radar airdrop\n"
                "/unlockrisk – pantau unlock\n"
                "/btcsource – toolkit Bitcoin\n"
            )

        # ✅ /insightdaily
        elif text == "/insightdaily":
            reply = (
                "📊 Insight Hari Ini:\n"
                "🔥 Narrative: Modular, AI, L2\n"
                "🏆 Top Token: TIA, OP, MANTA\n"
                "📈 Whale inflow: $1.6M – LDO"
            )

        # ✅ /score [TOKEN]
        elif text.startswith("/score"):
            token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
            reply = (
                f"📈 Skor Analisis untuk {token}:\n"
                "- TA: 86 | FA: 82 | Narrative: Restaking\n"
                "- VC Score: 92\n"
                "- Rekomendasi: DCA atau swing + alert unlock"
            )

        # ✅ /wallet [TOKEN]
        elif text.startswith("/wallet"):
            token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
            reply = (
                f"📡 Whale Insight {token}:\n"
                "- New Wallets +4.3%\n"
                "- Whale Transfer: +$1.2M\n"
                "- Distribusi: sehat, tidak terpusat"
            )

        # ✅ /airdropwatch
        elif text == "/airdropwatch":
            reply = (
                "🎁 Airdrop Aktif:\n"
                "- zkSync → snapshot minggu ini\n"
                "- AltLayer → bridge user aktif\n"
                "- LayerZero → on-chain tester eligible"
            )

        # ✅ /unlockrisk
        elif text == "/unlockrisk":
            reply = (
                "🔓 Token Unlock Mingguan:\n"
                "- $ARB: 4.2% besok\n"
                "- $XYZ: VC wallet ke Binance\n"
                "- Hindari beli menjelang unlock"
            )

        # ✅ /btcsource
        elif text == "/btcsource":
            reply = (
                "📘 Resource Bitcoin Lengkap:\n"
                "- Explorer: blockchain.com, blockchair\n"
                "- Mempool: mempool.space\n"
                "- Statistik: bitbo.io, Clark Moody\n"
                "- Rainbow: blockchaincenter.net\n"
                "- Whitepaper: bitcoin.org\n"
                "- Halving: bitcoinblockhalf.com"
            )

        else:
            reply = "❓ Command tidak dikenali. Coba ketik /start untuk lihat semua fitur."

        # Kirim balasan ke Telegram
        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

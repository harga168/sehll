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
        text = data["message"]["text"].strip().lower()

        # Command logic
        if text == "/start":
            reply = (
                "✅ Bot Riset Crypto AKTIF!\n\n"
                "Ketik /insightdaily untuk insight harian\n"
                "Contoh:\n"
                "/score ETH\n"
                "/wallet BTC\n"
                "/airdropwatch\n"
                "/unlockrisk\n"
                "/btcsource"
            )

        elif text == "/insightdaily":
            reply = (
                "📊 Insight Crypto Hari Ini:\n"
                "🔥 Narrative: Modular, AI, Restaking\n"
                "Top Token: $TIA, $ARB, $MANTA\n"
                "Skor Tertinggi: $TIA (93), $OP (88)\n"
                "Whale activity: $LDO +$1.4M inflow"
            )

        elif text.startswith("/score"):
    token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
    reply = (
        f"📈 Skor Analisis untuk {token}:\n"
        "- TA: 87 | FA: 82 | VC Score: 90\n"
        "- Narrative: ZK Rollup, AppChain\n"
        "- Rekomendasi: ✅ Swing Zone + DCA"
    

            )

        elif text.startswith("/wallet"):
    token = text.split(" ")[1].upper() if len(text.split(" ")) > 1 else "?"
    reply = (
        f"📡 Whale Insight untuk {token}:\n"
        "- New wallets: +4.5%\n"
        "- Whale activity: +$1.2M inflow\n"
        "- Holder distribusi: Sehat ✅"
    )


        elif text == "/airdropwatch":
            reply = (
                "🎁 Airdrop Radar:\n"
                "- zkSync: snapshot minggu ini\n"
                "- AltLayer: bridge early user\n"
                "- EigenLayer: restaking eligibility"
            )

        elif text == "/unlockrisk":
            reply = (
                "🔓 Token Unlock Minggu Ini:\n"
                "- $ARB: 4.2% total supply\n"
                "- $MANTA: VC unlock besok\n"
                "- Saran: pantau inflow ke CEX"
            )

        elif text == "/btcsource":
            reply = (
                "📘 Bitcoin Resource Kit:\n"
                "- Explorer: blockchain.com, btc.com\n"
                "- Mempool: mempool.space\n"
                "- Statistik: bitbo.io, Clark Moody\n"
                "- Rainbow Chart: blockchaincenter.net\n"
                "- Whitepaper: bitcoin.org\n"
                "- Halving: bitcoinblockhalf.com"
            )

        elif text == "/riskwatch":
            reply = (
                "⚠️ Token Berisiko Tinggi:\n"
                "- $XYZ: Dev mint token 3x\n"
                "- $RUG: LP 100% hilang\n"
                "- $MEME: Harga turun -97%, scam"
            )

        elif text == "/growthscore":
            reply = (
                "🚀 Growth Score:\n"
                "- $TIA: TVL +24%, dev aktif\n"
                "- $MANTA: users naik 19%\n"
                "- $LAVA: narrative infra on fire"
            )

        elif text == "/smartflow":
            reply = (
                "🧠 Smart Money Flow:\n"
                "- $ARB: VC +$2.1M (a16z, Jump)\n"
                "- $LDO: Whale stacking\n"
                "- $ETH: Institutions steady hold"
            )

        else:
            reply = (
                "❓ Perintah tidak dikenali.\n"
                "Coba: /start atau /insightdaily"
            )

        # Kirim ke Telegram
        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

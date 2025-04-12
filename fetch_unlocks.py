import requests
def get_unlocks():
    try:
        r = requests.get("https://api-v2.tokenunlocks.app/api/v1/token/nextUnlocks")
        d = r.json()
        msg = "🔓 Token Unlock Terdekat:\n"
        for i in range(3):
            t = d["data"][i]
            msg += f"• {t['tokenName']} – {t['unlockAmount']} {t['symbol']}\n  {t['date'][:10]}\n"
        return msg, "✅"
    except:
        return "⚠️ Gagal ambil data unlock.", "❌"
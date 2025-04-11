import requests

def get_unlocks():
    try:
        url = "https://api-v2.tokenunlocks.app/api/v1/token/nextUnlocks"
        response = requests.get(url)
        data = response.json()

        message = "🔓 [Unlock Token Terdekat]\n"
        for i in range(3):  # ambil 3 teratas
            token = data["data"][i]
            message += f"\n• {token['tokenName']} – Unlock: {token['unlockAmount']} {token['symbol']}\nTanggal: {token['date'][:10]}"
        return message

    except Exception as e:
        return f"⚠️ Gagal ambil data unlock: {e}"

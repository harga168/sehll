import requests

def get_token_price(symbol="ethereum"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_market_cap=true"
        response = requests.get(url)
        data = response.json()
        usd = data[symbol]["usd"]
        mc = data[symbol]["usd_market_cap"]
        return f"💰 Harga {symbol.upper()}: ${usd:,}\nMarketCap: ${int(mc):,}"

    except Exception as e:
        return f"⚠️ Gagal ambil harga dari CoinGecko: {e}"

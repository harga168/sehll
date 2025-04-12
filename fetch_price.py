import requests
def get_token_price(symbol="ethereum"):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_market_cap=true"
        r = requests.get(url)
        d = r.json()
        usd = d[symbol]["usd"]
        mc = d[symbol]["usd_market_cap"]
        return f"💰 {symbol.upper()}: ${usd:,} | MarketCap: ${int(mc):,}", "✅"
    except:
        return "⚠️ Gagal ambil harga token.", "❌"
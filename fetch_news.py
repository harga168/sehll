import feedparser

def get_crypto_news():
    try:
        feed = feedparser.parse("https://www.coindesk.com/arc/outboundfeeds/rss/")
        message = "📰 [Crypto News Terbaru]\n"
        for entry in feed.entries[:3]:
            message += f"\n• {entry.title}\n{entry.link}"
        return message
    except Exception as e:
        return f"⚠️ Gagal ambil berita: {e}"

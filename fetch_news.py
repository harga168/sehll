import feedparser
def get_crypto_news():
    try:
        feed = feedparser.parse("https://www.coindesk.com/arc/outboundfeeds/rss/")
        msg = "📰 Berita Crypto:\n"
        for entry in feed.entries[:3]:
            msg += f"• {entry.title}\n{entry.link}\n"
        return msg, "✅"
    except:
        return "⚠️ Gagal ambil berita crypto.", "❌"
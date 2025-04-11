import feedparser

def get_macro_news():
    try:
        feed = feedparser.parse("https://www.imf.org/en/News/rss")
        message = "🌍 [Berita Makro IMF]\n"
        for entry in feed.entries[:3]:
            message += f"\n• {entry.title}\n{entry.link}"
        return message
    except Exception as e:
        return f"⚠️ Gagal ambil data makro: {e}"

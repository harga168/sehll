import feedparser
def get_macro_news():
    try:
        feed = feedparser.parse("https://www.imf.org/en/News/rss")
        msg = "🌍 Makro Ekonomi:\n"
        for entry in feed.entries[:3]:
            msg += f"• {entry.title}\n{entry.link}\n"
        return msg, "✅"
    except:
        return "⚠️ Gagal ambil data makro.", "❌"
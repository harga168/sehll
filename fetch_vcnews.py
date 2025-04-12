import feedparser
def get_vc_news():
    try:
        feed = feedparser.parse("https://www.delphidigital.io/feed.xml")
        msg = "🧠 VC Narrative – Delphi:\n"
        for entry in feed.entries[:3]:
            msg += f"• {entry.title}\n{entry.link}\n"
        return msg, "✅"
    except:
        return "⚠️ Gagal ambil VC news.", "❌"
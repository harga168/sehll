def get_whale_alert():
    try:
        return "🐋 Smart Money Alert:\n• ARB: +$2.1M\n• OP: +$1.8M\n• LDO: +$1.5M", "✅"
    except:
        return "⚠️ Gagal ambil whale data.", "❌"
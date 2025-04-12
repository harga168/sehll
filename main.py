from flask import Flask, request
import requests
import os
import threading
from datetime import datetime
from plot_price_chart import create_price_chart
from plot_multi_price_chart import create_multi_price_chart
from plot_tvl_chart import create_tvl_chart
from plot_inflow_chart import create_inflow_chart

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL_TEXT = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
URL_PHOTO = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

def push_all_graphics():
    now = datetime.now().strftime("%d-%m-%Y %H:%M")
    text_msg = (
        f"📊 [AUTO INSIGHT + GRAFIK] ({now})\n"
        "🔥 Multi-token tracker, TVL, inflow terbaru\n"
        "🧠 Powered by Telegram Bot Institusi"
    )

    if CHAT_ID:
        requests.post(URL_TEXT, json={"chat_id": CHAT_ID, "text": text_msg})

        chart1 = create_price_chart("TIA")
        files1 = {'photo': ('chart1.png', chart1)}
        data1 = {'chat_id': CHAT_ID, 'caption': '📈 Harga $TIA Mingguan'}
        requests.post(URL_PHOTO, files=files1, data=data1)

        chart2 = create_multi_price_chart()
        files2 = {'photo': ('chart2.png', chart2)}
        data2 = {'chat_id': CHAT_ID, 'caption': '📊 Harga Multi-Token'}
        requests.post(URL_PHOTO, files=files2, data=data2)

        chart3 = create_tvl_chart()
        files3 = {'photo': ('chart3.png', chart3)}
        data3 = {'chat_id': CHAT_ID, 'caption': '💰 TVL Protokol DeFi'}
        requests.post(URL_PHOTO, files=files3, data=data3)

        chart4 = create_inflow_chart()
        files4 = {'photo': ('chart4.png', chart4)}
        data4 = {'chat_id': CHAT_ID, 'caption': '🐋 Whale Inflow 24 Jam'}
        requests.post(URL_PHOTO, files=files4, data=data4)

    threading.Timer(21600, push_all_graphics).start()

push_all_graphics()

@app.route('/')
def home():
    return "✅ BOT GRAFIK INSTITUSI AKTIF"

@app.route('/push', methods=['GET'])
def manual_push():
    push_all_graphics()
    return "✅ Grafik & Insight dikirim!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

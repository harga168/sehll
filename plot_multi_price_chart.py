import matplotlib.pyplot as plt
import io

def create_multi_price_chart():
    tokens = {
        'ETH': [1800, 1850, 1900, 2000, 1950],
        'BTC': [25000, 25500, 26000, 27000, 26500],
        'ARB': [1.0, 1.05, 1.08, 1.1, 1.03]
    }
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    plt.figure(figsize=(7, 4))
    for token, prices in tokens.items():
        plt.plot(days, prices, marker='o', label=token)
    plt.title("📈 Harga Token Minggu Ini")
    plt.xlabel("Hari")
    plt.ylabel("Harga USD")
    plt.legend()
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
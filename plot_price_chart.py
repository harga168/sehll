import matplotlib.pyplot as plt
import io

def create_price_chart(token='TIA'):
    prices = [1.1, 1.3, 1.45, 1.6, 1.5, 1.8]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    plt.figure(figsize=(6, 3))
    plt.plot(days, prices, marker='o')
    plt.title(f'Harga {token.upper()} Minggu Ini')
    plt.xlabel('Hari')
    plt.ylabel('Harga USD')
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
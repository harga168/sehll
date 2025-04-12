import matplotlib.pyplot as plt
import io

def create_tvl_chart():
    protocols = ['Lido', 'Aave', 'Curve', 'Uniswap']
    tvl = [14.5, 8.2, 5.7, 4.9]

    plt.figure(figsize=(6, 3.5))
    plt.bar(protocols, tvl, color='skyblue')
    plt.title("💰 TVL DeFi Protokol (USD Miliar)")
    plt.ylabel("TVL (B)")
    plt.grid(axis='y')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
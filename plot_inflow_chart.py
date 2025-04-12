import matplotlib.pyplot as plt
import io

def create_inflow_chart():
    tokens = ['ETH', 'ARB', 'LDO']
    inflows = [2.1, 1.8, 1.4]

    plt.figure(figsize=(6, 3.5))
    plt.bar(tokens, inflows, color='orange')
    plt.title("🐋 Whale Inflow 24 Jam (USD Juta)")
    plt.ylabel("Inflow (M)")
    plt.grid(axis='y')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf
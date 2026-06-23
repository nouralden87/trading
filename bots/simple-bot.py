"""
بوت تداول بسيط — Python × MEXC API
تعليمي فقط — ليس للإنتاج
"""

import time
import requests

SYMBOL = "PERMUSDT"
INTERVAL = "5m"
LIMIT = 50

def get_price():
    r = requests.get(f"https://api.mexc.com/api/v3/ticker/price?symbol={SYMBOL}")
    return float(r.json()["price"])

def get_klines():
    r = requests.get(f"https://api.mexc.com/api/v3/klines?symbol={SYMBOL}&interval={INTERVAL}&limit={LIMIT}")
    return r.json()

def calculate_rsi(prices, period=14):
    gains = [max(prices[i] - prices[i-1], 0) for i in range(1, len(prices))]
    losses = [max(prices[i-1] - prices[i], 0) for i in range(1, len(prices))]
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def main():
    print(f"Bot started for {SYMBOL}")
    while True:
        try:
            klines = get_klines()
            closes = [float(k[4]) for k in klines]
            rsi = calculate_rsi(closes)
            price = closes[-1]

            print(f"Price: {price:.4f} | RSI: {rsi:.1f}")

            if rsi < 30:
                print("BUY SIGNAL!")
            elif rsi > 70:
                print("SELL SIGNAL!")

            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()

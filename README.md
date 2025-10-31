# Lekzy Trading Pro 💹

💡 A Telegram trading bot that sends real-time buy/sell signals using **TwelveData API**, built with Python and deployed on **Render**.

---

## ✨ Features
- Live market data using [TwelveData API](https://twelvedata.com/)
- Monitors:
  - Currency pairs (e.g. EUR/USD, GBP/USD, USD/JPY)
  - Cryptocurrencies (e.g. BTC/USD, ETH/USD, BNB/USD)
  - Commodities (Gold, Silver, Crude Oil)
  - Stocks (AAPL, TSLA, MSFT, etc.)
- EMA + RSI + ROC + Volume filters for confirmation
- Telegram notifications for entry/exit signals
- Runs continuously on Render cloud

---

## ⚙️ Environment Variables

Create these in **Render → Environment tab**:

| Variable Name | Description |
|----------------|-------------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from [@BotFather](https://t.me/BotFather) |
| `TWELVE_DATA_API_KEY` | Your first TwelveData API key |
| `TWELVE_DATA_API_KEY_2` | Your second TwelveData API key |

---

## 🖥️ Installation (Local)

```bash
git clone https://github.com/lekzytradepro/Lekzy_trading_pro
cd Lekzy_trading_pro
pip install -r requirements.txt
python lekzy_trade_pro.py

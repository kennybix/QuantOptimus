

# 3-EMA Strategy

This is a simple trading bot based on the Exponential Moving Average (EMA) strategy. The bot trades on the 1-hour chart using a crossover of the *fast*, *normal*, and *slow* period EMAs to make a buy/sell decision. The bot then uses a 15-minute chart to monitor the trade and exit when there is a crossunder of the *fast* and *normal* period EMAs. The bot is built using Pine Script and the TradingView platform.

## Installation

To use this bot, you will need a TradingView account and a compatible broker. Simply copy and paste the Pine Script code into the TradingView Pine Editor and set up your broker connection. You can then run the bot on the 1-hour and 15-minute charts.

## Usage

Once the bot is set up, it will automatically make trades based on the EMA crossover and crossunder signals. You can adjust the parameters of the EMAs and the entry/exit signals to optimize the bot's performance. It is recommended that you backtest the bot on historical data before using it on live markets.

## Disclaimer

This bot is for educational purposes only and should not be used for live trading without thorough testing and risk management. The author of this bot is not responsible for any losses incurred from the use of this bot. Use at your own risk.

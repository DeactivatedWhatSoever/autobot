import time
import datetime
from app.strategy import volatility_breakout as vb
from app.exchange import upbit
from dotenv import load_dotenv


# Init dotenv
load_dotenv(verbose=True)
# Init global variables
symbol = 'KRW-BTC'
now = datetime.datetime.now()
midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
target_price = vb.target_price(symbol)


if __name__ == '__main__':
    while True:
        try:
            now = datetime.datetime.now()
            # Sell at midnight (End position)
            if midnight < now < midnight + datetime.timedelta(seconds=10):
                target_price = vb.target_price(symbol)
                midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
                upbit.sell(symbol)
            # Buy when current price is at target price (Start position)
            current_price = upbit.current_price(symbol)
            if current_price > target_price:
                upbit.buy(symbol)
        except Exception as e:
            print('Error:', e)
            print('Error:', e.with_traceback("Traceback"))
        time.sleep(1)


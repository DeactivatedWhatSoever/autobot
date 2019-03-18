import time
import datetime
from app.exchange import upbit


def target_price(symbol, timeframe='day'):
    """The price calculated by strategy."""
    ohlcv_df = upbit.ohlcv(symbol, timeframe)
    yesterday = ohlcv_df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target


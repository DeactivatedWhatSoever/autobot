import pyupbit
import datetime
import os


upbit_api = pyupbit.Upbit(os.getenv('API_KEY'), os.getenv('SECRET_KEY'))


def buy(symbol):
    krw = upbit_api.get_balances()[0][0]['balance']
    orderbook = pyupbit.get_orderbook(symbol)
    sell_price = orderbook[0]['orderbook_units'][0]['ask_price']
    unit = float(krw) / float(sell_price)
    #upbit_api.buy_limit_order(symbol, sell_price, unit)
    print('Balance:', krw, 'Buy Price:', sell_price, 'Shares:', unit)


def sell(symbol):
    krw = upbit_api.get_balances()[0][0]['balance']
    orderbook = pyupbit.get_orderbook(symbol)
    buy_price = orderbook[0]['orderbook_units'][0]['bid_price']
    unit = float(krw) / float(sell_price)
    #upbit_api.sell_limit_order(symbol, buy_price, unit)
    print('Balance:', krw, 'Sell Price:', buy_price, 'Shares:', unit)


def ohlcv(symbol='KRW-BTC', timeframe='day'):
    return pyupbit.get_ohlcv(ticker=symbol, interval=timeframe)


def current_price(symbol):
    return pyupbit.get_current_price(symbol)


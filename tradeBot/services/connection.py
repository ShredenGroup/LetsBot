import math
import time
import traceback
from typing import Dict,Optional
from binance.streams import ThreadedWebsocketManager
from binance.client import Client;
from ..config import Setting
class binanceConnection:
  def __init__(self):
 
    setting=Setting()
    binance_client=Client(
        setting.API_KEY,
        setting.API_SECRET
      )
    self.depth=binance_client.get_order_book(symbol='BNBBTC')
    print(setting.API_KEY)
    print(setting.API_SECRET)
    





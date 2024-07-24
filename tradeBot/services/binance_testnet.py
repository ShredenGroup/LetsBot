import math
import time
import traceback
from binance.client import Client;

from ..config import Setting
class binanceConnection:
  def __init__(self):
 
    setting=Setting()
    binance_client=Client(
        setting.API_KEY,
        setting.API_SECRET,
        testnet=True,
      )
  
    self.order=binance_client.create_order(
    symbol='BNBUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=0.01)
    self.system=binance_client.get_asset_details()
   
    
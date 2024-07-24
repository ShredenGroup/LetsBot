import sys
import threading
import time
from typing import Dict,Tuple,Set
from contextlib import contextmanager
class binanceOrder:
   def __init__(self,report):
      self.event=report
      self.symbol=report["symbol"]
      self.side=report["side"]
      self.order_type=report["order_type"]
      self.id=report["oder_id"]
   def __repr__(self):
      return f"<binance order {self.event}>"

class binanceCache:
   ticker_values: Dict[str,float]={}
   _balances:Dict[str,float]={}
   _balances_mutex:threading.Lock=threading.Lock()
   non_existent_ticker:Set[str]=set()
   orders:Dict[str,binanceOrder]={}
   
   
   
   
   

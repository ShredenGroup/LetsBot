import sys
from threading import Lock
import threading
import time
from typing import Dict,Tuple,Set
from contextlib import contextmanager
class BinanceOrder:
   def __init__(self,report):
      self.event=report
      self.symbol=report["symbol"]
      self.side=report["side"]
      self.order_type=report["order_type"]
      self.id=report["order_id"]
   def __repr__(self):
      return f"<binance order {self.event}>"

class BinanceCache:
   ticker_values: Dict[str,float]={}
   _balances:Dict[str,float]={}
   _balances_mutex:threading.Lock=Lock()
   non_existent_ticker:Set[str]=set()
   orders:Dict[str,BinanceOrder]={}

   @contextmanager
   def open_balances(self):
      with self._balances_mutex:
         yield self._balances

class OrderGuard:
   def __init__(self,pending_orders:Set[Tuple[str,int]],mutex:threading.Lock):
      self.pending_orders=pending_orders
      self.mutex=mutex
      self.mutex.acquire()
      self.tag=None

   def set_order(self,origin_symbol:str,target_symbol:str,order_id:int):
      self.tag=(origin_symbol+target_symbol,order_id)

   def __enter__(self):
      try:
         if self.tag is None:
            raise Exception("No tag detected")
         self.pending_orders.add(self.tag)
      finally:
         self.mutex.release()
      
   def __exit__(self):
      self.pending_orders.remove(self.tag)





   
   
   
   
   
   

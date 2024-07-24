from binance.um_futures import UMFutures



futureClient=UMFutures(key="7VC3PtSXjGRyIOKypWr3bQg11sgSAAfpqUzG8LsC0TjNRtk8X3i3jIpZrHmjqZUV",secret="qpTBYVLVowsazZlDdWxkyP0JPlUnX9uC5tULtmcXbICO6vdHXFVZ6xSb7TW0uSoh")

params = {
    'symbol': 'XRPUSDT',
    'side': 'BUY',
    'type': 'MARKET',
    'quantity': 15,
    'positionSide': 'LONG'
   
}
response = futureClient.new_order(**params)
print(response)
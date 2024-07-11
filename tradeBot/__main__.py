from .services import binanceConnection

BC=binanceConnection()
print(BC.depth)
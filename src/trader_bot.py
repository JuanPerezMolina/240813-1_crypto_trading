
from binance.client import Client
from binance.enums import *

API_KEY = "w4qgwUEnXLraraaV1cEfoxH6FR8bZJM8UCsILgQrOpveXDB5KpIhUb4eLkhGglQp"
API_SECRET = "Z3NxWQg7kQPgSiQzGRwtYB2XuMpv74m5rKQxQlS0e9SDCcKRD3gFQ8YxeUsOhZZD"
client = Client(API_KEY,API_SECRET, tld='com')
def obtener_tikckers():
    lista_tickers = client.get_all_tickers()
    for tiker in lista_tickers:
        symbol = tiker['symbol']
        price = tiker['price']
        print("Simbolo: " + symbol + ", Precio: " + price)
#obtener_tikckers()
def velas():   
    lista_precios_cierre = []
    data_historical = client.get_historical_klines("DARUSDT",Client.KLINE_INTERVAL_4HOUR,"804 hour ago UTC")

    #print("Cantidad de velas: " , len(data_historical))
    sumatoria = 0
    if len(data_historical) == 201:
      print("Se obtuvieron los datos correctamente")
      for i in range((201-200), 200):
         #print(data_historical[i])
         sumatoria += float(data_historical[i][4])
      sma = sumatoria/200
      print("SMA 200 DARUSDT: ", sma)
    else:
        print("No se pudo obtener el historial de velas") 
velas()

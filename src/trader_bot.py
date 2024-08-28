
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
def EMA_INTERVALO_5MIN(periodo, ticker):   
    lista_precios_cierre = []
    data_historical = client.get_historical_klines(ticker,Client.KLINE_INTERVAL_5MINUTE,"250 minutes ago UTC")

#    print("Cantidad de velas: " , len(data_historical))
    sumatoria = 0
    if len(data_historical) == 50:
      print("Se obtuvieron los datos correctamente")
      for i in range((50-periodo), 50):
         #print(data_historical[i])
         sumatoria += float(data_historical[i][4])
         precio_cierre_actual = float(data_historical[i][4])
      sma = sumatoria/periodo
      multiplicador = 2/(periodo + 1)
      EMA = sma
      EMA = (precio_cierre_actual - EMA) * multiplicador + EMA
      print("EMA: " + ticker + " periodo " + str(periodo) + " : " +str(EMA))
      return(EMA)
    else:
        print("No se pudo obtener el historial de velas") 
EMA_INTERVALO_5MIN(5,'BNXUSDT')
EMA_INTERVALO_5MIN(25,'BNXUSDT')

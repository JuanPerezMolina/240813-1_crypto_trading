
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
    data_historical = client.get_historical_klines(ticker,Client.KLINE_INTERVAL_5MINUTE,"275 minutes ago UTC")

    #print("Cantidad de velas: " , len(data_historical))
    sumatoria = 0
    if len(data_historical) == 55:
      #print("Se obtuvieron los datos correctamente")
      for i in range((55-periodo), 55):
         #print(data_historical[i])
         sumatoria += float(data_historical[i][4])
         precio_cierre_actual = float(data_historical[i][4])
      sma = sumatoria/periodo
      multiplicador = 2/(periodo + 1)
      EMA = sma
      EMA = (precio_cierre_actual - EMA) * multiplicador + EMA
      #print("EMA: " + ticker + " periodo " + str(periodo) + " : " +str(EMA))
      return(EMA)
    else:
        print("No se pudo obtener el historial de velas") 
ema5  = EMA_INTERVALO_5MIN(5,'BNXUSDT')
ema15 = EMA_INTERVALO_5MIN(15,'BNXUSDT')
ema25 = EMA_INTERVALO_5MIN(25,'BNXUSDT')
cruce_arriba  = (ema5 > ema15) and (ema15 < ema25) and (ema5 > ema25)
cruce_abajo = (ema5 < ema15) and (ema15 < ema25) and (ema5 < ema25)
prox_cruce_arriba  = (ema5 < ema15) and (ema15 < ema25) and (ema5 > ema25)
prox_cruce_abajo = (ema5 > ema15) and (ema15 < ema25) and (ema5 < ema25)
if cruce_arriba or cruce_abajo:
    print("Se esta cumpliendo la estrategia ema 5-15-25 de triple cruce hacia arriba ")
elif cruce_abajo:
    print("Se esta cumpliendo la estrategia ema 5-15-25 de triple cruce hacia abajo")
elif prox_cruce_arriba:
    print("Próximo a cumplirse la estrategia ema 5-15-25 de triple cruce hacia arriba")
elif prox_cruce_abajo:
    print("Próximo a cumplirse la estrategia ema 5-15-25 de triple cruce hacia abajo")
else:
    print("Todavia no esta por cumplirse la estrategia de triple cruce ema 5-15-25")
  

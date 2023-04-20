import requests
import urllib.request
import time
import csv
import datetime

url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"

prix = (requests.get(url).json())['EUR']
print(f"Prix BTC: {prix} euros.")

for i in range (60):

    time.sleep(10)  #En seconde

    prix = (requests.get(url).json())['EUR']

    now = datetime.datetime.now()
    time_now = (now.strftime("%d-%m %H:%M:%S"))

    with open ("data.csv", "a") as data_sheet:
        data_sheet.write(str(prix) + " / " + time_now + "\n")

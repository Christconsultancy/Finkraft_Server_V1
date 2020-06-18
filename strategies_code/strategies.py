import pandas as pd
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('Stock')
data = client.query('SELECT "open" FROM "ACC"')
data_list = list(data)
df_data = pd.DataFrame(data)
data = df_data.head(15)
print(data)





def ema(start_date, end_date, timeframe, parameter):
    print("working")
    ma = 0
    ema = 0
    count = 0
    totalClose = 0
    currentClose = 0
    N = parameter
    data = pd.read_csv("temp_data/ACC.csv")
    print("Check point")
    for i, date in enumerate(data["date"]):
        if (date == start_date):
            currentClose = data["close"][i]
            count = 1
            totalClose = 0
            while count <= N:
                totalClose = totalClose + data["close"][i - count]
                count = count + 1
            break

    multiplier = 2 / (count + 1)

    ma = totalClose / count
    ema = (currentClose * multiplier) + (ma * (1 - multiplier))

    if (currentClose > ema):
        singal = "Buy"
    else:
        singal = "Sell"

    print(singal)
    statergy_result = {
        'start_date': start_date,
        'end_date': end_date,
        'timeframe': timeframe,
        'singal': singal,
    }
    return statergy_result


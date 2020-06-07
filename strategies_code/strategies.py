import pandas as pd


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

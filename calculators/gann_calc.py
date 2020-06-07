#inputs
# Signal
# open price
# (reward:risk) ratio

#ouputs
# Entry price
# Target
# Stock Loss

#import statement
import time
import pandas as pd

signal = input("Enter the SIGNAL [BUY / SELL]: ")
openPrice = int(input("Enter the OPEN PRICE : "))
print("Enter the Reward Risk Ratio")
reward = int(input("Enter the reward : "))
risk = int(input("Enter the risk : "))

print("The values are : \nSignal : ",signal,"\nOpen Price : ",openPrice,"\nReward : Risk = ",reward," : ",risk)

#creating GANN Chart from Excel File
gann = pd.read_excel('gann.xlsx')
gann.drop(['ODD-1','ODD-2','ATR'],inplace=True,axis=1)
gann_lst = []
for i in gann.index:
	for j in gann.loc[i]:
		try:
			gann_lst.append(int(j))
		except:
			pass
gann_lst = list(set(gann_lst))
gann_lst.sort()

print("GANN Values : \n", gann_lst,"\n")

#calculator
for i in range(len(gann_lst)-1):
    if gann_lst[i] < openPrice and gann_lst[i + 1] >= openPrice:
        if signal == "BUY":
            print("ENTRY PRICE : ",gann_lst[i + 1])
            print("TARGET PRICE : ",gann_lst[i + 1 + reward])
            print("STOCK LOSS : ",gann_lst[i+1-risk])
        else:
            print("ENTRY PRICE : ",gann_lst[i])
            print("TARGET PRICE : ",gann_lst[i - reward])
            print("STOCK LOSS : ",gann_lst[i + risk])

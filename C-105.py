import pandas as pd
import math

import statistics

df = pd.read_csv("Data.csv")
data = list(df)

intData = []

for i in data:
    intData.append(int(i))

mean = sum(intData)/len(intData)

squareList = []

for x in intData:
    a = x - mean
    a = a ** 2
    squareList.append(a)

total = sum(squareList)

result = total/(len(intData)-1)

stDev = math.sqrt(result)
print(stDev)
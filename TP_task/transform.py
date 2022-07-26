import pandas as pd
import json

#df = pd.read_json('/content/properties_1.json', orient='split')
#df.head()

with open("TP_task/properties_1.txt", "r", encoding='utf-8-sig') as f:
    data = f.readlines()
print(data[0])
pd.read_json(data[0], orient='split')
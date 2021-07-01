import urllib.request
import json
import pandas as pd
from pandas.io.json import json_normalize

api_key="4c5269704f6479643130366f67786449"

day_start="20210501"
day_end="20210531"
dt_index=pd.date_range(start=day_start,end=day_end)
dt_list=dt_index.strftime("%Y%m%d").tolist()

df=pd.DataFrame()

for i in dt_list:
    url="http://openapi.seoul.go.kr:8088/"+api_key+"/json/CardSubwayStatsNew/1/1000/" + i
    response = urllib.request.urlopen(url) 
    json_str = response.read().decode("utf-8")
    json_object = json.loads(json_str)
    df_temp=pd.json_normalize(json_object['CardSubwayStatsNew']['row'])
    df=df.append(df_temp)
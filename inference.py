
import json
import requests
import pandas as pd


data = pd.read_csv('sample_inference_data.csv')
data = data.drop(columns=['Timestamp', 'Location', 'Future_weather_condition'])
#data = data.drop(columns=['Future_weather_condition'])
url = 'http://0e9c3e51-105d-46ac-8c09-5e8b264b8e29.francecentral.azurecontainer.io/score'
headers = {'Content-Type':'application/json'}


for i in range(len(data)):
            inference_data = data.values[i].tolist()
            inference_data = json.dumps({"data": [inference_data]})
            r = requests.post(url, data=inference_data, headers=headers)
            print(str(i)+str(r.content))


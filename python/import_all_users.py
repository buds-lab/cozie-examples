import requests
import pandas as pd
import json

#Set your parameters for the API query
payload = {'experiment-id': 'besh', 'weeks': '1'}

response = requests.get('https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/', params = payload)



response_data = json.loads(response.content)[1]['data']
cozie_df = pd.read_json(response_data, orient='index')

print(cozie_df)


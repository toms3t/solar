import requests
import json
from datetime import date
from secrets import solaredge_api_key, site_id
from decimal import Decimal, getcontext


start_date = '2022-02-07'
today = date.today()
today_formatted = today.strftime("%Y-%m-%d")
url = f'https://monitoringapi.solaredge.com/site/{site_id}/energy?timeUnit=DAY&endDate={today_formatted}&startDate={start_date}&api_key={solaredge_api_key}'

r = requests.get(url)
j = json.loads(r.text)
day_count = len(j['energy']['values'])
avg_daily_usage_watts = sum([x['value'] for x in j['energy']['values']])/day_count
avg_daily_usage_kwh = round(avg_daily_usage_watts/1000, 3)

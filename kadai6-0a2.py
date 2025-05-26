import requests

APP_ID = "2bf15cea0a5c270fd8c02c203636dc666019e6b4"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,

"LANG":"J",
"STATS_DATA_ID":"0003343391",
"NARROWING_COND":"",
"DATA_FORMAT":"J",
"METAGET_FLG":"Y",
"EXPLANATION_GET_FLG":"Y",
"ANNOTATION_GET_FLG":"Y",
"REPLACE_SP_CHARS":0,
"CNT_GET_FLG":"N",
"SECTION_HEADER_FLG":1
    
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)

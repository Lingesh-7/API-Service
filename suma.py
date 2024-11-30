import requests
import requests
#  6a90e58c-7ade-46c3-a62b-aca481e22f77
print("2024-09-30T00:00:00+0000".split('T')[0])
# url="https://api.openbrewerydb.org/v1/breweries"

# # auyth="q9GX1aDDj_Xp4TWdLMhP"
# para={
#     "by_country": "illinois"
# }
# response=requests.get(url=url,params=para)
# print(response.json())
# for i in response.json():
#     print(i['name'])

# url = "https://api.marketstack.com/v1/eod?access_key=8445a652db9735d5c1cd67230f51d30d"

# querystring = {
#     "symbols":"AAPL",
#     'exchange':"XNAS",
#     'sort':'DESC',
#     'date_from':'2024-10-06',
#     'date_to':'2024-10-08'
#     }

# response = requests.get(url, params=querystring)

# data_=response.json()
# for i in data_['data']:
#     print(i['date'])
# url="http://api.marketstack.com/v1/"

# param={
#     'access_key':"8445a652db9735d5c1cd67230f51d30d",
#     'symbol':"AAPL",
#     'exchange':"XNAS",
#     'sort':'DESC',
#     'date_from':'2024-10-06',
#     'date_to':'2024-10-08',

# }

# data=requests.get(url=url,params=param)
# print(data.json())
# exchange=StringField(label="Exchange",validators=[DataRequired()])
#     sort=StringField(label="Sort:DESC/ASC")
#     date_from=StringField(label="Date From")
#     date_to=StringField(label="Date To")
#     limit=StringField(label="Limit")
#     submit=SubmitField(label="GET!")
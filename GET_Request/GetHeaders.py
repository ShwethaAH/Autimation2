import requests

headerdata= {'T1':'header1','T2':'Header2'}
response= requests.get('https://httpbin.org/get',headerdata)
print(response.text)
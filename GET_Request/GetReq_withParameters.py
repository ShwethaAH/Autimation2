import requests

parameter= {'name':'testworld','email':'test@123.con', 'number':'1313'}
response= requests.get('https://httpbin.org/get', params=parameter)
print(response.text)
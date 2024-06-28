import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users"

#read input file
file= open('C:\\Users\\ShwethaHagedal\\Downloads\\API Learning\\CreateUser.json','r')
json_input = file.read()
req_json=json.loads(json_input)
#read and parse
print(req_json)

#make POST req with json input body
response=requests.post(url,req_json)
print(response.content)
print("**********")

#validating response code
assert response.status_code==201

#fetch header from response
print(response.headers)
print("**********")
print(response.headers.get('Content-Length'))
print("**********")

#parse response to json format
resp_json= json.loads((response.text))
#pick id using json path , every time we run ll get new id inserted via POST
id=jsonpath.jsonpath(resp_json,'id')
print(id[0])







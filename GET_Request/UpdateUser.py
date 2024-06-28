import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users/2"

#read input file
file= open('C:\\Users\\ShwethaHagedal\\Downloads\\API Learning\\CreateUser.json','r')
json_input = file.read()
req_json=json.loads(json_input)
#read and parse
print(req_json)

#make PUT req with json input body
response=requests.put(url,req_json)
print(response.content)
print("**********")

#validating response code
assert response.status_code==200

#parse response content
reponse_json=json.loads(response.text)
updated_li = jsonpath.jsonpath(reponse_json,'updatedAt')
print(updated_li[0])
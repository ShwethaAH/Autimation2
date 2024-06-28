import requests
import json
import jsonpath

#API URL reqres.in
url="https://reqres.in/api/users?page=2"

#send GET req
obj= requests.get(url)
print(obj)

#parse response to json format
json_obj=json.loads(obj.text)
print(json_obj)
print("========")

#fetch value  using json path
pages=jsonpath.jsonpath(json_obj,'total_pages')
print(pages[0])
#validate ans is 2 but we are giving 5 , so error ll display
#assert pages[0]==5

#fetch all first name from response
for i in range(0,3):
    firstname=jsonpath.jsonpath(json_obj,'data['+str(i)+'.first_name')
    print(firstname[0])


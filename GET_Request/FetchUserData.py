import requests

#API URL reqres.in
url="https://reqres.in/api/users?page=2"

#send GET req
obj= requests.get(url)
print(obj)

#display response
print(obj.content)
print(obj.headers)

#validate status code
print(obj.status_code)
assert obj.status_code == 200

#fetch response headers
print(obj.headers)
print(obj.headers.get('Date'))
print(obj.headers.get('Server'))

#fetch cookies
print(obj.cookies)
print(obj.encoding)
print(obj.elapsed)

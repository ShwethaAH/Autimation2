import requests

#API URL reqres.in
url="https://reqres.in/api/users?page=2"

#send GET req
dltobj= requests.delete(url)
print(dltobj)

print(dltobj.status_code)

assert dltobj.status_code == 204
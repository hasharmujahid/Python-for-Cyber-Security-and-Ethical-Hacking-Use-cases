import jwt

payload_data= {
    'name': 'admin',
    'iat': '1234354545',
    'eat': '4345453452'
}
token=jwt.encode(payload=payload_data,
                 key='my secret key')

print(token)
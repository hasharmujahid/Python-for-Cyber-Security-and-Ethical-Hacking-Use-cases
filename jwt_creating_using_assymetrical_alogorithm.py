import jwt
from cryptography.hazmat.primitives import serialization

private_key = open("../ssh/id_rsa", 'r').read()

key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

payload_data = {
    'name': 'admin',
    'iat': '1234354545',
    'eat': '4345453452'
}
token = jwt.encode(
    algorithm='RS256',
    key=key,
    payload=payload_data

)

print(token)

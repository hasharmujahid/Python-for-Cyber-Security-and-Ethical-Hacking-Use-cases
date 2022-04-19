import jwt
from cryptography.hazmat.primitives import serialization

# load the public key

public_key = open('../ssh/id_rsa.pub', 'r').read()

# create key

key = serialization.load_ssh_public_key(public_key.encode())

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJpYXQiOiIxMjM0MzU0NTQ1IiwiZWF0IjoiNDM0NTQ1MzQ1MiJ9.TmlZ3Bd1MmqXaaWVwx82tIgKr7uWZ56j7-1qkTHB0pJJPCPeFlUI6hXgYyKu5XPULkcoWRckCsFxzpk4aLhq5cCCf1VzGbFzXQXUqb1TRb_kadKfTHCsvpgzkKHFeqIviJR961J2RSl3SjywG0pClk5gx4MuIsiR6sqbKoj8htkCh9Yi5PxQyd5L0iSfq7DF-ytFVhNi4YqYOaPFRJGSjDQBxDsaUi4Q_7RaxcXs_Hr8N9F6oSkeqzQJRZvwMTWEpMBGLGlu1RNpaYY6SNmqmK9lnV1qb5l_aEtse3884jZglsz-_3h2bmWG7EmkeItciOP_WXYxAvfGzvhSUKBrB3MQGltti-qL98OTgopC_HL1bfCiqnJ0QM7A-UFehrnM3EyQ-GJzswT-Rh62J-oChwEdoCRKjVxPToKJvzAL73QEmVXYbPuil2PQ7ogArl6lx_0Rmqgax-u2jj9lAO9BWo4aqjZ_92BAnvZYf9-bGDSrlaLc2JH4W7eHxm8TS1fB"

# decode

decode=jwt.decode(jwt=token, key=key, algorithms=['RS256', ])
print(decode)
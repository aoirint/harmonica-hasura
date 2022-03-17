from dotenv import load_dotenv
load_dotenv()

import os
import time
import json
import jwt

jwt_secret = json.loads(os.environ['HASURA_GRAPHQL_JWT_SECRET'])
secret_key = jwt_secret['key']

# https://hasura.io/docs/latest/graphql/core/auth/authentication/jwt.html
encoded_jwt = jwt.encode(
  payload={
    'sub': '1',
    'name': 'user',
    'admin': False,
    'iat': int(time.time()),
    'https://hasura.io/jwt/claims': {
      'x-hasura-allowed-roles': 'user',
      'x-hasura-default-role': 'user',
      'x-hasura-user-id': '1',
    },
  },
  key=secret_key,
  algorithm='HS256',
)

print(encoded_jwt)

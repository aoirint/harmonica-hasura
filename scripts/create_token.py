import os
import time
import json
import jwt

def create_token(
  secret_key: str,
  user_id: str,
  role: str,
) -> str:
  # https://hasura.io/docs/latest/graphql/core/auth/authentication/jwt.html
  encoded_jwt = jwt.encode(
    payload={
      'sub': user_id,
      'name': role,
      'admin': False,
      'iat': int(time.time()),
      'https://hasura.io/jwt/claims': {
        'x-hasura-allowed-roles': [role],
        'x-hasura-default-role': role,
        'x-hasura-user-id': user_id,
      },
    },
    key=secret_key,
    algorithm='HS256',
  )
  return encoded_jwt


if __name__ == '__main__':
  from dotenv import load_dotenv
  load_dotenv()

  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('--user_id', type=str, required=True)
  parser.add_argument('--role', type=str, required=True)
  args = parser.parse_args()

  jwt_secret = json.loads(os.environ['HASURA_GRAPHQL_JWT_SECRET'])
  secret_key = jwt_secret['key']

  user_id = args.user_id
  role = args.role

  token = create_token(secret_key=secret_key, user_id=user_id, role=role)
  print(token)

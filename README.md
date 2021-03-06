# Harmonica Hasura

## Python Utility

### Create JWT Token

```shell
python3 -m venv venv

# Linux, macOS
source venv/bin/activate
# Windows
source venv/Scripts/activate

pip3 install -r scripts/requirements.txt

python3 scripts/create_token.py --user_id 1 --role sensor
python3 scripts/create_token.py --user_id 2 --role client
```

### Generate requirements.txt

```shell
pip3 install pip-tools

pip-compile scripts/requirements.in
```

## Maintenance

### Update database structure

```shell
# On development machine,
docker-compose up -d
hasura console --project ./hasura --endpoint=http://127.0.0.1:8080/ --admin-secret myadminsecretkey

git add .
git commit
git push

# On server,
git pull
docker-compose up -d --force-recreate
```

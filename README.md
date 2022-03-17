# Harmonica Hasura

## Python Utility

### Create JWT Token

```shell
python3 -m venv venv

# Linux, macOS
source venv/bin/activate
# Windows
source venv/Scripts/activate

pip3 install -r scripts/requiments.txt

python3 scripts/create_token.py
```

### Generate requirements.txt

```shell
pip3 install pip-tools

pip-compile scripts/requirements.in
```

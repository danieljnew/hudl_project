# HUDL Sample Login Tests


## Prerequisites
- Chrome 94
- Python 3
- Chromedriver 94

## Installation Steps

- Clone this repo
- create a virtual env ex. python3 -m venv environments/hudl
- activate virtual env ex. source environments/hudl/bin/activate
- cd into project root
- pip install -r requirements.txt
- copy config.json file into project root (Daniel can give you this either through Google drive share, lastpass or some other file sharing system)
- add path to chromedriver on host machine to CHROME_BINARY_PATH in const.py

## Executing Tests

- pytest tests/test_login.py
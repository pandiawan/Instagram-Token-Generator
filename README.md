## Instagram Token Generator
Instagram bearer or cookies generator

### Requirements
- Python 3.8+

### Configuration
- Install requirements
```bash
$ pip install -r requirements.txt
```
- Copy `config.py.example` to `config.py`
```bash
$ cp config.py.example config.py
```
### Example
#### Bearer Version 
```
from instagram import InstagramLogin

username = 'xxxxxxx'
password = 'xxxxxxx'

ig = InstagramLogin()
response, bearer = ig.generate_bearer(username, password)
if "logged_in_user" in response:
    print(bearer)
else:
    print("Error login `{}` with error: `{}`".format(username, response['message']))

```

#### Cookie Version 
```
from instagram import InstagramLogin

username = 'xxxxxxx'
password = 'xxxxxxx'

ig = InstagramLogin()
response, cookies = ig.generate_cookie(username, password)
if "logged_in_user" in response:
    print(cookies)
else:
    print("Error login `{}` with error: `{}`".format(username, response['message']))
```


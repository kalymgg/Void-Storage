

# Void Storage

It's a password generator, which uses your credentials as a seed. That means that you only have to remember your Void credentials to recalculate your password whenever you need it.

## Pro's and Con's
[+] User data can't be compromised (cause there's no data to store), unless your machine/local network is.   
[+] No Signup needed. Just pick some credentials and keep them safe.   
[-] If you lost your Void credentials, there's no way out. You're doomed.   

Demo: [click](https://kalymgg.pythonanywhere.com/)


# Pay Attention!

The generator depends on python's random() function. If it's algorithm ever change, you will get different results for your old credentials, so run the test when changing your python version from the original (Python 3.8.5) to make sure nothing changed:

```bash
python3 VoidStorage.py
```

## Module Usage

```python
from VoidStorage import voidStorage

login, password = 'VoidLover', 'qwerty123'
storage = voidStorage(login, password) # Init storage

domain, user = 'youtube.com', 'youtubeLover@gmail.com'
password = storage.findPassword(domain, user) # Get password for service

print(password)
```
##  Deploy A Server!
(Flask required)
```bash
python3 server.py
```
Then visit 0.0.0.0:8080 or access via API:
```bash
curl -v -XGET 'http://0.0.0.0:8080/api/void?login=VoidLover&pass=qwerty123&domain=youtube.com&user=youtubeLover@gmail.com'
```
Returns 8 digit string.



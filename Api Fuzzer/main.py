import requests
import sys


def loop():
    for word in sys.stdin:
        res = requests.get(url=f"https://example.com/api/{word}")
        if res.status_code == 404:
            loop()
        else:
            print(res)
            data = res.json() 
            print(data)
loop()
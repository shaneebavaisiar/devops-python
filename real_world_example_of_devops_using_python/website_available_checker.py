import requests
url="https://examplessfa.com"

try:
    response = requests.get(url)
    print(f"{url} is UP and the status code is :{response.status_code}")
except requests.ConnectionError:
    # print(f"{url} is down")
    print(e)
finally:
    print("the session closed !!!")
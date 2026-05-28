import urllib.request
req = urllib.request.Request("http://127.0.0.1:4521/ws/chat/", headers={"Connection": "Upgrade", "Upgrade": "websocket"})
try:
    with urllib.request.urlopen(req) as response:
        print(response.status)
except Exception as e:
    print(e)

import requests
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'list':
    resp = requests.get("http://localhost:8888/list")
    print(resp.text)
elif len(sys.argv) > 2 and sys.argv[1] == 'upload':
    print(sys.argv[2])
    r = requests.post('http://localhost:8888/upload',
                      files={'file': open(sys.argv[2], 'rb')})
    print(r.content)

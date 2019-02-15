import requests

response = requests.get('https://api.github.com/repos/atom/atom').json()
print(response)
for i in range(1000):
    print(i+1)
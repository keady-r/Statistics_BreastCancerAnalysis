import requests
url = "http://google.com"
response = requests.get(url)
print (response.text)
import requests

url = 'http://172.18.58.80/hr2/'
webpage = requests.get(url)

print(webpage.text)

print("status code:")
print("\t",webpge.status_code)
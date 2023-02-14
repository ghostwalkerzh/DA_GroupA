import requests

url = 'http://www.wikipedia.org'
webpage = requests.get(url)

print(webpage.text)

print("Status code:")
print("\t *", webpage.status_code)

h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])

print("**********")

headers = {'User-Agent' : 'Iphone 14'}

url2 = 'http://httpbin.org/headers'
request_header = requests.get(url2, headers=headers)
print(request_header.text)
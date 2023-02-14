import requests

url = 'http://172.18.58.80/hr2/'
webpage = requests.get(url)

print(webpage.text)

print("Status code:")
print("\t *", webpage.status_code)

h = requests.head(url)
print("Header:")
print("==========================================")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])

print("==========================================")

headers = {'User-Agent' : 'Mobile'}

#url2 = 'http://httpbin.org/headers'
request_header = requests.get(url, headers=headers)
print(request_header.text)




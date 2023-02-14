import requests
#Libraries required
#requests, urllib3, w3lib, scrapy

url = 'http://172.18.58.80/hr2/'
#Step 4
webpage = requests.get(url)
print(webpage.text)

#For status code
#Step 5
print("Status code:")
print("\t *", webpage.status_code)

#Step 6
h = requests.head(url)
print("Header:")
print("==========================================")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("==========================================")

#Step 7
headers = {'User-Agent' : 'Mobile'}

'''
#TBD remove comment and uncomment chunk if incorrect and required to dsiplay UA
#url2 = 'http://httpbin.org/headers'
request_header = requests.get(url, headers=headers)
print('==========================================================================')
print(request_header)
'''



import requests

#set the target webpage
url = 'http://www.wikipedia.org'
webpage = requests.get(url)

#this will get the full webpage in text
print(webpage.text)

#get and print the status code
print("Status code:")
print("\t *", webpage.status_code)

#get the headers
h = requests.head(url)
print("Header:")
print("**********")
#to print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])

print("**********")

#modify the headers user-agent
headers = {'User-Agent' : 'Iphone 14'}

#Test it on an external site
url2 = 'http://httpbin.org/headers'
request_header = requests.get(url2, headers=headers)
print(request_header.text)
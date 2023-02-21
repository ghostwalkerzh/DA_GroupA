import requests
import unittest
#Libraries required
#requests, urllib3, w3lib, scrapy

url = 'http://172.18.58.80/hr2/'
#Step 4
'''
webpage = requests.get(url)
print(webpage.text)
'''
#For status code
#Step 5
'''
print("Status code:")
print("\t *", webpage.status_code)
'''
#Step 6
h = requests.head(url)
'''
print("Header:")
print("==========================================")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("==========================================")
'''
#Step 7
headers = {'User-Agent' : 'Mobile'}

'''
#TBD remove comment and uncomment chunk if incorrect and required to dsiplay UA
#url2 = 'http://httpbin.org/headers'
request_header = requests.get(url, headers=headers)
print('==========================================================================')
print(request_header)
'''

#Testing
class testingprogram(unittest.TestCase):
    def test_url(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print(url, 'URL request is successful, Code 200')
            else:
                print(url, 'Requested URL is not found')
        except Exception as e:
            print(url, "Error:", {e})
    def test_getheader(self):
        print("Web Header:")
        print("==========================================")
        for x in h.headers:
            print("\t ", x, ":", h.headers[x])
        print("==========================================")
if __name__ == '__main__':
    unittest.main()

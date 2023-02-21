import requests
import unittest
#Libraries required
#requests, urllib3, w3lib, scrapy

url = 'http://172.18.58.80/hr2/'
url2 = 'http://httpbin.org/headers'

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
request_header = requests.get(url2, headers=headers)
print('==========================================================================')
print(request_header.text)
'''

#Testing
class testingprogram(unittest.TestCase):
    def test_url(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print("=====================Response=====================")
                print(url, 'URL request is successful, Code 200')
                print("=====================Response=====================")
            else:
                print("=====================Response=====================")
                print(url, 'Requested URL is not found')
                print("=====================Response=====================")
        except Exception as e:
            print("=====================Response=====================")
            print(url, "Error:", {e})
            print("=====================Response=====================")
    def test_getheader(self):
        print("Web Header:")
        print("=====================Website Header=====================")
        for x in h.headers:
            print("\t ", x, ":", h.headers[x])
        print("=====================Website Header=====================")
    def test_useragentmod(self):
        request_header = requests.get(url2, headers=headers)
        print('=====================User-Agent Modification Demostration=====================')
        print(request_header.text)
        print('=====================User-Agent Modification Demostration=====================')
    def test_printwebpage(self):
        print('=====================Webpage in Text=====================')
        webpage = requests.get(url)
        print(webpage.text)
        print('=====================Webpage in Text=====================')
if __name__ == '__main__':
    unittest.main()

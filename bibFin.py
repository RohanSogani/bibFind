import scholarly
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import sys
import os
import re
import requests

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

paper = input("Enter Research Paper Name --> ")
search_query = scholarly.search_pubs_query(paper)
with Capturing() as output: 
    print(next(search_query))

print(output)
stringfyOutput = str(output)

urlContainer = re.findall(r'(https?://[^\s]+)', stringfyOutput)

bibTexUrl = urlContainer[-1]
#Remove extra character, will improve in future
bibTexUrl = bibTexUrl[:-4]
print(bibTexUrl)

request_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

with requests.Session() as s:
    r = s.get(bibTexUrl, headers=request_headers)

os.system('clear')
print("Status Code -->", r)
print("BibTex for ",paper," is")
print(r.text)


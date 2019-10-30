import scholarly
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import sys
import re
import urllib.request

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
print(bibTexUrl)


with urllib.request.urlopen(bibTexUrl) as response:
   html = response.read()


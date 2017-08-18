
import urllib.request
import re
link="https://en.wikipedia.org/wiki/Decimal"
f=urllib.request.urlopen(link)
myfile=f.read()
s=re.findall(r'<p>(.*?)</p>',str(myfile))
sentences=re.split(r'[.?!][ ]*',str(s))
for x in sentences:
    print(x)

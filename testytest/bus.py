# Project Catching the Bus
# https://www.safaribooksonline.com/library/view/python-programming-language/9780134217314/PYMC_01_02.html
import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22')
data = u.read()

from xml.etree.ElementTree import XML

doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)

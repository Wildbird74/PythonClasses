# Project: Reading Command Line Arguments and Making a Script
# https://www.safaribooksonline.com/library/view/python-programming-language/9780134217314/PYMC_01_03.html
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: script.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid,route))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
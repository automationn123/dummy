'''
Created on 19-Mar-2014

@author: ARCHANA
'''
import urllib2 
from bs4 import BeautifulSoup
import re
url = ('http://espn.go.com/mens-college-basketball/schedule?date=20140319')
opener = urllib2.build_opener()
ourUrl = opener.open(url).read()
pTitle = re.compile('<title>(.*)</title>')

pLink = re.compile('<link rel.*href="(.*)"/>')

findTitle = re.findall(pTitle,url)
findLink = re.findall(pLink,url)

listIterator =[]
listIterator[:] =range(3,10)
for i in listIterator:
    print pTitle[i]


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
soup = BeautifulSoup(ourUrl)
title = soup.title.text
body = soup.findAll('title')
outfile = open('E:\projectpython\wiki.txt','w') 
for i in body:
    i = re.sub('\[/d\]', '', str(i))
    outfile.write(str(i) + '\n\n')  
 


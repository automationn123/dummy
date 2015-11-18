'''
Created on 04-Mar-2014

@author: ARCHANA
'''
import urllib2
import xlwt
from bs4 import BeautifulSoup
url = urllib2.urlopen("http://espn.go.com/mens-college-basketball/schedule?date=20140319")
soup = BeautifulSoup(url)
#workbook = xlwt.Workbook()
#worksheet = workbook.add_sheet('ESPN')
for td in tr.find_all("td"):
    print td



        
    
'''
Created on Mar 19, 2014

@author: Fissionlabs
'''
from bs4 import BeautifulSoup
import xlwt
import requests
rcount = -1
#url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get("http://espn.go.com/mens-college-basketball/schedule?date=20140321")
data = r.text
soup = BeautifulSoup(data)
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('ESPN')
for row in soup.find_all('tr'):
#     for row in soup.find_all('td'):
    rcount = rcount+1
    data= row.getText()
#     fdata=data[data.index("("):data.index(")")]
    print data.find('(')
#     print(fdata)
    worksheet.write(rcount,0,row.getText())
#         print("*******************************")
workbook.save('espn.xls')

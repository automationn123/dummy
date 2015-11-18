'''
Created on 25-Mar-2014

@author: Rohitha
'''
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from pytz import timezone
import json
import pytz
import requests
import time
import urllib
import urllib2
import xlwt
payload = {'kaveInfoRequired': 'NO', 'fankaveId': '5sjXiF95bJ', 'leagueId': 'NBA','date': '2014-03-31','endDate':'2014-04-08','apiVersion': '1.0.4'}
r = requests.post("http://staging.fankave.com/Fankave/get/schedule", data=payload)
print r.text
data = json.loads(r.text)
file = open("newfile.txt", "w")
time_format='%H:%M:%S'
listvalues=["awayFirstName","homeFirstName","status","channel"]
count = -1
for dump in  range(len(data["Schedule"])):
    t = datetime.strptime(data["Schedule"][dump]       ["scheduledTime"],"%H:%M:%S")
    deltatime = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    pst_time = deltatime +timedelta(hours = -4)
    pst_time = str(datetime.strptime(str(pst_time),"%H:%M:%S").strftime("%I:%M %p")) 
    count = count +1
    file.write(pst_time+',')
    for values in listvalues:
        file.write(data["Schedule"][dump][values]+',')
    file.write('\n')
#worksheet.write(count,0,data["Schedule"][dump][values]) 
file.close()



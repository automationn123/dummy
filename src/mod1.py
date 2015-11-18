'''
Created on 03-Mar-2014

@author: ARCHANA
'''
import os
import sys
import subprocess
p = subprocess.Popen("adb devices", stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print output
print err
device="4300bf1c77bbcf00"
debugapk="C:/Users/ARCHANA/Desktop/resign/PeelTab-Prod-Market-Release-jenkins-PeelTab-Master-market-417_debug.apk"
cmd = "E:/ROBOTIUM/adt-bundle-windows-x86_64-20131030/sdk/platform-tools/adb -s"+device+" install "+debugapk
# p = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True).wait()
# print "success"
os.system(cmd)
Targetpackagename = "com.peel.app"
cmd = "E:/ROBOTIUM/adt-bundle-windows-x86_64-20131030/sdk/platform-tools/adb -s"+device+" uninstall "+Targetpackagename
p = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True).wait()
print "success"





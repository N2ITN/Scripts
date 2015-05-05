# This script allows the user to download all lab login files hosted on CT Berkely lab's portal
# It also serves as an example of HTTP requests, HTML parsing, and file downloading methods

import requests
# HTTP requests (third party module)
from bs4 import BeautifulSoup as bs
# HTML parsing (third party module)
import re
# regular expressions
import os
# for file manipulation



###### User specific variables ########
projectnum = ''
# Example C1234


user = ''
password = ''
# Your login credentials go here

myFolder = r''
# Location to download requested files

########################################


LoginList = []
PayloadList = []
# declare empty lists


mainPage = "https://labline.ctberk.com/app/PortalProjectMenu"
#login page
linkPage = ["https://labline.ctberk.com/app/PortalProject?projectnum=C1374"]
#page with links to iterate on



AUTH = user, password
URL = mainPage
payload = {
    'login_id': user,
    'login_password': password,
     'cmd_login' : 'Log In',
    'persistent': '1'  }
# dictionary data structure to create login session

s = requests.Session()
s.post(URL, data=payload)
# login and create seesion


prefix = "https://labline.ctberk.com"

suffix = "/app/PortalProject?projectnum=" + projectnum

filePage = prefix + suffix
ZZZ = s.get(filePage)


def getLinks(key):
	soup = bs(key.text)

	links = soup.findAll("a",href=True)

	return links


Loginlinks = getLinks(ZZZ)

for link in Loginlinks:
    if re.findall('loginnum', link['href']):
        URL1 = prefix + link['href']
        LoginList.append(URL1)
# get list of links to pages with lab login info


for login in LoginList:
	Login = str(login[-6:])
	loginPage = s.get(login)	
	payload = getLinks(loginPage)
# get list links from lab login pages

	for link in payload:
		tempList = []
		if re.findall('deliverable', link['href']) or re.findall('&num=', link['href']):
			lText =  str(link.get_text()).strip()
			URL1 = prefix + link['href']
			PayloadList.append(URL1)
			tempList.append(URL1)
		# filer list for only only the applicable files 

			for item in tempList:
				print item
				print Login
				print "lText: %s" %lText
				print
				if "EDD" in lText:
					ext = ".zip"
				else: ext = ".pdf"
			# append file extensions


				if os.access(Login,os.F_OK) == False:
					os.mkdir(Login)

				fFile = s.get(item)

				f = open(myFolder+Login + "\\"+ Login+ "_" + lText + ext,'wb')
				f.write(fFile.content)
				f.close 
				# download all files

			




# This module will download weather data from a university site and format the data
# that lie within a speficic time range into an excel document with conditional formatting

# It is set up my default to collect 24-hour precipiation data from North Boeing Field in Seattle


import requests

from bs4 import BeautifulSoup as bs

import re

import os

import urllib

from datetime import datetime


def KBFI(var):
	#var can be integer or date in m/d/yyyy format

	if var== 0:
		return

	vType =type(var)
	
	date_format = "%m/%d/%Y"
	i = datetime.now()
	todayString= str(i).split(" ")[0]

	DAY = todayString.split("-")[2]
	MONTH =  todayString.split("-")[1]
	YEAR =  todayString.split("-")[0]

	if vType == int:
		DAYS = str(var)
	elif vType == str:

		sDate = var
		now = i.strftime(date_format)
	
		today = datetime.strptime(now, date_format)

		
		startDate = datetime.strptime(sDate, date_format)



		DAYS = today - startDate
		DAYS =  str(DAYS).split(" ")[0]



	url = 'http://httpbin.org/digest-auth/auth/user/pass'

	LoginList = []
	PayloadList = []
	mainPage = "http://mesowest.utah.edu/cgi-bin/droman/my_login.cgi"
	# linkPage = 'http://mesowest.utah.edu/cgi-bin/droman/download_ndb.cgi?stn=KBFI&year1=2015&day1=8&month1=4&hour1=&timetype=LOCAL&unit=0'
	# linkPage2 = 'http://mesowest.utah.edu/cgi-bin/droman/meso_download_mesowest_ndb.cgi?product=&stn=KBFI&unit=0&time=LOCAL&daycalendar=1&day1=1&month1=04&year1=2015&yearcal=2015&hour1=13&monthcal=04&hours=1&output=Excel&order=1&TMPF=TMPF&RELH=RELH&SKNT=SKNT&GUST=GUST&DRCT=DRCT&QFLG=QFLG&CHC1=CHC1&CHC2=CHC2&CHC3=CHC3&CIG=CIG&HI6=HI6&LO6=LO6&PEAK=PEAK&HI24=HI24&LO24=LO24&PDIR=PDIR&PMSL=PMSL&ALTI=ALTI&P03D=P03D&PCHA=PCHA&P01I=P01I&P03I=P03I&P06I=P06I&P24I=P24I&RMK=RMK&RAW=RAW&ITIM=ITIM&UTIM=UTIM&WNUM=WNUM&VSBY=VSBY&DWPF=DWPF'
	linkPage3 = 'http://mesowest.utah.edu/cgi-bin/droman/meso_download_mesowest_ndb.cgi?product=&stn=KBFI&unit=0&time=LOCAL&daycalendar=1&day1='+DAY+'&month1='+MONTH+'&year1='+YEAR+'&yearcal='+YEAR+'&hour1=14&monthcal=04&hours='+ DAYS+ '&output=Excel&order=1&P24I=P24I'
	#page with links to iterate on

	user = 'ZESTELA'
	password = 'Mastodon'

	AUTH = user, password
	URL = mainPage
	payload = {
	    'user': user,
	    'password': password,
	     'submitted' : 'Login',
	    'persistent': '1'  # remember me
	}
	print 'connecting...'
	s = requests.Session()
	s.post(URL, data=payload)

	# print s.cookies


	f_out = open("KBFI.xls", "wb")
	x=s.get(linkPage3).content
	f_out.write(x)

	f_out.close()
	print 'file downloaded.'

def rainDictionary():
	print
	print 'processing...'
	import xlrd
	from xlrd import open_workbook, cellname, XL_CELL_TEXT

	rdBook = open_workbook("KBFI.xls")

	# open the path of the current file
	newRow = [ ]
	# print "Sheet names: "
	dateList = []
	pList = []
	rainyDaylist=[]
	rainList = []
	precip = 0

	for sheet in rdBook.sheets():
		MAXDATE = sheet.cell(1,0).value.split(" ",1)[0]
		# print MAXDATE
		MINDATE = sheet.cell(sheet.nrows-4,0).value.split(" ",1)[0]
		# print MINDATE

		for row_index in xrange(sheet.nrows): 

			if row_index > 0 and row_index < sheet.nrows-4:
				NEWDATE = str(sheet.cell(row_index,0).value.split(" ",1)[0])
				if not NEWDATE in dateList:
					dateList.append(NEWDATE)
					
				#make list of dates

				if len( str(sheet.cell(row_index,1).value)) > 1 and str(sheet.cell(row_index-1,0).value.split(" ",1)[0]) == NEWDATE:
				 	rainyDay = str(sheet.cell(row_index,0).value.split(" ",1)[0])
				 	precip =  sheet.cell(row_index,1).value
				 	rainyDaylist.append(rainyDay)
					pList.append(precip)

		for date in dateList:
			dayval =0
			if date in rainyDaylist:
				index = rainyDaylist.index(date)
				# print 'index:%s ' %index
				dayval = pList[index]
				# print 'dayval: %s ' %dayval
				rainList.append(dayval)
				continue
			rainList.append(dayval)

		return zip(dateList,rainList)

def xlOut():

	import os
	from xlwt import easyxf, Workbook
	rainD= rainDictionary()
	print 'writing output...'
	print
	st = easyxf('pattern: pattern solid;' 'align: vertical center, horizontal left,' 'wrap on')
	
	st.pattern.pattern_fore_colour = 47

	rt = easyxf('pattern: pattern solid;' 'align: vertical center, horizontal left,' 'wrap on')
	
	rt.pattern.pattern_fore_colour = 53
	# lt =easyxf('align: vertical center, horizontal center, wrap on;')
	
	
	lt = easyxf('align: vertical center, horizontal left, wrap on ; font: bold on' )
	
	wb = Workbook()
	ws = wb.add_sheet("Result")

	ws.write(0,0,"Date",lt)
	ws.write(0,1,"P24",lt)
	n=1

	for key in rainD:
		lt = easyxf('align: vertical center, horizontal left, wrap on;' )
			

		# print key
		# date = n,0,str(key[0],)
		p24=key[1]
		ws.write(n,0,str(key[0],),lt)
		if p24 > 0.4:
			lt = st
		if p24 > 1.0:
			lt = rt
		
		ws.write(n,1,str(key[1],),lt)
		
		n+=1
	wb.save('KBFI_report.xls')
	print 'launching file.'
	try:
		os.startfile('KBFI_report.xls')
		os.startfile('http://www.wrh.noaa.gov/forecast/wxtables/index.php?lat=47.544090665057986&lon=-122.31645584106445&table=custom&duration=7&interval=6')
	except:
		os.system("open KBFI_report.xls")



KBFI(7)
#Refreshes KBFI file
#Args can be:
	# int for days, 
	# 'm/d/yyyy 'for start date, 
	# or 0 for nothing

xlOut()
#processes KBFI file, makes new excel report and launches it





		 	
		 





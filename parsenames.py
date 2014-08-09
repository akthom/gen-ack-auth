#from http://ptigas.com/blog/2012/01/21/name2gender-in-python/

import glob
from bs4 import BeautifulSoup

files = glob.glob('names/*.html')

for f in files :
	html_data = open( f ,'r').read()

	soup = BeautifulSoup(html_data)
	year = soup.find(id="yob")['value']
	tables = soup.findAll('table')
	trs = tables[2].findAll('tr')
	for tr in trs[1:-1]:
		tds = tr.findAll('td')
		print "%s,%s,%s,%s" % (
                       tds[1].contents[0], 
                       tds[0].contents[0].replace(',',''), 
                       'male', 
                       year)
		print "%s,%s,%s,%s" % (
                       tds[3].contents[0], 
                       tds[2].contents[0].replace(',',''), 
                       'female', 
                       year)

#fin-script

import urllib
import pytz
import pandas as od
from bs4 import BeautifulSoup
from datetime import datetime
from pandas.io.data import DataReader


SITE = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
START = datetime(2000, 1, 1, 0, 0, 0, 0, pytz.utc)
END = datetime.today().utcnow()

hdr = {'Uer-Agent' : 'Mozilla/5.0'}
req = urllib.request.Request(site, headers=hdr)
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page)
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = list()
sector_tickers = dict()
for row in table.findAll('tr'):
	col = row.findAll('td')
	if len(col) > 0:
		ticker = str(col[0].string.strip())
		sector = str(col[3].string)
		if ticker not in tickers:
			tickers.append(ticker)
		if sector not in sector_tickers:
			sector_tickers[sector] = list()
		sector_tickers[sector].append(ticker)
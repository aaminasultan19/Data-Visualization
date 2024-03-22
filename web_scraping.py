# -*- coding: utf-8 -*-
"""Web Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WlkROUSAxscemJG4_FBUft46Tdz44V0M
"""

import requests
from bs4 import BeautifulSoup

def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://www.geeksforgeeks.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
	print(item['src'])
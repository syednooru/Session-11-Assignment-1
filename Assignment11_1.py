#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:29:28 2018

@author: apple
"""



from bs4 import BeautifulSoup
import urllib
from collections import Counter
import nltk

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
 
text = soup.get_text(strip=True)


tokens = [t for t in text.split()]
Counter(tokens)
freq = nltk.FreqDist(tokens)
 
for key,val in Counter(tokens).items():
    print (str(key) + ':' + str(val))
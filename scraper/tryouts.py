# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import requests
from lxml import html

URL = 'http://econpy.pythonanywhere.com/ex/001.html'
page = requests.get(URL)
tree = html.fromstring(page.content)
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')
print 'buyers', buyers
print 'prices', prices

# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import requests
from lxml import html

URL = 'http://www.espncricinfo.com/ci/engine/match/index.html'
page = requests.get(URL)
tree = html.fromstring(page.content)
c1 = tree.xpath('//div[@class="innings-info-1"]/text()')[0]
c2 = tree.xpath('//div[@class="innings-info-2"]/text()')[0]
s1 = tree.xpath('//span[@class="bold"]/text()')[1]
s2 = tree.xpath('//span[@class="bold"]/text()')[2]
print c1, s1
print c2, s2

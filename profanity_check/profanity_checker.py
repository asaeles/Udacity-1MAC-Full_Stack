import requests
import random
import re
from HTMLParser import HTMLParser
import os

def get_imdb_top_urls():
	url = 'https://www.imdb.com/chart/top'
	req = requests.get(url)
	ms = re.findall('\n<a href="(/title/tt\d+)', req.text)
	urls = []
	for m in ms:
		urls.append('https://www.imdb.com' + m)
	return urls

def get_quotes(url):
	url = url + '/quotes'
	req = requests.get(url)
	m = re.search("<title>([^<]+) - Quotes - IMDb</title>", req.text)
	text = HTMLParser().unescape(m.group(1))
	m = re.search("we don't have any Quotes", req.text)
	if m != None:
		return None
	ms = re.findall('<span class="character">([^<]+).+?</a>:[\r\n]+(\[[^\]]+][\r\n]+)?([^<]+)', req.text)
	for m in ms:
		text += "\r\n" + HTMLParser().unescape(m[0]) + ': ' + HTMLParser().unescape(m[2])
	return text

# Prepare Top Quotes file
# os.chdir(os.path.realpath(os.path.dirname(__file__)))
# f = open("top_quotes.txt", "w", 5)
# for url in get_imdb_top_urls():
# 	quotes = get_quotes(url)
# 	if quotes != None:
# 		f.write(quotes.encode('utf8') + "\r\n-----------\r\n")
# f.close()

f = open("top_quotes.txt", "r")
line_num = 0
for line in f:
	line_num += 1
	m = re.search("^[\t ]*$", line)
	if m != None:
		continue
	req = requests.get('http://www.wdylike.appspot.com/?q=' + line)
	if req.text == 'true':
		print str(line_num) + ' --> ' + line
print "Done"


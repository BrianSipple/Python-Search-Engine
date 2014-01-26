#python3... import urllib.request
from bs4 import BeautifulSoup
from getpage import get_page
from webcorpus import WebCorpus


# Deprecated by choosing to use BeautifulSoup
#
#def get_next_url(text):
#	"""
#	Helper method when crawling a webpage. Finds the next HTML "<a href=" tag,
#	then finds the url string in betwreen quotes.
#	Url is returned -- along with the position of the url_enQuote 
#	so the method can be called continuously (i.e. recursively) within a page
#	"""
#	link_start = text.find('<a href=')
#	if link_start == -1:
#		return None, 0
#	else:
#		url_startQuote = text.find('"', link_start)
#		url_endQuote = text.find('"', url_startQuote + 1)
#		url = text[ (url_startQuote + 1) : url_endQuote]
#	return url, url_endQuote



def getAllLinks(page):
	soup = BeautifulSoup(page)
	links = []
	for link in soup.find_all('a'):
		links.append(link.get('href'))
	return links


def isImportant(link):
	"""an important link contains a bold tag, or is containted within a bolbe tag"""
	return link.find('b') or link.find_parent('b')



def boldLinks(page):
	soup = BeautifulSoup(page)
	links = soup('a')
	return set([link.get('href') for link in links if isImportant(link)])




def crawlWeb(seed):
	toCrawl = set([seed])		#start with a seed page
	crawled = []			#keep a record of sites crawled to prevent repeat visits
	wcorpus = WebCorpus()
	while toCrawl:
		url = toCrawl.pop()					
		if url not in crawled:				#check whether already crawled
			content = get_page(url)		#read-in all of the page's html text
			outlinks = getAllLinks(content)  #store outlinks in var for building graph
			for outlink in outlinks:
				wcorpus.add_link(url, outlink)
			for word in content.split():
				wcorpus.add_word_occurrence(url, word)
			toCrawl.update(outlinks)		#add outlinks to toCrawl stack if we haven't cralwed already
			crawled.append(url)				#store page that we popped in crawled. 
	return wcorpus	


















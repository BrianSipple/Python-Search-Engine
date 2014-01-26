# Gets the underlying HTML of a webpage
def get_page(url):
	try:
		import urllib.request
		return urllib.request.urlopen(url).read().decode('utf-8')
	except:
		return ""

	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""
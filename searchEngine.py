import urllib.request

# Gets the underlying HTML of a webpage
def get_page(url):
	try:
		import urllib.request
		return urllib.request.urlopen(url).read().decode('utf-8')
	except:
		return ""


def get_next_url(text):
	link_start = text.find('<a href=')
	if link_start == -1:
		return None, 0
	else:
		url_startQuote = text.find('"', link_start)
		url_endQuote = text.find('"', url_startQuote + 1)
		url = text[ (url_startQuote + 1) : url_endQuote]
	return url, url_endQuote



def get_all_links(text):
	links = []
	while (True):
		url, url_endQuote = get_next_url(text)
		if url:
			links.append(url)
			text = text[url_endQuote:]
		else:
			break
	return links


def union(a, b):
	for x in b:
		if x not in a:
			a.append(x)
	return a	


def crawlWeb(seed):
	toCrawl = [seed]
	crawled = []
	index = {}
	graph = {}
	while toCrawl:
		page = toCrawl.pop()					
		if page not in crawled:				#check whether already crawled
			content = get_page(page)
			add_page_to_index(index, url, content)
			outlinks = get_all_links(content)  #store outlinks in var for building graph
			graph[page] = outlinks
			union(toCrawl, outlinks)		#if not, crawl... and union the page's returned link array
			crawled.append(page)			#store page that we popped in crawled. 
	return index, graph	



#Creating a keyword/URL index

index = {}

def add_to_index(index, keyword, url):
	# Format of index: [[keyword, [url, count], [url, count]]
	for entry in index:
		if entry[0] == keyword:
			for link in entry[1]:
				if link[0] == url:
					return
			entry[1].append([url, 0])
			return
	index.append([keyword, [[url, 0]]])




def record_user_click(index, keyword, url):
	for entry in index: 		#Going through each word in index
		if entry[0] == keyword:
			for link in entry[1]:	#Going through the urls that are attached  to the keywords
				if link[0] == url:
					link[1] += 1	#Increase the count of the link
	


def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []



# Grab keywords from loading a page's text and call add_to_index


def add_page_to_index(index, url, content):
	 words = content.split()
	 for word in words:
	 	add_to_index(index, word, url)



# Computing the PageRank!

def compute_ranks(graph):
	d = 0.8   	#damping factor
	numLoops = 10

	ranks = {}
	npages = len(graph)		#graph is the dictionary of nodes
	for page in graph:
		ranks[page] = 1.0 / npages		#initialize each page and its starting rank

	#update the new ranks based on the old ranks
	for i in range(0, numLoops):
		newranks = {}
		for page in graph:
			newrank = (1 - d) / npages
			#update by summing in the inlink ranks
			for node in graph:			 #loop through the graph asynchronously to check for another node that links to page
				if page in graph[node]:  # node links to page, so we add to newrank based on the rank of this node. 
					newrank = newrank + d * (ranks[node] / len(graph[node]))
			newranks[page] = newrank
		ranks = newranks
	return ranks



#LuckySearch for finding the best rank

def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
    	return None
    best = pages[0]
    for x in pages[1:]:				#Iterate through each page, comparing ranks and upataing when necessary
        if ranks[x] > ranks[best]:
            best = x
    return best
   













 

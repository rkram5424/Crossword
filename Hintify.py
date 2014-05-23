import urllib, urllib2, re
from BeautifulSoup import BeautifulSoup

class Hintify:

	def __init__(self, word):
		word = word.replace(' ', '_')
		wiki_url = 'http://www.en.wikipedia.org/wiki/' + word
		wiki_source = self.wiki_clean(wiki_url)	
		print wiki_url

	def wiki_clean(self, url):
		response = urllib.urlopen(url)
		wiki_source = response.read()
		soup = BeautifulSoup(wiki_source)
		print soup.find('div',id="bodyContent").p

if __name__ == '__main__':
	Hintify('frog')
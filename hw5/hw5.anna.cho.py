import sys
import re
import urllib.request as something
import urllib.error as er
import string
from bs4 import BeautifulSoup

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################

# Your code goes here
def getSoup(url):
	"""Given a url, reads the page into a string and calls preprocess_yelp_page to preprocess the page before returning a parsable soup from BS4.
	"""
	# Source: starter code for hw4
	try: 
		#open url and get data
		response = something.urlopen(url)
		content = response.read()
		content = content.decode('utf-8')
		response.close()
	except:	# In case the url does not work
		print("The url is not functional: " + url)
		exit()
	else:
		content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
		soup = BeautifulSoup(content, 'html.parser')
		return soup

def getTop(soup):
	"""For a given webpage, returns the restaurant names and the number of reviews a given restaurant has.
	"""
	restaurant_dict = {}
	# Find a regular search result within the page.
	regular_result = soup.find_all('li', {"class" : "regular-search-result"})
	for li in regular_result:
		# Find the restaurant names within the page.
		# Used this page as a guide: http://stackoverflow.com/questions/16248723/how-to-find-spans-with-a-specific-class-containing-specific-text-using-beautiful
		a = li.find('a', {"class" : "biz-name js-analytics-click"})
		restaurant_name = a.get_text()
		# Find the review count within the page.
		span = li.find('span', {"class" : "review-count rating-qualifier"})
		review_count = span.get_text()
		# source: http://stackoverflow.com/questions/15340582/python-extract-pattern-matches
		review_count = re.match(r'^[0-9]+', review_count).group()
		review_count = int(review_count)
		# Add restaurants and their respective counts to the dictionary
		restaurant_dict[restaurant_name] = review_count
	return restaurant_dict		

def main():

	# Create a dictionary for all 4 pages of restaurants and their counts.
	total_dict = {}
	url_1 = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=0#'
	url_2 = 'https://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=10&sortby=rating'
	url_3 = 'https://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=20&sortby=rating'
	url_4 = 'https://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=30&sortby=rating'
	# print(getSoup(url_1))
	page_1 = getSoup(url_1)
	page_2 = getSoup(url_2)
	page_3 = getSoup(url_3)
	page_4 = getSoup(url_4)
	Top1 = getTop(page_1)
	Top2 = getTop(page_2)
	Top3 = getTop(page_3)
	Top4 = getTop(page_4)
	# source: http://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python
	for d in (Top1, Top2, Top3, Top4):
		total_dict.update(d)
	# Create a sorted list of restaurants by count.
	# source: http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
	# source: http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/
	sorted_list = sorted(total_dict, key=total_dict.__getitem__, reverse=True)
	# print(sorted_list)
	# Open a file to write the results
	with open('restaurants.anna.cho.txt', 'w') as f:
		for restaurant in sorted_list:
			f.write('{},{}\n'.format(restaurant, total_dict[restaurant]))

if __name__ == '__main__':
	main()




# import requests, bs4
import urllib.request as re
import urllib.error as er
from bs4 import BeautifulSoup

def main():
	# # Source: https://automatetheboringstuff.com/chapter11/
	# res = requests.get('http://www.gutenberg.org/browse/scores/top')
	# res.raise_for_status()
	# webpage = bs4.BeautifulSoup(res.text)
	# # print(webpage)
	# top100 = webpage.select('li') # list of Top 100 books

	# # get text and URL
	# for i in range(10):
	# 	title = top100[i].getText()
	# url = "http://www.dailykos.com/story/2013/04/27/1203495/-GunFAIL-XV"
	url = "http://www.gutenberg.org/browse/scores/top"

	page = re.urlopen(url).read()
	soup = BeautifulSoup(page)
	# print(soup)
	link = soup.select("ol > li > a")
	li = soup.select("ol > li")
	with open('catalog,txt', 'w') as f:
	# title1 = soup.li.getText()
		for index in range(9):
			book = li[index].getText()
			href = link[index].get('href')
			# print(soup.findNext("li").getText())
			# print(soup.findNext("ol > li > a"))
			f.write('{},http://www.gutenberg.org/browse/scores/top{}\n'.format(book, href))
	

if __name__ == '__main__':
	main()
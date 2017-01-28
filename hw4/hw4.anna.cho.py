import urllib.request as re
import urllib.error as er
import string

def ReadCatalog(catalog_file):
	""" Reads the Catalog file and creates the dictionary Books (Titles are keys, list of index and URL is value)
	and list of titles."""
	count = 0	# Index of book in catalog
	Books = {}	
	Titles = []
	with open(catalog_file, 'r') as f:
		lines = f.readlines(); 
		for book in lines:
			book = book.strip()
			url_index = book.rfind('http')
			if url_index == -1:	# If no URL
				url = ""
				title = book
			else:
				url = book[url_index:]
				title = book[:url_index - 1]
			if title not in Titles:	# Check if title is already in Titles in case there are duplicates listed in the catalog
				Titles.append(title)
				Books[title] = [count, url]	# Add book to Books dictionary
				count += 1 # Increment the index
	return Books, Titles

def ReadBook(url):
	"""Takes in a url, cleans the data by taking out punctuation and numbers and changing all letters to lowercase.
	"""
	try:
	# open url
		response = re.urlopen(url)
	# get data
		content = response.read()
		content = content.decode('utf-8')
	# close connection
		response.close()
	except:	# URL doesn't work
		content = ""	
		print("The url is not functional : " + url)
		return []	# If URL doesn't work, list of words is empty
	else:
		# Clean Data
		return filter_data(content)

def filter_data(text):
	"""Cleans data by taking out punctuation and numbers and changing all letters to lowercase."""
	list_of_words = text.split()
	# remove all non-alphabetical characters
	list_of_words = [''.join([char for char in word if char in string.ascii_letters]).lower() for word in list_of_words]
	# remove empty spaces
	list_of_words = [word for word in list_of_words if word.isalpha()]
	return list_of_words	

def UpdateWords(data, clean_text, length, book_index):
	"""Takes in a dictionary of word counts, cleaned text, number of books in the catalog, and current book's index. 
	Returns an updated word count dictionary for the book in question.
	"""
	total_words = len(clean_text)	# total number of words
	for idx in range(total_words):	
		word = clean_text[idx]
		# Check if word is already in data dictionary.
		if word not in data:
			# Add word to data with list with length equal to the number of books in the list
			count_list = [0] * length	# Create a new list of word counts.
			count_list[book_index] += 1	# Increment the count for the index of the book in question
			data[word] = count_list	# Update the dictionary of word counts.
		else:	# Word is already in dictionary
			data[word][book_index] += 1	# Increase word count at the correct index of the book.
	return data

def Search(Words, Books, Titles):
	"""Prints the counts of each word.
	Prints the catalog.
	Prints the titles.
	Terminates.
	"""

	user_input = input('Search term? ')
	length = len(Titles)	# Total number of books
	while user_input != '<terminate>':
		if user_input == '<terminate>':
			break;
		# If user inputs '<catalog>', the program prints the Books dictionary in order of book index.
		elif user_input == '<catalog>':
			for i in range(length): # For each book index
				for book in Books:	# Print the corresponding item in the Books dictionary.
					if Books[book][0] == i:
						print('{} : {}'.format(book, Books[book]))
			user_input = input('Search term? ')
		elif user_input == '<titles>':
			for i in range(length): # For each book index
				for book in Books:	# Print the corresponding item in the Books dictionary.
					if Books[book][0] == i:
						print(book)
			user_input = input('Search term? ')
		else:
			if user_input in Words:
				copy = list(Words[user_input]) # Create a copy of the word counts for the word
				count = 0;	# Count to keep track of how many books have been accounted for
				while count < length:
					maximum = max(copy)	# Find maximum and add print to console.
					for index in range(length):
						if copy[index] == maximum:
							count += 1
							print("{}. The word {} appears {} times in {} (link: {})".format(count, user_input, maximum, Titles[index], Books[Titles[index]][1]))
							copy[index] = -1
			else: # If input not in any of the books
				print("\"{}\" is not contained in these books.".format(user_input))
			user_input = input('Search term? ')

def main():

	data = {}
	try:
		Books, Titles = ReadCatalog('hw4localcatalog.txt')
	except:
		print("file not found")
	else:
		length = len(Titles)
		for book in Titles:
			book_index = Books[book][0]	
			url = Books[book][1]
			clean_text = ReadBook(url)
			data = UpdateWords(data, clean_text, length, book_index)
		Search(data, Books, Titles)

if __name__ == '__main__':
	main()
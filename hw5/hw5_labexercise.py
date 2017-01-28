import urllib.request as req
from bs4 import BeautifulSoup

url = 'http://www.ischool.berkeley.edu/people/students/mims/2018'

response = req.urlopen(url)
page_source = response.read()

soup = BeautifulSoup(page_source, 'html.parser')

images = soup.find_all('img', {'class': 'imagecache-profile-thumbnail'})

# len(images)

# for i, image in enumerate(images):
# 	source = image['src']
# 	address = 'http://www.ischool.berkeley.edu/' + source
# 	req.urlretrieve(address, filename=str(i)+'.jpg')

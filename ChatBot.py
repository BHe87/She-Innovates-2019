from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import requests
from unidecode import unidecode

data = []

def talk():
	


	
def scrape():
	page = requests.get("https://en.wikipedia.org/wiki/Watermelon")
	#print(page.status_code)
	soup = BeautifulSoup(page.content, 'html.parser')
	#u = unidecode(soup)
	#print(soup.prettify())
	#print(list(soup.children))
	#types = [type(item) for item in list(soup.children)]
	#print(types)
	#html = list(soup.children)[2]
	#print(list(html.children))
	#body = list(html.children)[3]
	#print(body)
	#print(list(body.children))
	#p = list(body.children)[1]
	for text in soup.find_all('p'):
		data.append(text.get_text())


def main():
	scrape()
	talk()
	print(data)

if __name__ == '__main__':
	main()
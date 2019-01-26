from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import requests
from unidecode import unidecode
import re
from flask import Flask

def talk(data):
	user_input = input('What do you want to know? ')
	
	for p in data:
		blob = TextBlob(p)
		for sentence in blob.sentences:
			if user_input in sentence:
				print(sentence)
				return
			#print(sentence)

def remove_parentheses(data): 
	cleaned = []
	for p in data:
		cleaned.append(re.sub(r'\([^()]*\)', "", p))

	cleaned2 = []
	for x in cleaned:
		cleaned2.append(re.sub(r'\([^()]*\)', "", x))

	return cleaned2


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
	site_text = []
	for text in soup.find_all('p'):
		site_text.append(text.get_text())

	return site_text

def main():
	site_text = scrape()
	cleaned = remove_parentheses(site_text)
	talk(cleaned)
	#print(data)

if __name__ == '__main__':
	main()
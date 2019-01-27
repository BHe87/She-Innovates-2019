from flask import render_template, redirect, url_for, request
from app import app
from bs4 import BeautifulSoup
from textblob import TextBlob
from unidecode import unidecode
import requests
import re

site_text = []

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/topic', methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		topic = request.form['topic']
		return redirect(url_for('success', name=topic))
	

@app.route('/success/<name>')
def success(name):
	page = requests.get("https://en.wikipedia.org/wiki/%s" % name)
	soup = BeautifulSoup(page.content, 'html.parser')
	for text in soup.find_all('p'):
	 	site_text.append(text.get_text())		
	data = remove_parentheses(site_text)
	return redirect(url_for('part2', topic=name, wiki=page))


@app.route('/part2/<topic>/<wiki>')
def part2(topic):
	return render_template('part2.html', topic=topic)


@app.route('/question', methods = ['POST', 'GET'])
def respond():
	if request.method == 'POST':
		question = request.form['question']
		#return 'Question: %s' % question
		response = get_response(question)
		return render_template('part2.html', response=response)


def get_response(question):
	parsed = TextBlob(question)
	noun, adjective, verb = find_parts_of_speech(parsed)
	return '%s %s %s' % (noun, adjective, verb)


def find_parts_of_speech(sentence):
	noun = find_noun(sentence)
	adjective = find_adjective(sentence)
	verb = find_verb(sentence)
	return noun, adjective, verb


def find_noun(sentence):
	noun = ''

	for word, part_of_speech in sentence.pos_tags:
		if part_of_speech == 'NN' or part_of_speech == 'NNS' or part_of_speech == 'NNP' or part_of_speech == 'NNPS':
			noun = word

	return noun


def find_adjective(sentence):
	adjective = ''

	for word, part_of_speech in sentence.pos_tags:
		if part_of_speech == 'JJ' or part_of_speech == 'JJR' or part_of_speech == 'JJS':
			adjective = word

	return adjective


def find_verb(sentence):
	verb = ''

	for word, part_of_speech in sentence.pos_tags:
		if part_of_speech == 'VB' or part_of_speech == 'VBD' or part_of_speech == 'VBG' or part_of_speech == 'VBN' or part_of_speech == 'VBP' or part_of_speech == 'VBZ':   
			verb = word

	return verb


def remove_parentheses(data): 
	cleaned = []
	for p in data:
		cleaned.append(re.sub(r'\([^()]*\)', "", p))

	cleaned2 = []
	for x in cleaned:
		cleaned2.append(re.sub(r'\([^()]*\)', "", x))

	return cleaned2
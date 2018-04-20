import requests
import sys
import time, random

def start():
	print 'I will not be responsible for what you do in this tool'
	url = raw_input('what you want to search in onion link ? ')
	nipe = 'http://onion.link'
	gud = requests.post(url, data={'search':url, 'gsc-search-button gsc-search-button-v2':'submit'})
	for response in gud:
		print response

if __name__ == '__main__':
	start()
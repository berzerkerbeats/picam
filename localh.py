import requests

def do_Post():
	requests.post('localhost:8080/post', data={'key':'value'})


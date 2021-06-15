import requests

def do_Post():
	requests.post('http://localhost:8080/api/post', data={'key':'value'})


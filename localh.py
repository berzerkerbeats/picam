import requests

def do_Post():
	requests.post('http://192.168.0.2:8080/api/post', data={'key':'value'})


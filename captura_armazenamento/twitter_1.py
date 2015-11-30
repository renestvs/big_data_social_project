import json
from requests_oauthlib import OAuth1Session

key = "vLpy9MINtMXlSl0hl75OoR0BD"
secret = "JmSLl7HsbhJ6XBqSS5i7q7EBeYoqOjMZJ1MFkcFmU2QpG4OiqE"
token = "1076380759-3WjYgXIIc38QqaVRii1kQBDGxJcZfF9OYkc6nqC"
token_secret = "AJv6rphbI10fSpclZoOI6qIwmph4AfqH75YAtScWehSWR"

requests = OAuth1Session(key, secret, token, token_secret)
r = requests.post('https://stream.twitter.com/1/statuses/filter.json',
	data={'track': ['transito','engarrafamento']},
	stream=True)

for line in r.iter_lines():
	if line:
		try:
			print json.loads(line) # tweet retornado
		except:
			"Ocorreu um erro."

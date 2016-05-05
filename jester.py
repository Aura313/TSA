import requests
import json
from textblob import TextBlob
# from spacy.en import English

url = 'http://localhost:9200/tweets-new/main/_search'
data = {"query":{"match_all":{}}}
res = requests.post(url, json.dumps(data))
# nlp = English()

t = json.loads(res.content)

for tw in t[u'hits'][u'hits']:
	# print tw
	txt = tw[u'_source'][u'text']
	# txtp = nlp(txt)
	print txt
	print TextBlob(txt).sentiment
	raw_input()


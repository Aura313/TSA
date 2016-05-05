from elasticsearch import Elasticsearch, helpers
from pprint import pprint
import requests
import json
import pickle

search_string = 'iphone'
query = { "query": {  "match": { "text": search_string  } } }

response = requests.post('http://localhost:9200/tweets/clustered/_search', json.dumps(query) )
response = json.loads(response.content)

# pprint(response[u"hits"][u"hits"])

results = []
for x in response[u"hits"][u"hits"]:

	polarity =  x["_source"][u'polarity']
	cluster =  x["_source"][u'cluster_id']
	results.append((polarity,cluster))


pprint(results)

from pprint import pprint
import requests
import json


article = 'android'

url = 'http://conceptnet5.media.mit.edu/data/5.4/c/en/%s' % article
res =  requests.get(url)
r = json.loads(res.content)

features = []
for edge in r['edges']:
	features.append(edge[u'features'])


final = []
for feat in features:
	print feat
	r = raw_input("Press Y to accept as a valid feature")
	if r.lower() == 'y':
		final.append(feat)

pprint(final)

import json
import tweet_reader
from elasticsearch import Elasticsearch, helpers
from pprint import pprint

es = Elasticsearch(hosts=['http://localhost:9200/'])

counter = 0
ts = tweet_reader.TweetStreamer()

for tweet in ts:
	counter += 1
	pprint(tweet)
	raw_input()
print counter

# helpers.bulk(es,ts)
from elasticsearch import Elasticsearch, helpers
import tweet_reader

es =  Elasticsearch(hosts=['http://localhost:9200/'])

ts = tweet_reader.TweetStreamer()

helpers.bulk(es,ts)

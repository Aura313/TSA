import requests
import ujson
from pprint import pprint
import traceback

class _elasticsearch(object):

	def __init__(self, table = "main"):
		self.table = table
	
	def __iter__(self):
		URL = "http://localhost:9200/tweets-new/%s/_search?scroll=2m&size=1000" % self.table
		# query = { "bool": { "must": [ { "match": { "tp" : False } }, { "match": { "nlp" : True } } ] } }
		query = { "match_all" : {} }
		data = ujson.dumps( { "query" : query} )

		scroll_id = None

		while True:
			try:
				# print URL
				# print data
				response = requests.post(URL, data)
				# pprint (response)
				response = ujson.loads(response.content)
			except Exception, e:
				print traceback.format_exc()
				break
			
			if scroll_id == None:
				URL = "http://localhost:9200/_search/scroll"
				scroll_id = response[u'_scroll_id']
				data = ujson.dumps({'scroll':"2m", "scroll_id": scroll_id})

			for document in response["hits"]["hits"]:
				yield (document)

			if len(response["hits"]["hits"]) <= 0 :
				#Clear the scroll API
				print "REACHED :D"
				try:
					requests.delete(URL,data=ujson.dumps( { "scroll_id": scroll_id } ))
					print "Deleting Stuff"
				except:
					continue
				break

# es = _elasticsearch()

# for tweet in es:
# 	pprint(tweet)
# 	raw_input()


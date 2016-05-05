from sklearn.cluster import KMeans
import numpy
import math
import features
from elasticsearch import Elasticsearch, helpers
import elasticsearch_reader
import tweet_reader
import pickle
import sys

#Some Macros
NUMBER_OF_CLUSTERS = 3

# tweets = [
# 			'Tanya has really great boobs',
# 			' Priyansh cannot be more dumb',
# 			'Tanya REGularly fucks Neelu',
# 			'Tanya is short',
# 			'So is this sent',
# 			'Is this the real life',
# 			'is ths fntsy',
# 			'cot in da landslyde',
# 			'no esc frm reality',
# 			'these are some really big ass sentences',
# 			'just so that the classifier gets good data',
# 			'and can distinguish between small and big sentences'
# 		]

kmean = KMeans(n_clusters = NUMBER_OF_CLUSTERS)
tweet_stream = tweet_reader.TweetStreamer()
es = elasticsearch_reader._elasticsearch()
es_client = Elasticsearch(hosts = 'http://localhost:9200/')


def train_kmean():

	global kmean
	counter = 0

	feature_list = []
	for tweet in es:
		feature_values = features.feature_transform(tweet)
		# print feature_values
		if feature_values == -1:
			continue
		feature_list.append(feature_values)
		counter += 1
		print counter
		# print feature_list[-1]


	feature_list = numpy.array(feature_list)


	#Stamping out a Kmeans object
	kmean.fit(feature_list)
	f = open('kmean.dat','w+')
	pickle.dump(kmean,f)
	f.close()

	# sys.exit(0)
	#Again, fetch all tweets and label them.
	es_new = elasticsearch_reader._elasticsearch()
	counter = 0
	tweets = []

	centroids = kmean.cluster_centers_
	centroids = list([list(x) for x in centroids])

	print "About to push tweets now"
	for tweet in es_new:
		cluster_id = int(kmean.labels_[counter])
		feature_values = list(feature_list[counter])

		diff = 0
		for i in range(len(feature_values)):
			diff += abs(math.pow( centroids[cluster_id][i],2) - math.pow( feature_values[i],2 ) )
		#  diff
		# raw_input()
		diff = math.sqrt(diff)

		tweet["_type"] = 'clustered'
		tweet["_source"]["feature_values"] = feature_values
		tweet["_source"]["cluster_id"] = cluster_id
		tweet["_source"]["polarity"] = diff

		tweets.append(tweet)
		if len(tweets) >= 1000:
			helpers.bulk(es_client, tweets)
			print "Pushing tweets", counter
			tweets = []

		counter += 1

train_kmean()

# #TESTING AREA
# a = 'short sentence'
# b = 'short SENTENCE '
# c = ' this is a really really really long sentence'
# d = ' THIS is a Long Seentece with CAPS'


# print kmean.predict(features.feature_transform(a)), a
# print kmean.predict(features.feature_transform(b)), b
# print kmean.predict(features.feature_transform(c)), c
# print kmean.predict(features.feature_transform(d)), d
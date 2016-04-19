from sklearn.cluster import KMeans
import numpy
import features

import tweet_reader

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


def train_kmean():

	global kmean

	feature_list = []
	for tweet in tweet_stream:
		feature_list.append( features.feature_transform(tweet) )

	feature_list = numpy.array(feature_list)


	#Stamping out a Kmeans object
	kmean.fit(feature_list)

train_kmean()

#TESTING AREA
a = 'short sentence'
b = 'short SENTENCE '
c = ' this is a really really really long sentence'
d = ' THIS is a Long Seentece with CAPS'


print kmean.predict(features.feature_transform(a)), a
print kmean.predict(features.feature_transform(b)), b
print kmean.predict(features.feature_transform(c)), c
print kmean.predict(features.feature_transform(d)), d
from sklearn.cluster import KMeans
import numpy
import features

#Some Macros
NUMBER_OF_CLUSTERS = 3
def train_kmean():

	feature_list = []
	for x in range(10):
		feature_list.append( features.feature_transform("Priyansh is stupid.") )

	feature_list = numpy.array(feature_list)


	#Stamping out a Kmeans object
	kmean = KMeans(n_clusters = NUMBER_OF_CLUSTERS)
	kmean.fit(feature_list)

a = [1,3,6,3,7,4,6,3,7,8]
print kmean.predict(a)
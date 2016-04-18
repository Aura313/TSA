import random
import string


def _feature_length_of_data_node(data_node):
	return len(data_node)

def _feature_number_of_cap_letters(data_node):
	counter = 0
	for letter in data_node:
		if letter in string.uppercase:
			counter += 1

	return counter

def feature_transform(data_node):
	# a = []
	# for x in range(0,10):
	# 	a.append(random.randint(0,8))
	# return a

	#Declare an empty array of features that we'll be computing for our data node
	feature_list = []

	#Call the feature that we've created up there
	feature_length_of_data_node = _feature_length_of_data_node(data_node)
	feature_number_of_cap_letters = _feature_number_of_cap_letters(data_node)


	feature_list.append(feature_length_of_data_node)
	feature_list.append(feature_number_of_cap_letters)

	#Return this feature list
	return feature_list

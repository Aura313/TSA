import random


def _feature_length_of_data_node(data_node):
	return len(data_node)

def feature_transform(data_node):
	a = []
	for x in range(0,10):
		a.append(random.randint(0,8))
	return a



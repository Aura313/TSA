import random
import string

positive_emoticions = [ ':)',':P',';)',':)',';-)',':-)','=)',':D','XD', '=D','=]','D:',';D',':]']
negative_emoticons = [ ':(', ':-(', ':/', ':o', '=/','=(']
good_words = ['win', 'yay', 'wow']
bad_words = ['no' , 'sad']

def _feature_number_of_tokens(data_node):
	return len(data_node)

#NER (think how can we use it)

#NER for sentiment analysis

# def _feature_number_of_cap_letters(data_node):
# 	counter = 0
# 	for letter in data_node:
# 		if letter in string.uppercase:
# 			counter += 1

# 	return counter

def _feature_number_of_good_words(data_node):

	words = data_node.split()
	counter = 0
	for word in words:
		if word in good_words:
			counter +=1

	return counter	



def _feature_number_of_bad_words(data_node):
	words = data_node.split()
	counter = 0
	for word in words:
		if word in bad_words:
			counter += 1

	return counter


def _feature_has_link(data_node):
	#Split
	# words = data_node.split()
	pass

#Overall positive polarity
def _feature_has_overall_positive_polarity(data_node):
	pass

#Overall negative polarity
def _feature_has_overall_negative_polarity(data_node):
	pass

#HasHashtags
def _feature_has_hashtags(data_node):
	#Split
	words = data_node.split()

	for word in words:
		if word[0] in ['#',u'#']:
			return 1
			# TESTING
			print "HasHashtags"

	return 0

#Number of Positive emoticon
def _feature_number_of_positive_emoticons(data_node):
	#Divide the string into words
	words = data_node.split()
	counter = 0
	for word in words:
		if word in positive_emoticions:
			counter += 1
			# TESTING
			print "positive_emoticion"
	return counter	

#Number of negative emoticon
def _feature_number_of_negative_emoticons(data_node):
	
	words = data_node.split()
	counter = 0
	for word in words:
		if word in negative_emoticons:
			counter += 1
			# TESTING
			print "negative_emoticon"
	return counter

def feature_transform(data_node):
	# a = []
	# for x in range(0,10):
	# 	a.append(random.randint(0,8))
	# return a

	#Declare an empty array of features that we'll be computing for our data node
	feature_list = []

	#Call the feature that we've created up there
	feature_number_of_tokens = _feature_number_of_tokens(data_node)
	# feature_number_of_cap_letters = _feature_number_of_cap_letters(data_node)
	feature_number_of_positive_emoticons = _feature_number_of_positive_emoticons(data_node)


	feature_list.append(feature_number_of_tokens)
	# feature_list.append(feature_number_of_cap_letters)
	feature_list.append(feature_number_of_positive_emoticons)

	#Return this feature list
	return feature_list

# ----------------------------------------- TESTING SHIZ -------------------------------------------

# print _feature_number_of_positive_emoticons("I think barca is going to win this time! :) #barca #football")
print _feature_has_hashtags("No,I don't think barca is going to win this time! :( #barca #football #sad")
# print _feature_number_of_negative_emoticons("No, we can't lose this world to trump. :( :/")
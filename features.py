from spacy.en import English
import random
import string
import re

nlp = English()

positive_emoticons = [':)',':P',';)',':)',';-)',':-)','=)',':D','XD', '=D','=]','D:',';D',':]']
negative_emoticons = [ ':(', ':-(', ':/', ':o', '=/','=(',":'-("]
good_words = ['win', 'yay', 'wow']
bad_words = ['no' , 'sad']

URL_REGEX = u'''((?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?]))'''
EMOTICON_REGEX = '''[:=;8X]'?-?[\)\/\(\?DPpo\]]'''
HASHTAG_REGEX = '''\#[^\ ]*'''



def _feature_number_of_tokens(data_node):
	# return len(data_node)
	data_node_processed = nlp(data_node)
	return len(data_node_processed)

def _feature_has_entities(data_node):
	data_node_processed = nlp(data_node)
	for token in data_node_processed:
		if not token.ent_type == 0:
			return 1
	return 0

#NER (think how can we use it)

#NER for sentiment analysis

# def _feature_number_of_cap_letters(data_node):
# 	counter = 0
# 	for letter in data_node:
# 		if letter in string.uppercase:
# 			counter += 1

# 	return counter

#GoooWords
def _feature_number_of_good_words(data_node):

	words = data_node.split()
	counter = 0
	for word in words:
		if word in good_words:
			counter +=1

	return counter	

#BadWords

def _feature_number_of_bad_words(data_node):
	words = data_node.split()
	counter = 0
	for word in words:
		if word in bad_words:
			counter += 1

	return counter

#HasLink
def _feature_has_link(data_node):
	for regex_match in re.findall(URL_REGEX, data_node):
		#Regex match now contains those highlighted things that you saw on the regexr.com page (snippets of strings)
		print regex_match
		return 1
	return 0

#Overall positive polarity
def _feature_has_overall_positive_polarity(data_node):
	pass
		#sentlex

#Overall negative polarity
def _feature_has_overall_negative_polarity(data_node):
	pass
	#sentlex

#HasSlang

def _feature_has_slangs(data_node):
	pass


#HasHashtags
def _feature_has_hashtags(data_node):
	#Split
	words = data_node.split()

	for word in words:
		if word[0] in ['#',u'#']:
			return 1

	return 0

#Number of Hashtags
def _feature_number_of_hashtags(data_node):
	return len(re.findall(HASHTAG_REGEX,data_node))



#Number of Positive emoticon
def _feature_number_of_positive_emoticons(data_node):
	#Divide the string into words
	words = data_node.split()
	counter = 0
	# for word in words:
	# 	if word in re.findall(positive_emoticions, data_node):
	# 		counter += 1
	# 		# TESTING
	# 		print "positive_emoticion"
	# return counter

	# counter = 0
	regex_pattern = "[:=;8X]'?-?[\)\/\(\?DPpo\]]"
	for regex_match in re.findall(EMOTICON_REGEX, data_node):
		#Regex match now contains those highlighted things that you saw on the regexr.com page (snippets of strings)
		if regex_match in positive_emoticons:
			#Assuming that our positive_emoticons is comprehensive
			counter += 1

		else:
			if regex_match not in negative_emoticons:
				print "We do not recognize this emoticon. Put it in either of these lists - ", regex_match

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

# print _feature_number_of_positive_emoticons("I think barca is going to win this time!:):):):):) :) :D #barca #football")
print _feature_has_hashtags("No,I don't think barca is going to win this time! :( #barca #football")
print  _feature_number_of_hashtags("No,I don't think barca is going to win this time! :( #barca #football")
# # print _feature_number_of_negative_emoticons("No, we can't lose this world to trump. :( :/")
# print _feature_has_link("Yaar ye website kitni faad hai http://google.com ")
# print _feature_has_link("Yaar ye pornsite kitni faad hai www.gaandfaad.com")
# print 
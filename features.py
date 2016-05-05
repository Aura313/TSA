from spacy.en import English
from textblob import TextBlob
from pprint import pprint
import random
import string
import re

nlp = English()

positive_emoticons = [':)',':P',';)',':)',';-)',':-)','=)',':D','XD', '=D','=]','D:',';D',':]','8)','XP']
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

def _feature_number_of_entities(data_node):
	data_node_processed = nlp(data_node)
	counter= 0
	for token in data_node_processed:
		if not token.ent_type == 0:
			counter += 1
	return counter


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
	text = nlp(data_node)
	counter = 0
	for token in text:
		s = TextBlob(token.text).sentiment
		if s[0] > 0:
			counter +=1
	return counter
	

#BadWords

def _feature_number_of_bad_words(data_node):
	text = nlp(data_node)
	counter = 0
	for token in text:
		s = TextBlob(token.text).sentiment
		if s[0] < 0:
			counter +=1
	return counter

def _feature_number_of_junk_words(data_node):
	text = nlp(data_node)
	counter = 0
	for token in text:
		s = TextBlob(token.text).sentiment
		if s[0] == 0:
			counter +=1
	return counter

#HasLink
def _feature_has_link(data_node):

	if len(data_node) == 0:
		return 0
	return 1

#Overall positive polarity
def _feature_has_overall_positive_polarity(data_node):
	if TextBlob(data_node).sentiment[0] > 0:
		return 1
	return 0
		#sentlex

#Overall negative polarity
def _feature_has_overall_negative_polarity(data_node):
	if TextBlob(data_node).sentiment[0] < 0:
		return 1
	return 0

#HasSlang
def _feature_has_slangs(data_node):
	pass

#HasRetweets
def _feature_has_retweets(data_node):
	return (data_node)
# def _feature_has_favourites(data_node):
# 	if len(data_node) == 0:
# 		return 0
# 	return 

def _feature_number_of_retweets(data_node):
	return (data_node)


def _feature_number_of_favourites(data_node):
	return (data_node)

def _feature_has_mentions(data_node):
	if len(data_node) == 0:
		return 0
	return 1

def _feature_number_of_mentions(data_node):
	return int(data_node)

def _feature_number_of_followers(data_node):
	return int(data_node)
	

def _feature_number_of_followings(data_node):
	return int(data_node)

def _feature_number_of_friends(data_node):
	return int(data_node)

# def _feature_screen_name(data_node):
# 	return int(data_node)

def _feature_number_of_statuses(data_node):
	return int(data_node)

def _feature_has_retweet(data_node):
	return int(data_node)

#HasHashtags
def _feature_has_hashtags(data_node):	
	if len(data_node) == 0:
		return 0
	return 1

#Number of Hashtags
def _feature_number_of_hashtags(data_node):
	# return len(re.findall(HASHTAG_REGEX,data_node))
	return len(data_node)

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
				# print "We do not recognize this emoticon. Put it in either of these lists - ", regex_match
				pass

	return counter


#Number of negative emoticon
def _feature_number_of_negative_emoticons(data_node):
	words = data_node.split()
	counter = 0
	regex_pattern = "[:=;8X]'?-?[\)\/\(\?DPpo\]]"
	for regex_match in re.findall(EMOTICON_REGEX, data_node):
		#Regex match now contains those highlighted things that you saw on the regexr.com page (snippets of strings)
		if regex_match in positive_emoticons:
			#Assuming that our positive_emoticons is comprehensive
			counter += 1

		else:
			if regex_match not in negative_emoticons:
				# print "We do not recognize this emoticon. Put it in either of these lists - ", regex_match
				pass
	return counter

def feature_transform(data_node):
	# a = []
	# for x in range(0,10):
	# 	a.append(random.randint(0,8))
	# return a

	#Declare an empty array of features that we'll be computing for our data node
	feature_list = []
	try:
		tweet_text = data_node['_source'][u'text']
	except:
		pprint(data_node["_id"])
		# raw_input()
		return -1

	tweet_url = data_node['_source'][u'entities'][u'urls']
	tweet_hashtags = data_node['_source'][u'entities'][u'hashtags']
	tweet_mentions = data_node['_source'][u'entities'][u'user_mentions']
	tweet_favourites = data_node['_source'][u'user'][u'favourites_count']
	tweet_statuses = data_node['_source'][u'user'][u'statuses_count']
	tweet_followings = data_node['_source'][u'user'][u'following']
	tweet_followers = data_node['_source'][u'user'][u'followers_count']
	tweet_friends = data_node['_source'][u'user'][u'friends_count']
	tweet_screen_name = data_node['_source'][u'user'][u'screen_name']
	tweet_retweet_count = data_node['_source'][u'retweet_count']
	tweet_has_retweets = data_node['_source'][u'retweeted']



	#Call the feature that we've created up there
	feature_number_of_tokens = _feature_number_of_tokens(tweet_text)
	feature_number_of_positive_emoticons = _feature_number_of_positive_emoticons(tweet_text)
	feature_number_of_negative_emoticons = _feature_number_of_negative_emoticons(tweet_text)
	feature_number_of_junk_words = _feature_number_of_junk_words(tweet_text)
	feature_number_of_good_words = _feature_number_of_good_words(tweet_text)
	feature_number_of_bad_words = _feature_number_of_bad_words(tweet_text)
	feature_has_entities = _feature_has_entities(tweet_text)
	feature_number_of_entities = _feature_number_of_entities(tweet_text)
	feature_has_overall_positive_polarity = _feature_has_overall_positive_polarity(tweet_text)
	feature_has_overall_negative_polarity = _feature_has_overall_negative_polarity(tweet_text)
	feature_has_hashtags = _feature_has_hashtags(tweet_hashtags)
	feature_has_link = _feature_has_link(tweet_url)
	

	# feature_has_mentions = _feature_has_mentions(tweet_mentions)
	# feature_has_retweets = _feature_has_retweets(tweet_retweet_count)
	# feature_screen_name = _feature_screen_name(tweet_screen_name)
	# feature_has_favourites = _feature_has_favourites(tweet_favourites)
	# feature_number_of_mentions = _feature_number_of_mentions(tweet_mentions)
	# feature_number_of_favourites = _feature_number_of_favourites(tweet_favourites)
	# feature_number_of_statuses = _feature_number_of_statuses(tweet_statuses)
	# feature_number_of_followings = _feature_number_of_followings(tweet_followings)
	# feature_number_of_followers = _feature_number_of_followers(tweet_followers)
	# feature_number_of_friends = _feature_number_of_friends(tweet_friends)
	# feature_number_of_retweets = _feature_number_of_retweets(tweet_retweet_count)


	feature_list.append(feature_number_of_tokens)
	feature_list.append(feature_number_of_positive_emoticons)
	feature_list.append(feature_number_of_negative_emoticons)
	feature_list.append(feature_number_of_junk_words)
	feature_list.append(feature_number_of_good_words)
	feature_list.append(feature_number_of_bad_words)
	feature_list.append(feature_has_entities)
	feature_list.append(feature_number_of_entities)
	feature_list.append(feature_has_hashtags)
	feature_list.append(feature_has_link)
	# feature_list.append(feature_has_overall_negative_polarity)
	# feature_list.append(feature_has_hashtags)
	# feature_list.append(feature_number_of__words)
	# # feature_list.append(feature_has_hashtags)
	# feature_list.append(feature_has_mentions)
	# feature_list.append(feature_has_favourites)
	# feature_list.append(feature_number_of_mentions)
	# feature_list.append(feature_number_of_favourites)
	# feature_list.append(feature_number_of_statuses)
	# feature_list.append(feature_number_of_followings)
	# feature_list.append(feature_number_of_followers)
	# feature_list.append(feature_number_of_friends)
	# feature_list.append(feature_has_retweets)
	# feature_list.append(feature_screen_name)
	# feature_list.append(feature_number_of_retweets)
	#Return this feature list
	return feature_list

# ----------------------------------------- TESTING SHIZ -------------------------------------------

# print _feature_number_of_positive_emoticons("I think barca is going to win this time!:):):):):) :) :D #barca #football")
# print _feature_has_hashtags("No,I don't think barca is going to win this time! :( #barca #football")
# print  _feature_number_of_hashtags("No,I don't think barca is going to win this time! :( #barca #football")
# print _feature_number_of_negative_emoticons("No, we can't lose this world to trump. :( :/")
# print _feature_has_link("Yaar ye website kitni faad hai http://google.com ")
# print _feature_has_link("Yaar ye pornsite kitni faad hai www.gaandfaad.com")
# print 
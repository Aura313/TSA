import json
import os

OUTPUT_FOLDER = '../newOutput/'
INDEX_NAME = "tweets-new"
TYPE_NAME = "main"

class TweetStreamer:
	def __init__(self):
		#List all files in domain
		self.file_list = os.listdir(OUTPUT_FOLDER)
		self.counter = 0

	def __iter__(self):

		for file_name in self.file_list:
			file_obj = open(OUTPUT_FOLDER+file_name)
			print file_name
			for line in file_obj:
				try:
					tweet = json.loads(line)
					op_dict = {
				            "_index": INDEX_NAME, 
				            "_type": TYPE_NAME, 
				            "_id": self.counter,
				            "_source": tweet
					    }
					self.counter += 1
					yield op_dict
				except:
					continue


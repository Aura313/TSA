import json
import os

OUTPUT_FOLDER = '../output/'

class TweetStreamer:
	def __init__(self):
		#List all files in domain
		self.file_list = os.listdir(OUTPUT_FOLDER)

	def __iter__(self):

		for file_name in self.file_list:
			file_obj = open(OUTPUT_FOLDER+file_name)
			for line in file_obj:
				try:
					tweet = json.loads(line)
					yield tweet
				except:
					continue
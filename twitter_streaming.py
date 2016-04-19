#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3254617124-DBtCVka9aT50lQ5Q8AhuMh0sqKYT5igEDZHEAeG"
access_token_secret = "Om8N1KnGLVYFL65ktGV0PUwB7jDK95eVDcaQ2Jr4IGSqp"
consumer_key = "NvSFVD0rGKsS5l4gLH3ZbZehF"
consumer_secret = "PE1HvGC8q61IKJdslhfmZr6Pm531fh5ofakZ0oqbBB8BSULdGf"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self):
        self.filename = 'output'
        self.counter = 0
        self.file_counter = 0
        self.file_obj = open(self.filename,'w+')

    def on_data(self, data):
        #store in file
        self.file_obj.write(data)

        self.counter += 1
        if self.counter >= 50:
            self.file_counter += 1
            self.file_obj.close()
            print "NEW FILE OPENED"
            self.file_obj = open(self.filename + str(self.file_counter),'w+')
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler("NvSFVD0rGKsS5l4gLH3ZbZehF", "PE1HvGC8q61IKJdslhfmZr6Pm531fh5ofakZ0oqbBB8BSULdGf")
    auth.set_access_token("3254617124-DBtCVka9aT50lQ5Q8AhuMh0sqKYT5igEDZHEAeG", "Om8N1KnGLVYFL65ktGV0PUwB7jDK95eVDcaQ2Jr4IGSqp" )
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
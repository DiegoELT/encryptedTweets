import keys
import encrypt
from twython import Twython
from dotenv import load_dotenv
import os

testfile = "test.pem"
keys.create_private_key_file(testfile)

message = input("Message: ")

private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

encrypted = encrypt.encrypt_with_key(public_key, message)

load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

print("Messaged cyphered succesfully")

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def del_all(twitter):
    while True:
        timeline = twitter.get_user_timeline(count=200)
        if len(timeline) == 0:
            print("No tweets left to delete")
            break

	#delete the timeline
        for tweet in timeline:
            status = int(tweet['id_str'])
            twitter.destroy_status(id=status)
            print('Tweet deleted: ' + str(status))
            print(len(timeline))


del_all(twitter)

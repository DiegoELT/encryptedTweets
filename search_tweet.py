import keys
import encrypt
from twython import Twython
from dotenv import load_dotenv
import os

testfile = "test.pem"
keys.create_private_key_file(testfile)


private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')


print("Messaged cyphered succesfully")

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


tweets = twitter.search(q='python', result_type='popular')

print(tweets["statuses"][0]["text"])



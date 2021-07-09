import keys
import encrypt
from dotenv import load_dotenv
import os
from twython import Twython
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

testfile = "test.pem"


private_key = keys.read_private_key(testfile)

with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
            )

load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print('Keys recovered succesfully')

##########################

timeline = twitter.get_user_timeline(screen_name='fakest_ever',
        count=1, tweet_mode='extended')

print('Timeline recovered')

ourtweet = timeline[0]['full_text']
#decoded = bytearray(ourtweet)

ourtweet = ourtweet.replace('&gt;','>')
ourtweet = ourtweet.replace('&lt;','<')
ourtweet = ourtweet.replace('amp;','')

ourtweet = ourtweet.replace('á','@')
ourtweet = ourtweet.replace('é','#')
ourtweet = ourtweet.replace('ó','.')


print('Lastest tweet recovered')

decoded = base64.b85decode(ourtweet)
print("decrypted tweet: ", encrypt.decrypt_with_key(private_key, decoded))


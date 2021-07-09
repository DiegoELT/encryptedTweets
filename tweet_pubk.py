import keys
import encrypt
from dotenv import load_dotenv
import os
from twython import Twython
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

testfile = "test.pem"


keys.create_private_key_file(testfile)

private_key = keys.read_private_key(testfile)

public_key = keys.get_public_from_private(private_key)

pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)

with open('public_key.pem', 'wb') as f:
    f.write(pem)

print('Keys generated')

#########################

load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print('Keys recovered succesfully')


##########################
pubfile = open('public_key.pem','r+')
arr = pubfile.readlines()
arr = arr[1:-1]
pubkey = ''.join(arr)

twitter.update_status(status=pubkey)
print("Tweet posted")

##########################

timeline = twitter.get_user_timeline(screen_name='fakest_ever',
        count=1, tweet_mode='extended')

print('Timeline recovered')

ourtweet = timeline[0]['full_text']

ourtweet = ourtweet.replace('&gt;','>')
ourtweet = ourtweet.replace('&lt;','<')
ourtweet = ourtweet.replace('amp;','')


print('Public key recovered')

with open('recovered_public_key.pem', 'w') as f:
    f.write('-----BEGIN PUBLIC KEY-----\n')
    f.write(ourtweet)
    f.write('\n-----END PUBLIC KEY-----')

print('public key saved as recovered_public_key.pem')


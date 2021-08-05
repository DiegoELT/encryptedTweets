import keys
import encrypt
from dotenv import load_dotenv
import os
from twython import Twython
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def recover_tweets():
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
        count=5, tweet_mode='extended')

    print('Timeline recovered successfully')


    enc = []
    for i in range(5):
        ourtweet = timeline[i]['full_text']

        ourtweet = ourtweet.replace('&gt;','>')
        ourtweet = ourtweet.replace('&lt;','<')
        ourtweet = ourtweet.replace('amp;','')

        ourtweet = ourtweet.replace('á','@')
        ourtweet = ourtweet.replace('é','#')
        ourtweet = ourtweet.replace('ó','.')
        enc.append(ourtweet)


    print('Lastest 5 tweets recovered')


    dec = []
    for i in range(5):
        decoded = base64.b85decode(enc[i])
        decoded = encrypt.decrypt_with_key(private_key, decoded)
        dec.append(decoded)
    

    all_tweets = (zip(enc,dec))

    print(all_tweets)

    return render_template('recover_tweets.html', data=all_tweets)


app.run(host='localhost', port='5000')

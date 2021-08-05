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

@app.route('/')
def box():
    return render_template('send_tweet.html')

@app.route('/', methods=['POST', 'GET'])
def send_tweet():
    if request.method == 'POST':
        print('Starting process...')

        testfile = "test.pem"

        message = request.form['tweet']

        private_key = keys.read_private_key(testfile)

        with open("public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

        encrypted = encrypt.encrypt_with_key(public_key, message) # Currently only working until 158 characters per message

        print("Messaged cyphered succesfully")

#########################

        load_dotenv()

        APP_KEY = os.getenv('APP_KEY')
        APP_SECRET = os.getenv('APP_SECRET')
        OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
        OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        print('Keys recovered succesfully')

        encoded = base64.b85encode(encrypted)

##########################

        repl = str(encoded).replace('@','á')
        repl = repl.replace('#','é')
        repl = repl.replace('.','ó')
        repl = repl[2:-1]

        twitter.update_status(status=repl)
        print("Tweet posted")
    
    return render_template('send_tweet.html', data=repl)

app.run(host='localhost', port=5000)

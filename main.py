import keys
import encrypt
from dotenv import load_dotenv
import os
from twython import Twython
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from flask import Flask, request, render_template

testfile = "test.pem"

#message = "Test Message"
#message = input()


#################################

app = Flask(__name__)

@app.route('/')
def box():
    return render_template('box.html')

@app.route('/post_tweet', methods=['POST'])
def post_tweet():
    text = request.form['tweet']
    message = text
    return message

app.run(host='localhost', port=5000)

##################################


#keys.create_private_key_file(testfile)

private_key = keys.read_private_key(testfile)

'''
public_key = keys.get_public_from_private(private_key)

pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)

with open('public_key.pem', 'wb') as f:
    f.write(pem)
'''

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
'''
pubfile = open('public_key.pem','r+')
arr = pubfile.readlines()
arr = arr[1:-1]
pubkey = ''.join(arr)

'''
repl = str(encoded).replace('@','á')
repl = repl.replace('#','é')
repl = repl.replace('.','ó')
repl = repl[2:-1]

twitter.update_status(status=repl)
print("Tweet posted")

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

'''
with open('recovered_public_key.pem', 'w') as f:
    f.write('-----BEGIN PUBLIC KEY-----\n')
    f.write(ourtweet)
    f.write('\n-----END PUBLIC KEY-----')
'''

decoded = base64.b85decode(ourtweet)
print("decrypted tweet: ", encrypt.decrypt_with_key(private_key, decoded))


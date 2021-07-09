import keys
import encrypt
from dotenv import load_dotenv
import os
from twython import Twython
import base64

testfile = "test.pem"
keys.create_private_key_file(testfile)

message = "Test Message"

private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

encrypted = encrypt.encrypt_with_key(public_key, message) # Currently only working until 158 characters per message

load_dotenv()

APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')


print("Messaged cyphered succesfully")

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

encoded = base64.b85encode(encrypted)
test = base64.b85decode(encoded)

twitter.update_status(status=encoded)

print("Tweet posted")

print("encrypted tweet: ", encrypted.hex())

print("decrypted tweet: ", encrypt.decrypt_with_key(private_key, encrypted))

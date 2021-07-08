import keys
import encrypt
from twython import Twython

testfile = "test.pem"
keys.create_private_key_file(testfile)

message = input("Message: ")

private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

encrypted = encrypt.encrypt_with_key(public_key, message)


APP_KEY = 'm4PEvpmaa7oGkVImobkLoPTki'
APP_SECRET = 'sgT3CBoGEQd04Upw9uB5bf3ho7fEOwPGgCVRPUNjdB5XW7YMij'
OAUTH_TOKEN = '1402056904818532352-kqjT9O6Gpyej3onhgnjbUdOH9urCCh'
OAUTH_TOKEN_SECRET = '9I0ICgiz9k4WMnNZx3WJwiJylfo9SGg9WnZzAtKHNutBF'

print("Messaged cyphered succesfully")

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.update_status(status='ekisde')#encrypted.hex())

print("Tweet posted")

print("encrypted tweet: ", encrypted.hex())

print("decrypted tweet: ", encrypt.decrypt_with_key(private_key, encrypted))

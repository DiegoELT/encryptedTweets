import keys
import encrypt
from twython import Twython

testfile = "test.pem"
keys.create_private_key_file(testfile)


private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)



APP_KEY = 'm4PEvpmaa7oGkVImobkLoPTki'
APP_SECRET = 'sgT3CBoGEQd04Upw9uB5bf3ho7fEOwPGgCVRPUNjdB5XW7YMij'
OAUTH_TOKEN = '1402056904818532352-kqjT9O6Gpyej3onhgnjbUdOH9urCCh'
OAUTH_TOKEN_SECRET = '9I0ICgiz9k4WMnNZx3WJwiJylfo9SGg9WnZzAtKHNutBF'

print("Messaged cyphered succesfully")

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


tweets = twitter.search(q='python', result_type='popular')

print(tweets["statuses"][0]["text"])



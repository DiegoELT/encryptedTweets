import keys
import encrypt
import base64

testfile = "test.pem"
keys.create_private_key_file(testfile)

message = "Test Message"

private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

encrypted = encrypt.encrypt_with_key(public_key, message) # Currently only working until 158 characters per message

encoded = base64.b85encode(encrypted)
test = base64.b85decode(encoded)

#owo = base64.b85encode(encrypted)
#print(g(str(hex1)))

print(encrypt.decrypt_with_key(private_key, test))
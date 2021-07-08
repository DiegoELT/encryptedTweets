import keys
import encrypt
import codecs

testfile = "test.pem"
keys.create_private_key_file(testfile)

message = "Test Message 1"
message2 = "Test Message 2"

private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

encrypted = encrypt.encrypt_with_key(public_key, message)
encrypted2 = encrypt.encrypt_with_key(public_key, message2)

print(len(encrypted))
print(len(encrypted2))

hex1 = encrypted.hex()

print(encrypt.decrypt_with_key(private_key, encrypted))
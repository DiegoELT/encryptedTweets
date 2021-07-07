import keys
import encrypt

testfile = "test.pem"
keys.create_private_key_file(testfile)

message = input("Message: ")

private_key = keys.read_private_key(testfile)
public_key = keys.get_public_from_private(private_key)

encrypted = encrypt.encrypt_with_key(public_key, message)

print("Messaged cyphered succesfully")

print(encrypt.decrypt_with_key(private_key, encrypted))
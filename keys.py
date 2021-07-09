# Importing the libraries that are needed for testing the Asymmetric Encryption
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def get_public_from_private (asymm_key):
    return asymm_key.public_key()

def create_private_key_file (filename): 
    private_key = rsa.generate_private_key (
        public_exponent = 65537, 
        key_size = 1790,
        backend = default_backend()
    )
    pem = private_key.private_bytes (
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(filename, 'wb') as file:
        file.write(pem)

def read_private_key (filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key
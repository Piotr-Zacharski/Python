from cryptography.fernet import Fernet

key = Fernet.generate_key()


def encrypt(message, key):
    return Fernet(key).encrypt(message)


def decrypt(message, key):
    return Fernet(key).decrypt(message)


# message = b"Na wakacje za rok pojedziemy do Szwajcarii!"
# encrypted_message = encrypt(message, key)
# print(encrypted_message)
# print(decrypt(encrypted_message, key))

with open('lorem.txt', 'rb') as file:
    data = file.read()

with open('encrypted_lorem.txt', 'wb') as file:
    file.write(encrypt(data, key))

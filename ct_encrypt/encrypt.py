import string
import random

global_key=[]
char=list(string.ascii_letters + string.digits + ' ')


# the thing about encryption and decryption is the ability to manipulte strings and keep strings...i mean cryptography i based on two things, which is a key-value pair
# in my case i use a key-vhar pai
class fernet():

    encrypted_message=''
    decrypted_message=''

    def generate_key():
        global global_key
        if not global_key:
           key=list(string.ascii_letters + string.digits +  ' ')
           random.shuffle(key)
           global_key.extend(key)


    def encrypt(message):
        fernet.generate_key()
        for words in message:
            index=char.index(words)
            fernet.encrypted_message += global_key[index]

        print(fernet.encrypted_message)


    def decrypt():
        for words in fernet.encrypted_message:
            index=global_key.index(words)
            fernet.decrypted_message+=char[index]

        print(fernet.decrypted_message)




from Crypto.Cipher import AES
from Crypto.Util import randpool
import base64, os, binascii

BLOCK_SIZE = 32
key_size = 32
PADDING = '0'
plaintext = 'secret data'
mode1 = AES.MODE_ECB
mode2 = AES.MODE_CBC

key_bytes = randpool.RandomPool(512).get_bytes(key_size)

pad = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE

data = plaintext + pad * chr(pad)

iv_bytes = randpool.RandomPool(512).get_bytes(BLOCK_SIZE)

encrypted_bytes = iv_bytes + AES.new(key_bytes, mode1, iv_bytes).encrypt(data)

#encrypted_string = base64.urlsafe_b64encode(str(encrypted_bytes))
#key_string = base64.urlsafe_b64encode(str(key_bytes))

#key_bytes2 = base64.urlsafe_b64decode(key_string)
#print '{} \n{}\n'.format(binascii.hexlify(key_bytes), binascii.hexlify(key_bytes2))

#encrypted_bytes2 = base64.urlsafe_b64decode(encrypted_string)
#print '{} \n{}\n'.format(binascii.hexlify(encrypted_bytes), binascii.hexlify(encrypted_bytes2))

#iv_bytes2 = encrypted_bytes2[:BLOCK_SIZE]
#print '{} \n{}\n'.format(binascii.hexlify(iv_bytes), binascii.hexlify(iv_bytes2))

#ncrypted_bytes2 = encrypted_bytes2[BLOCK_SIZE:]
#plain_text2 = AES.new(key_bytes2, mode1, iv_bytes2).decrypt(encrypted_bytes2)
#pad = ord(plain_text2[-1])
#plain_text2 = plain_text2[:-pad]

plain_text2 = AES.new(key_bytes, mode1, encrypted_bytes[BLOCK_SIZE:]).decrypt(encrypted_bytes[BLOCK_SIZE:])
pad = ord(plain_text2[-1])
plain_text2 = plain_text2[:-pad]

print '{} \n{}\n'.format(plaintext, plain_text2)

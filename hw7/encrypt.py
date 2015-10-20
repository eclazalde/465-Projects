from Crypto.Cipher import AES
from Crypto.Util import randpool
import base64, os, binascii

# Initial values
BLOCK_SIZE = 16
keySize = 32
PADDING = '0'
plaintext = ''
with open("plaintext.txt", "r") as myfile:
	plaintext = myfile.read()
modeECB = AES.MODE_ECB
modeCBC = AES.MODE_CBC
print 'Original Message:\n{}\n-----------\n'.format(plaintext)

# Vairables needed for the encrypt and decrypt
key = randpool.RandomPool(512).get_bytes(keySize)
pad = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
data = plaintext + pad * PADDING
iv = randpool.RandomPool(512).get_bytes(BLOCK_SIZE)

# Encrypt in ECB Mode
encryptedECB = AES.new(key, modeECB).encrypt(data)

# Decrypt in ECB Mode
plaintextECB = AES.new(key, modeECB).decrypt(encryptedECB)
plaintextECB = plaintextECB[:-pad]

# Print ECB results
print 'ECB Mode Ciphertext:\n{}\n'.format(binascii.hexlify(encryptedECB))
print 'Decoded Message:\n{}\n'.format(plaintextECB)

# Encrypt in CBC Mode
encryptedCBC = AES.new(key, modeCBC, iv).encrypt(data)

# Decrypt in CBC Mode
plaintextCBC = AES.new(key, modeCBC, iv).decrypt(encryptedCBC)
plaintextCBC = plaintextCBC[:-pad]

# Print CBC results
print 'CBC Mode Ciphertext:\n{}\n'.format(binascii.hexlify(encryptedCBC))
print 'Decoded Message:\n{}\n'.format(plaintextCBC)

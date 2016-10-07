from Crypto.Cipher import AES
import base64

encoded_text = ''
secret_key = ''

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
decoded = cipher.decrypt(base64.b64decode(encoded_text))
print decoded.strip()
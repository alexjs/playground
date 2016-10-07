from Crypto.Cipher import AES
import base64

msg_text = 'test some plain text here'.rjust(32)
secret_key = ''

cipher = AES.new(secret_key,AES.MODE_ECB)
encoded = base64.b64encode(cipher.encrypt(msg_text))
print encoded.strip()

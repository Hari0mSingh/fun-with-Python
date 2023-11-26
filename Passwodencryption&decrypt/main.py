#wap to encode and decode the password

import base64

password = input('Enter your password: ')

def encodeAndDecodePass(password):
    encoded_Pass = base64.b64encode(password.encode())
    print(f"encoded password is: {encoded_Pass}\n")
    decoded_pass = base64.b64decode(encoded_Pass.decode())
    print(f"decoded password is: {decoded_pass}")

encodeAndDecodePass(password)
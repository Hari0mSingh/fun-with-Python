import base64

data = b'Hello, World!'
encoded_data = base64.b64encode(data)
decoded_data = base64.b64decode(encoded_data)

print(f'Original Data: {data}')
print(f'Base64 Encoded: {encoded_data}')
print(f'Decoded Data: {decoded_data.decode()}')

import hashlib

def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

hash_pass = ''
input_pass = input('')
input_hash = my_hash(input_pass)

if hash_pass == input_hash:
    print('good')
else:
    print('bad')
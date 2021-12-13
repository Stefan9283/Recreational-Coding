import hashlib

f = open("in")
secret_key = f.read().strip('\n')

num = 1
while True:
    key = secret_key + str(num)
    hex = hashlib.md5(key.encode()).hexdigest()
    if hex.startswith('00000'):
    # if hex.startswith('000000'): # 6 zeros for the 2nd part
        print(num)
        break
    num += 1
    
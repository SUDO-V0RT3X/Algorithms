import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

length = int(input("Number of characters: "))
password = ''

for n in range(length):
    password += random.choice(chars)
    
print(password)

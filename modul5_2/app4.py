# encoding
import random

data = input('give string: ')
key = random.randint(129, 255)

result = ''
for letter in data:
    result += chr(ord(letter) ^ key)

print(result)

result1 = ''
for letter in result:
    result1 += chr(ord(letter) ^ key)

print(result1)
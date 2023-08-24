name = 'Emanuel'  # string
print(name)

age = 37  # int
print(age)
result = type(age)
print(result)

age = 37.0  # float
print(age)
result = type(age)
print(result)

age = 37 + 0j  # complex
print(age)
result = type(age)
print(result)

print('Methods of string: ', dir(name))

# name.
# age.
# print(type(37))


number1 = 5
number2 = number1
number2 = number1 + 1
print(number2)
print(number1)

print('Return from print: ', print(37))
result1 = input('Input data1 here: ')
print(result1)
result2 = input('Input data2 here: ')
print(result2)
# print(type(result))
print('Result of add str: ', result1 + result2)
print('Result of add int: ', int(result1) + int(result2))
# True = 3
print(True)
print(False)
print(type(True))
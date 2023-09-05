# first_number = int(input('give number:'))
#
# if first_number == 10:
#     print('number is 10')
# elif first_number == 11:
#     print('number is 11')
# else:
#     print('number is other')
#
# a = 10
# print(a)
# a = a + 1  # a += 1
# print(a)
# a += 1
# print(a)
#
# while a >= 10:
#     print(a)
#     a -= 2
#
# print('done')

# Example1

# n = 0
#
# while n < 10:
#     if n == 7:
#         n += 1
#         continue
#     elif n == 8:
#         break
#     print(n)
#     n += 1
#
# print('done')

# # Example2
#
# a = 'abcd'
# if a:
#     print('done')
#
# print(bool('abcd'))
# print(bool('d'))
# print(bool(''))
#
# print(bool(100))
# print(bool(-100))
# print(bool(0))
#
# print(bool(None), 'is value of None')
#
# if print('condition'):
#     print('failed')
# else:
#     print('success')
#
# print(bool(print))

# # Ex3
#
# print(True and True)
# print('x' and True)
# print(True and 'x')
# print(0 and True)
#
# a = True
# b = 'x'
#
# # and in Python
# if a:
#     print(b)
# else:
#     print(a)
#
#
# print(True or True)
# print('x' or True)
# print(True or 'x')
# print(0 or True)
#
# # find condition for 'or'


for letter in 'abcd':
    print(letter)

# for letter in 134:
#     print(letter)

print(range(10))
print(type(range(10)))

for number in range(2, 10): # number = range(10)[0]
    print(number)
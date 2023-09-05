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

n = 0

while n < 10:
    if n == 7:
        n += 1
        continue
    elif n == 8:
        break
    print(n)
    n += 1

print('done')
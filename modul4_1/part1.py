# result = 'a'
#
#
# def factorial(number):
#     global result
#     print('in function:', result)
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result
#     # return True
#     print('last print: ', result)  # this will never get executed
#
#
# returned_result = factorial(5)
# print('outside of function:', result)
# print(returned_result)

t1 = tuple('abc')
print(t1)
print(t1[0])
print(t1[0:2])

t2 = (1, 2, 3, 4)
print(t2)

a = 1
b = 2

a, b = b, a  # this works in python since right side is a tuple
print(a, b)

tuple_with_vars = (a, b)
print(tuple_with_vars[0], '->', tuple_with_vars[1])  # for exercise 3

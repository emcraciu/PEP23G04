result = 'a'


def factorial(number):
    global result
    print('in function:', result)
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
    # return True
    print('last print: ', result)  # this will never get executed


returned_result = factorial(5)
print('outside of function:', result)
print(returned_result)

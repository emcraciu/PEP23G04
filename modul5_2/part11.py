try:
    # x
    1/1
except (IndexError, ArithmeticError):
    print('we have division by 0')

except NameError:
    print('no variable')
else:
    print('division success in else')
# print('division success')
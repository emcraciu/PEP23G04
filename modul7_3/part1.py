# enumerate


my_list = ['a', 'b', 'c']
for index, element in enumerate(my_list):
    print(index + 1, element)


a, *b, c = 1, 2, 3, 4, 5, 6
print(b)
a, b, *c = 1, 2, 3, 4, 5, 6
print(c)


def test1(*args, **kwargs):
    print(args)
    print(kwargs)
# *(letter for letter in 'my_string')
test1(*(letter for letter in 'my_string'), **{'a':1, 'b':2})
# test1(a=1, b=2)


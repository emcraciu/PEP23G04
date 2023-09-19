# my_dict = {'test1': 1, 1: '1'}
# print(my_dict)
# print(id(my_dict))
#
# # Update dict
# my_dict.update({1.1: '1.1'})
# print(my_dict)
# print(id(my_dict))
#
# # print({my_dict: 'test2'}) # not hashable object as key
# print(my_dict.__hash__)  # objects without hash are not usable for dict keys
# print([1, 2, 3].__hash__)  # objects without hash are not usable for dict keys
#
# print('abcd'.__hash__())
# print('abcde'.__hash__())
#
# my_dict.update(one=1.1)
# print(my_dict)
#
#
# # Get keys , values and items
# my_keys = my_dict.keys()
# print(type(my_keys))
# print(my_keys)
#
# result1 = next(my_keys.__iter__())
# print(result1)
#
#
# my_values = my_dict.values()
# print(type(my_values))
# print(my_values)
#
# result1 = next(my_values.__iter__())
# print(result1)
#
#
# my_items = my_dict.items()
# print(type(my_items))
# print(my_items)
#
# result1 = next(my_items.__iter__())
# print(result1)
#
#
# for item in my_dict.items():
#     print(item)
#
# for key, value in my_dict.items():
#     print(key, value)

# Exceptions:
def divide(number1, number2):
    # if not number2:
    #     return 'infinit'
    result = 'infinit'
    try:
        print(abcd)
        result = number1/number2
    except ZeroDivisionError:
        print('something is wrong')
    except NameError:
        print('something else was wrong')
        result = 'could not calculate'
    return result

r = divide(1, 1)
print(r)
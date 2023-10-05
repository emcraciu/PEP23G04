# Exceptions Advanced
def test():
    return None

print('Functions will retun memory location when printed', test)


my_list = [1,2,3]

my_list_iterator = my_list.__iter__()
print(type(my_list_iterator))



print(my_list_iterator)
print(next(my_list_iterator))
print(next(my_list_iterator))
print(next(my_list_iterator))
# print(next(my_list_iterator))


for _ in my_list.__iter__():
    # raise StopIteration
    print('In for loop:', _)

# list comprehancion
my_new_list = [_ for _ in {1, 5, 9}]
print(my_new_list)

# generator
my_new_tuple = (_ for _ in {1, 5, 9})
print(my_new_tuple)
print(next(my_new_tuple))
print(next(my_new_tuple))
print(next(my_new_tuple))
# print(next(my_new_tuple))

for i in (_ for _ in {1, 5, 9}):
    print('In second for loop:', i)


# convert iterable object to list:
print([_.lower() for _ in 'exaMple' if _.upper() != 'E'])
print(list('exaMple'))
my_added_string = 'add me'
string1 = 'Hello World\n'
string2 = r'Hello World\n'
string3 = '''

Hello World

'''
string4 = f'Hello World {my_added_string}'
string5 = rf"\nHello World {my_added_string}"

print(string1, string2, string3, string4, string5, sep='\t')

string_with_quotes = 'my string \''
print(string_with_quotes)

# String methods
my_string = 'Hello World, {} {}'
my_string = my_string.format('Python', 'User')
print(my_string)

my_string = 'Hello World, {1} {0}'
my_string = my_string.format('Python', 'User')
print(my_string)

my_string = 'Hello World, {arg1} {arg2}'
my_string = my_string.format(arg1='Python', arg2='User', arg3='None')
print(my_string)


print(len(my_string))


print('___'.center(11, '#'))

my_string = 'Hello World'

print(my_string[0])

#'HelloWorld'
# 0123456789
# -10-9-8-7-6-5-4-3-2-1

# index
print(my_string[len(my_string) - 1])
print(my_string[-1])
print(my_string[-3])

# slice
print(my_string[0:3])
print(my_string[-5:-1])
print(my_string[-5:])
print(my_string[:-2])
print(my_string[:])

# step

print(my_string[0:7:1])
print(my_string[::-1])
print(my_string[::-2])



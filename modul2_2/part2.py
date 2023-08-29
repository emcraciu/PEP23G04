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

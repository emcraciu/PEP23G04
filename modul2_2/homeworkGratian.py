# 5
String = input('Introduceti un cuvant: ')
rev_str = reversed(String)
if list(String) == list(rev_str):
    print('True')
else:
    print('False')

# 6
my_string1 = 'Hello'
my_string2 = my_string1*4
print('Hello', 'Python.', sep='_', end='\n')
print(my_string2)

my_string3 = 'Ana'
my_string4 = my_string3*4
print('Ana', 'are', 'mere.', sep='_', end='\n')
print(my_string4)

my_string5 = 'Pizza'
my_string6 = my_string5*4
print('Pizza', 'Party.', sep='_', end='\n')
print(my_string6)

# 7
a = 5
b = 5
c = 'ana'
print('Locatia lui a este: ', id(a), type(a))
print('Locatia lui b este: ', id(b), type(b))
print('Locatia lui c este: ', id(c), type(c))
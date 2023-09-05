# Homework points: 5, 6, 7 from lab

# 5)

entered_word = input('Introduceti un cuvant: ')
print(entered_word[::-1] == entered_word[::])

# 6)

# 6.1)
print('Hello Python', 'Ana are mere', 'Pizza Party', sep='_')

# 6.2)
print('Hello Python', 'Ana are mere', 'Pizza Party', sep='.')

# 6.3)

str1 = 'Hello Python'
# 01234
str2 = 'Ana are mere'
str3 = 'Pizza Party'

print(str1, str2, str3, sep=4 * str1[0:5])  # interval inchis la stanga si deschis la dreapta

# 7)

a = 5.
b = 5
c = 'ana'

print('Locatia lui a este: ', str(id(a)), 'Locatia lui b este: ', str(id(b)), 'Locatia lui c este: ', str(id(c)))
print('Tipul variabilei a este: ', str(type(a)), 'Tipul variabilei b este: ', str(type(b)), 'Tipul variabilei c este: ',
      str(type(c)))

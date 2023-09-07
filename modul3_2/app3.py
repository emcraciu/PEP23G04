options = [1, 2]
choices = [4, 3.5]
currency = [5, 10]

print('1. Cappuccino ... 4 lei')
print('2. Espresso ...3.5 lei')
choice = int(input('Ce optiune alegeti? [1,2]: ').strip())
money = int(input('Introduceti o bacnota [5,10]: ').strip())
if money in currency:
    if choice in options:
        print(f'Veti primi restul de {money - choices[choice - 1]} lei.')
    else:
        print('Optiune Invalida')
else:
    print('Bancnota Incorrecta')

## to many choices
# if choice== '1' and money== '5':
#     print('Veti primi restul de 1 lei.')

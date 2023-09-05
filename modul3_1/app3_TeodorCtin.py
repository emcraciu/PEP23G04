cappuccino = 1
espresso = 2
pret_cappuccino = 4
pret_espresso = 3.5
optiune_aleasa = int(input('1. Cappuccino         ... 4 lei \n 2. Espresso          ... 3.5 lei \n Ce optiune alegeti? [1, 2]:'))
bancnota_introdusa = int(input('Introduceti o bancnota [5,10]:'))

if optiune_aleasa == cappuccino:
    print(f'Veti primi restul de: {bancnota_introdusa - pret_cappuccino} \n Produsul se livreaza...')
elif optiune_aleasa == espresso:
    print(f'Veti primi restul de {bancnota_introdusa - pret_espresso} \n Produsul se livreaza...')


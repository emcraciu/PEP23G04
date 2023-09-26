STOCK = {'Mere': {100: 20, 101: 20}}


def show_stock(product):
    pass


def add_product(product, price, quantity):
    product, price, quantity = product.strip(), price.strip(), quantity.strip()
    try:
        merchendise = (STOCK[product])
    except KeyError:
        merchendise = STOCK[product] = {}

    try:
        stock = merchendise[int(price)]
    except KeyError:
        merchendise[int(price)] = int(quantity)
    else:
        merchendise[int(price)] = stock + int(quantity)


def remove_product(product, price, quantity):
    product, price, quantity = product.strip(), price.strip(), quantity.strip()
    try:
        merchendise = (STOCK[product])
    except KeyError:
        print(f'Produsul introdus nu se afla in stoc')
        return
    try:
        stock = merchendise[int(price)]
    except KeyError:
        print(f'{product} la pretul {price} nu se afla in stoc')
        return
    if stock < int(quantity):
        print('Nu avem suficient stoc pentru comanda dorita')
        return
    merchendise[int(price)] = stock - int(quantity)


def change_request(option):
    if option == '3':
        response = input('Please provide: product, price, quantity')
        data = response.split(',')
        remove_product(*data)
    elif option == '2':
        response = input('Please provide: product, price, quantity')
        data = response.split(',')
        add_product(*data)


while True:
    print('Meniu:')
    option = input('''
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
''')
    option = option.strip()
    if option == '4':
        exit()
    change_request(option)

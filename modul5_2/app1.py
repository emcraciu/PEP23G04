STOCK = {'product': {100: 20, 101: 20}}
def show_stock(product):
    pass

def add_product(product, price, quantity):
    pass

def remove_product(product, price, quantity):
    pass

def get_change_request():
    input('Please provide: product, price, quantity')

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
    elif option == '3':
        get_change_request()


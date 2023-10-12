class Shop:
    categories = {'Haine': [], 'Accesorii': [], 'Imbracaminte': []}

    def first_menu(self):
        print('''Bun venit la magazinul PyCharm
        1. Categorii.
        2. Produse.
        3. Iesire.    
    ''')
        try:
            option = int(input('Alegeti optiunea:'))
            if option not in range(1, 4):
                raise Exception
        except Exception:
            print('Optiunea aleasa nu e valida.')
            self.first_menu()
        else:
            if option == 1:
                self.category_menu()

    def category_menu(self):
        print(f' category '.center(80, '#'))
        for category in self.categories:
            print(f'--- {category}')
        input()
        self.first_menu()

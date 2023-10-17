class Shop:
    categories = {'Haine': [], 'Accesorii': [], 'Imbracaminte': []}
    first_menu_list = ['Categorii', 'Produse', 'Iesire']
    product_menu_list = ['Adaugare', 'Vizualizare', 'Iesire']

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
            elif option == 2:
                self.product_menu()

    def category_menu(self):
        print(f' category '.center(80, '#'))
        for category in self.categories:
            print(f'--- {category}')
        input()
        self.first_menu()

    def product_menu(self):
        print(f' product '.center(80, '#'))
        print('''Optiuni:
        1.Adaugare
        2.Vizualizare
        3.Iesire
    ''')
        option = self.__get_option(self.product_menu, self.product_menu_list)
        print(option)
        if option == 3:
            self.first_menu()

    def __get_option(self, menu, menu_options):
        option = input('Introduceti optiunea: ')
        try:
            option = int(option.strip())
        except ValueError:
            print('Option is not valid.')

            return menu()

        else:
            if option not in range(1, len(menu_options) + 1):
                print('Valoarea optiunii nu este valida:')
                return menu()

            return option


s = Shop()
s.first_menu()
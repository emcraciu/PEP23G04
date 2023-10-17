class Shop:
    categories = {'Haine': [{'Nume': 'Tricou', 'Pret': 45.44, 'Stoc': 34},
                            {'Nume': 'Pantaloni', 'Pret': 50.99, 'Stoc': 40}],
                  'Accesorii': [],
                  'Imbracaminte': []}
    first_menu_list = ['Categorii', 'Produse', 'Iesire']
    product_menu_list = ['Adaugare', 'Vizualizare', 'Iesire']

    def first_menu(self):
        print('''Bun venit la magazinul PyCharm''')
        for index, entry in enumerate(self.first_menu_list):
            print(f'    {index + 1}. {entry}')
        option = self.__get_option(self.first_menu, self.first_menu_list)
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
        print('''Optiuni: ''')
        for index, entry in enumerate(self.product_menu_list):
            print(f'    {index + 1}. {entry}')
        option = self.__get_option(self.product_menu, self.product_menu_list)
        print(option)
        if option == 3:
            self.first_menu()
        elif option == 2:
            self.list_products()
        elif option == 1:
            self.add_product()

    def list_products(self):
        for category, product_list in self.categories.items():
            print(f' {category} '.center(80, '#'))
            for product in product_list:
                print(*(f'{key}: {value}\n' for key, value in product.items()))

    def add_product(self):
        category = input('Categoria pordusului: ')
        if not self.categories.get(category, False):
            self.categories.update({category: []})
        else:
            self.categories[category] += [{'bla': 'test'}]
        print(self.categories)

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

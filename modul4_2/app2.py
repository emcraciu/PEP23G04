




def putere(lista: list):
    result = lista[0] ** lista[1]
    print(result)
    print(lista)


if __name__ == '__main__':
    def suma(lista: list):
        result = 0
        for i in lista:
            result += i
        print(result)
        print(lista)
        return result


    menu = {
        '1': putere,
        '2': suma,
        '3': putere,
    }
    input('Introduceti numere. Cand sunteti gata, introduceti x.')
    lista_numere = []
    while True:
        number = input("Number: ")
        if number == 'x':
            break
        else:
            number = int(number)
            lista_numere.append(number)
    print(lista_numere)

    meniu = '''
    Meniu:
    1. Media numerelor
    2. Suma numerelor
    3. Puterea numerelor din lista de numere
    4. Iesire
    '''

    print(meniu)

    answer = input('Introduceti optiunea: ').strip()
    # menu.get(answer)(lista_numere)
def medie(lista: list):
    result = suma(lista) / len(lista)
    print(result)
    print(lista)


medie([1,2,3])
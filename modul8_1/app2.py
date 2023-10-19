class Masina:
    def __init__(self, marca: str, usi: int, culoare: str, an:
    int, pret: float):
        self.marca = marca
        self.usi = usi
        self.culoare = culoare
        self.an = an
        self.__pret = pret

    def getPret(self):
        return self.__pret

    def __add__(self, other):
        pret = self.getPret() + other.getPret()
        return Masina('', 0, '', 0, pret)


masina1 = Masina("Audi", 4, "gri", 2006, 3400)
masina2 = Masina("BMW", 2, "maro", 2007, 4788.60)
masina3 = Masina("Volvo", 4, "gri", 2017, 27000)
masina4 = Masina("Audi", 4, "negru", 2013, 10200)
masina5 = Masina("Audi", 2, "gri", 2005, 3400)
masina6 = Masina("BMW", 4, "negru", 2017, 22000)
masina7 = Masina("Volvo", 4, "gri", 2017, 27000)

masini = [masina7, masina6, masina5, masina4, masina3, masina1, masina2]

avr = sum(masini[1:], start=masini[0]).getPret() / len(masini)
print(avr)

x = masina1 + masina2 + masina3 + masina4 + masina5 + masina6 + masina7
print(x.getPret() / len(masini))


def my_map(masina: Masina):
    return masina.getPret()


print(map(my_map, masini))
print(list(map(my_map, masini)))

# Map

# regular function
avr = sum(map(my_map, masini)) / len(masini)
print(avr)

# lambda function
avr = sum(map(lambda masina: masina.getPret(), masini)) / len(masini)
print(avr)

# Filter
result = filter(lambda masina: masina.getPret() > 10000, masini)
print(result)

# print(list(result)) # this will consume the filter that is a generator
first_car = next(result)
other_cars = list(result)

print(sum(other_cars, start=first_car).getPret() / (len(other_cars) + 1))

# BMW



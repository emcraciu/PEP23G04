import random

pricepull1 = ['suc', 'chipsuri', 'prajituri', ]
pricepull1.extend(['' for _ in range(100)])
pricepull2 = ['prajitor', 'consola', 'tastatura', ]
pricepull2.extend(['' for _ in range(100)])
pricepull3 = ['robot', 'masina', 'racheta', ]
pricepull3.extend(['' for _ in range(100)])


def check_age(cnp):
    current_year = 2023
    id = cnp[0:7]
    if len(id) != 7:
        print('not enough characters')
    else:
        year = int(id[1:3])
        print(year)
        if id[0] < '5':
            year += 1900
        else:
            year += 2000
        result = current_year - year
        if result >= 18:
            return True
        else:
            return False


CNP = input('CNP: ')
while True:
    try:
        valoare_bon = int(input('Introduceti valoarea bonului: '))
    except ValueError:
        print('Nu ati introdus un numar.')
    else:
        break
if check_age(CNP):
    pass
else:
    print('Nu aveti varsta necesara: ')
if valoare_bon < 100:
    print('Valoarea bonului este gresita')
elif 100 <= valoare_bon <= 500:
    option = random.choice(pricepull1)
    if option:
        print(f'Ai castigat:{option}')
    else:
        print('Ai pierdut')
elif 500 < valoare_bon <= 1000:
    option = random.choice(pricepull2)
    if option:
        print(f'Ai castigat:{option}')
    else:
        print('Ai pierdut')
else:
    option = random.choice(pricepull3)
    if option:
        print(f'Ai castigat:{option}')
    else:
        print('Ai pierdut')

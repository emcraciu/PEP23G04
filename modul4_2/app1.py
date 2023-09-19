def sondaj_varsta():
    participanti_sondaj = int(input('Cati participanti avem la sondaj?'))
    raspunsuri = list()
    for i in range(participanti_sondaj):
        print(i + 1)
        varsta = 0
        while not varsta:
            try:
                varsta = int(input(f'Introduceti varsta participantului {i + 1}'))
            except:
                continue
        raspunsuri.append(varsta)
    print(raspunsuri)
    v_total = 0
    for i in raspunsuri:
        v_total += i
    medie = v_total / participanti_sondaj
    return medie

raspuns = sondaj_varsta()
print(raspuns)
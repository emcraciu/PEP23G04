curr_year = 2023
id = input('first 7 number from cnp: ')
if len(id) != 7:
    print('not enough characters')
else:
    year = int(id[1:3])
    print(year)
    if id[0] < '5':
        year += 1900
    else:
        year += 2000
    result = curr_year - year
    if result >= 18:
        print('Aveti peste 18 ani.')
    else:
        print('Nu aveti peste 18 ani')

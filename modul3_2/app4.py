password = '7788'
counter = 0
while input('Introduceti parola:') != password:
    print('Parola gresita, mai incercati')
    counter += 1
    if counter >= 3:
        print('Acces restrictionat')
        break
else:
    print('Acces permis')

username = input('Introduceti usernameul:')
password = input('Introduceti parola:')


def validare_parola(password):
    print(password)
    if '%' not in password and '!' not in password and '@' not in password:
        print('Parola trebuie sa contina una din urmatoarele caractere: %, !, @.')
    for i in range(10):
        i = str(i)
        if i in password:
            break
    else:
        print('Parola trebuie sa contina o cifra')


validare_parola(password)

username = input('Introduceti un nume de utilizator: ')


def validare_parola(password):
    result = True
    # if {'%', '!', '@'}.symmetric_difference(set(password)):
    if '%' not in password and '!' not in password and '@' not in password:
        print('Parola trebuie sa contina unul dintre urmatoarele caractere: %, @, !')
        result = False
    for i in range(10):
        i = str(i)
        if i in password:
            break
    else:
        print('Parola trebuie se contina o cifra')
        result = False
    if len(password) < 7:
        print('Parola trebuia sa contina minim 7 caractere')
        result = False

    return result


while not validare_parola(input('Introduceti o parola: ')):
    pass

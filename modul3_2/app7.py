lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
print(lista_taskuri)
# result = list(set(lista_taskuri))
result = []
for element in lista_taskuri:
    if element not in result:
        result.append(element)
print(result)

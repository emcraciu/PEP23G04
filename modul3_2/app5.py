# 01P - Teodor

list1 = ['Masa', 5, 'Scaun', 4.5, [5, 6, 7], 8]

for obj in list1:
    var_type = str(type(obj)).split("\'")[1]
    print(f'Tipul obiectului {obj} este {var_type}')

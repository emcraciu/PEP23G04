list1 = []

for _ in range(3):
    admin = input('admin:')
    password = input('password:')
    user_tuple = (admin, password)
    list1.append(user_tuple)

for item in list1:
    print(f'{item[0]} -> {item[1]}')

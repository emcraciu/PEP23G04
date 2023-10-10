class Car:
    color = 'red'
    wheels = 4
    is_clean = True

    def __init__(self, extra_wheel=False, color='blue'):
        if extra_wheel:
            self.wheels += 1
        self.color = color

    def drive(self):
        print(f'Driving {self.color} car ...')
        self.is_clean = False

    def wash_car(self):
        self.is_clean = True

my_car = Car(extra_wheel=True, color='black')
print(my_car.wheels)
print(my_car.color)
print('Clean car:', my_car.is_clean)
my_car.drive()
print('Clean car:', my_car.is_clean)
my_car.wash_car()
print('Clean car:', my_car.is_clean)

# your_car = Car(extra_wheel=False, color='white')
# print(your_car.wheels)
# print(your_car.color)

result = 'a'.capitalize()
print(result)
result = ['a'].append('b')
print(result)
result = my_car.wash_car()
print(result)
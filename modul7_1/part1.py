# color = 'blue'
# print(color)

class Car:
    color = 'red'

    def drive(self):
        print(f'Driving {self.color} car ...')



my_car = Car()
print(my_car)
print('my_car:', my_car.color)
my_car.color = 'blue'
print('my_car:', my_car.color)
my_car.drive()
# print(dir(my_car))


your_car = Car()
print(your_car)
print('your_car:', your_car.color)
your_car.color = 'green'
print('your_car:', your_car.color)
your_car.drive()
# print(dir(your_car))

# def x():
#     pass
#
# print(x.__name__)
# print(Car.drive(Car))
#
# print(Car.color)
# print(dir(Car))
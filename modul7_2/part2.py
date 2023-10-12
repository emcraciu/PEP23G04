# get/set/hasattr


class Car(object):
    color = 'red'
    wheels = 4
    is_clean = True

    def __init__(self, extra_wheel=False, color='blue'):
        if extra_wheel:
            self.wheels += 1
        self.color = color

    def drive(self):
        if getattr(self, 'nav', False):
        #if hasattr(self, 'nav') and self.nav:  # self.nav:
            print(f'Driving {self.color} {self.__class__.__name__} with nav ...')
        else:
            print(f'Driving {self.color} {self.__class__.__name__} ...')
        self.is_clean = False

    def wash_car(self):
        self.is_clean = True


class Logan2(Car):
    color = 'white'
    nav = True

    def __init__(self, extra_wheel=False, color='white', nav=False):
        super().__init__(extra_wheel=extra_wheel, color=color)
        self.nav = nav


l = Logan2(nav=True, color='green')
l.drive()

c = Car()
c.drive()


print('Dot notation', c.color)
print('Get function:', getattr(c, 'color'))
setattr(c, 'color2', 'yellow')
print('Set function', c.color2)
c.color2 = 'blue'
print('Dot notation', c.color2)
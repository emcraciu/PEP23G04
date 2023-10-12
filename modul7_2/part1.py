from modul7_1.part1 import Car

class Logan1(Car):
    color = 'white'

l = Logan1()
l.drive()

from modul7_1.part2 import Car

class Logan2(Car):
    color = 'white'
    nav = True

    def __init__(self, extra_wheel=False, color='white', nav=False):
        super().__init__(extra_wheel=extra_wheel, color=color)
        self.nav = nav


l = Logan2(nav=True, color='green')
l.drive()
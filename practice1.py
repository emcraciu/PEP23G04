"""
A production facility needs an iterable object to keep track off car warranty.
Each car have an int serial and datetime object for when the car was produced
Iterating the object will return all cars that are still covered by 3 years warranty (serial, <timedelta>)
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add sold care
    d) 10p: Method to print cars not covered by warranty
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Call method to add (sell) car (serial, <datetime>))
        - 1588, 20 Jan 2019 10:30:32
        - 1692, 20 Jan 2021 9:20:25
        - 1994, 20 Jan 2022 9:10:30
    c) 10p: Call method to return expired warranty (serial, <datetime>))
    d) 10p: Iterate the created object and write each care covered by warranty in a file
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""

# def my_func():
#     '''documentation for function'''
#     pass

"""this is module documentation"""
import datetime


class Warranty:
    """this is class documentation"""

    def __init__(self):
        self.warranties = {}

    def __iter__(self):
        return WarrantyIterator(self.warranties)

    def add_car(self, serial_number: int, date: str):
        """this will add a new car to the list of warranties"""
        date_object = datetime.datetime.strptime(date, '%d %b %Y %H:%M:%S')
        self.warranties.update({serial_number: date_object})

    def get_expired_warranties(self):
        now = datetime.datetime.now()
        for serial, date in self.warranties.items():
            result = now - date
            if result.days / 365 > 3:
                print(serial)


class WarrantyIterator:

    def __init__(self, warranty_data: dict):
        self.warranty_data = warranty_data

    def __iter__(self):
        return self

    def __next__(self):
        if not self.warranty_data:
            raise StopIteration
        now = datetime.datetime.now()
        for serial, date in self.warranty_data.copy().items():
            result = now - date
            if result.days / 365 < 3:
                r = (serial, result)
                del self.warranty_data[serial]
                return r
            else:
                del self.warranty_data[serial]
                continue


w = Warranty()
w.add_car(1588, '28 Jan 2019 10:30:32')
w.add_car(1598, '28 Jan 2022 10:30:32')
print(w.warranties)
w.get_expired_warranties()
with open('exemple.txt', 'w') as file:
    for serial in w:
        file.write(str(serial) + '\n')

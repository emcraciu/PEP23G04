# Iterator  -  Random letter generator
from random import randint


class RandomLetterIterator:

    def __init__(self, number_of_letters: int):
        self.number_of_letters = number_of_letters

    def __iter__(self):
        return self

    def __next__(self):
        self.number_of_letters -= 1
        if self.number_of_letters < 0:
            raise StopIteration
        return chr(randint(33, 127))


# iterator = RandomLetterIterator(3)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))
# print('#' * 80)
#
# for letter in RandomLetterIterator(5):
#     print(letter)
# my_str = 'abcd'
# print(type(my_str), id(my_str))
# str_iter = my_str.__iter__()
# print(str_iter)
# print(str_iter.__iter__())


class MyPasswordGen:
    def __init__(self, password_length):
        self.pl = password_length

    def __iter__(self):
        return RandomLetterIterator(self.pl)

    def generate_password(self):
        return ''.join(RandomLetterIterator(self.pl))


password = MyPasswordGen(10)
print(password.generate_password())
print('#' * 80)
for letter in password:
    print(letter)

#### generator
print('#' * 80)


def generator(number_of_letters):
    while number_of_letters > 0:
        number_of_letters -= 1
        yield chr(randint(33, 127))


my_gen = generator(10)
for letter in my_gen:
    print(letter)

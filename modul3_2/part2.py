# string1 = "Anxa are mere"
# number1 = 100
# x = False
#
# # for char in string1:
# #     if char == 'x':
# #         print('Am gasit x.')
# #         x = True
# #         break
# #
# # if not x:
# #     print("Sirul nu contine x.")
# #
# # print(char)  # if for loop have no letters then char is not created
# #
# # print(dir(string1))
# # print(string1.__iter__())
# # # print(number1.__iter__())
# #
# # # for number in number1:
# # #     print(number)
# #
# # var1 = string1.__iter__()
# # print(next(var1))
#
# # for with else:
# string1 = "Anxa are mere"
#
# for char in string1:
#     if char == 'x':
#         print('Am gasit x.')
#         break
#
# else:
#     print("Sirul nu contine x.")


# Lists

list1 = [11, '2', None, True, 2.3, '2', 2]
print(list1)

list1.append('abc')
print(list1)

list1.remove(None)
print(list1)

# for element in list1:
#     if element is True:
#         list1.remove(True)
#     # list1.append(True)
#     print('element from list: ', element)
#
# print(list1)

for element in list1.copy(): # list1[:]
    if element is True:
        list1.remove(True)
    # list1.append(True)
    print('element from list: ', element)

print(list1)
print(list1[:])  # this is a copy of the original list
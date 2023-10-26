from time import sleep

a = range(10)

with open('file.txt', 'a') as file:
    for i in a:
        sleep(1)
        # if i == 3:
        #     raise Exception
        file.write(str(i))
        file.flush() # not needed in context
        # file.close() # not needed in context


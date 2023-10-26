class MyObject:

    def __init__(self):
        print('before before')
        self.my_var = 10

    def __enter__(self):
        print('before')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('after')

# m = MyObject()
# print(type((m)))

with MyObject() as my_object:
    # raise Exception
    print(my_object.my_var)
    print('in context')

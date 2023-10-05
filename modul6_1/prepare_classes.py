# Exceptions


class MyCustomException(Exception):
    pass

def calculate(a, b):
    try:
        result = sum([a, b])
        # 1/0
        if not result:
            raise MyCustomException('This exception is special')
    except MyCustomException as e:
        print(f'got custom exception with args: {e.args}')
        raise e
    except Exception:
        print('got other exception')


def sum(numbers):
    result = 0
    for n in numbers:
        result += n
    return result

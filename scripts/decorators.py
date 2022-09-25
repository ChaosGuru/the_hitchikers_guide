def decorator(func):
    def wrapper():
        print('Decorator')
        func()

    return wrapper


def hello():
    print('Hello, World!')


hello = decorator(hello)


@decorator
def hello2():
    print('Hello, People!')
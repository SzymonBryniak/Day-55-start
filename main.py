def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f'You called {function.__name__}')
        print(f'It returned: {function(args[0], args[1], args[2])}')
    return wrapper_function


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1,2,3)

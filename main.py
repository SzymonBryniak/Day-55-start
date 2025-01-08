
def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f'You called {function.__name__}{args}')
        print(f'It returned: {function(args)}')
    return wrapper_function


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1,2,3)

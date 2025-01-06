class user:
  def __init__(self, username):
    self.user = username
    self.is_online = False


def authenticated_decorator(function):
  def wrapper_function(*args, **kwargs):
    if args[0].is_online == True:
      return f'{function(args[0])} is authenticated'
  return wrapper_function


@authenticated_decorator
def is_authenticated(function):
  return print(f'This is {function.user}`s blogpost')


user_object = user('Szymon')
user_object.is_online = True
is_authenticated(user_object)

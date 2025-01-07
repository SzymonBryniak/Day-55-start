class user:
  def __init__(self, username):
    self.user = username
    self.is_online = False


def authenticated_decorator(function):
  def wrapper_function(*args, **kwargs):
    if args[0].is_online == True:
     print('authenticated')
     function(args[0])
  return wrapper_function


@authenticated_decorator
def is_authenticated(function):
  print(f'This is {function.user}`s blog post')


user_object = user('Szymon')
user_object.is_online = True
is_authenticated(user_object)

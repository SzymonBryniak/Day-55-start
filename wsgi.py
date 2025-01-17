
from flask import Flask

app = Flask(__name__)



def make_bold(function):
  def wrapper_function():
    return f'<b>{function()}<b>'
  return wrapper_function

def make_emphasis(function):
  def wrapper_function():
    return f'<em>{function()}<em>'
  return wrapper_function

def make_underlined(function):
  def wrapper_function():
    return f'<u>{function()}<u>'
  return wrapper_function


@app.route('/')
def hello_world():
  return '<h1 style="text-align: center">Hello World!</h1>\
          <p>This is a paragraph.</p>\
          <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGswbGxpZnJlbTV5M2d5YW1tbG8wb3cyc2R2eHRuNDdhcHFqNnp1ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m1EQb15sqXIOeKFtju/giphy.gif">'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
  return "<u><em>Bye</em></u>"


@app.route("/username/<name>/<int:number>")
def greet(name):
  return f"Hello there {name + '12'}!"




if __name__ == "__main__":
  app.run(debug=True)

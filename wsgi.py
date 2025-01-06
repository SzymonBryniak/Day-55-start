from flask import Flask
import requests
app = Flask(__name__)


requests.get("https://www.google.com")


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
          <img src="https://api.deepai.org/job-view-file/5d3fa914-ce43-45cc-afe1-8bcc640a68fa/outputs/output.jpg" width=200>\
          <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmxkZWlxem51bmFuMDdib2c0NTF4dnloNmQwcmRsYW4xcWZsZXgxZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KYgNd2BvEuRfZjIZRs/giphy.webp">'


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

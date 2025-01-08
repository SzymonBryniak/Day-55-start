from flask import Flask


app = Flask(__name__)


@app.route('/')
def display_h1():
  return '<h1>Guess a number between 0 and 9</h1>'


if __name__ == "__name__":
  app.run(debug=True)

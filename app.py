from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def display_h1():
  return '<h1>Guess a number between 0 and 9</h1>\
          <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmR4ZHdhaDFvZGtuYnVtOHdvMG56aDdtemw2YmQyN3g1eGszaGJpNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5K7ngCtszoxxbaBieC/giphy.webp">'



@app.route('/<int:number>')
def random_numbers(number):
  random_number = random.randint(0, 9)
  if random_number == number:
    return '<h1>you guessed the number</h1>'
  else:
    return "<h1>you didn't guess the number</h1>"
  
 

if __name__ == "__name__":
  app.run(debug=True) 

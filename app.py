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
    return f'<h1>your number was: {number} you guessed the number.</h1>'
  elif random_number > number:
    return 'Too low, try again!\
              <br> \
              <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYW9uNmVrbnNxMXZ4N3E5ZXRtM2pqMDcyYXdsZDNoZThyc3RzNzdteiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2kS8TzTRJz8hFhLHMK/giphy.webp">'

  elif random_number < number:
    return 'Too high, try again! \
      <br> \
      <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2Roc3RzOHJpZTM2d2FiNTBrdzdqODYwNXhwbWFrOHhxajA2NHh5eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaP9whaYPIK00g/giphy.webp">'
  
 

if __name__ == "__name__":
  app.run(debug=True) 

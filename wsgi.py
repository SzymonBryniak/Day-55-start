
from flask import Flask
import requests
app = Flask(__name__)


requests.get("https://www.google.com")

@app.route('/')
def hello_world():
  return '<h1 style="text-align: center">Hello World!</h1>\
          <p>This is a paragraph.</p>\
          <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fcatastic.pet%2Fcat-breeds%2F11-interesting-facts-about-the-munchkin-cat%2F&psig=AOvVaw2zuerc9eIHZpah7lS5EkSs&ust=1736193512154000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPCjsISv34oDFQAAAAAdAAAAABAp">'

@app.route("/bye")
def say_bye():
  return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name):
  return f"Hello there {name + '12'}!"








if __name__ == "__main__":
  app.run(debug=True)
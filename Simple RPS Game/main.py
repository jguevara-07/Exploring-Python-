from flask import Flask, render_template
import random

app = Flask(
  __name__,
  template_folder = 'templates',
  static_folder = 'static'
)

options = ["rock", "paper", "scissors"]

@app.route('/')
def index():
  message = "Lets play RPS!  Choose your weapon!"
  return render_template(
    'index.html',
    output = message
    )
  
@app.route('/rock')
def rock():
  opponent = random.choice(options)
  if opponent == "rock":
    result = f"Computers choice is {opponent}. It is a Tie!"
  elif opponent == "paper":
    result = f"Computers choice is {opponent}. You Lose!"
  else:
    result = f"Computers choice is {opponent}. You Win!!!!"
  bs_class = "secondary"
  return render_template(
    'rock.html',
    output = result,
    color = bs_class
    )
@app.route('/paper')
def paper():
  opponent = random.choice(options)
  if opponent == "rock":
    result = f"Computers choice is {opponent}. You Win!!!!"
  elif opponent == "paper":
    result = f"Computers choice is {opponent}. It is a Tie!"
  else:
    result = f"Computers choice is {opponent}. You Lose!"
  bs_class = "primary"
  return render_template(
    'paper.html',
    output = result,
    color = bs_class
    )
@app.route('/scissor')
def scissor():
  opponent = random.choice(options)
  if opponent == "rock":
    result = f"Computers choice is {opponent}. You Lose!"
  elif opponent == "paper":
    result = f"Computers choice is {opponent}. You Win!"
  else:
    result = f"Computers choice is {opponent}. It is a Tie!"
  bs_class = "warning"
  return render_template(
    'scissor.html',
    output = result,
    color = bs_class
    )
app.run(
  host = "0.0.0.0",
  port = 8080,
  debug = True
)

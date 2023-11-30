import turtle
from turtle import *
from time import *

class Paddle(Turtle):
  def __init__(self, x,y):
    super().__init__()
    self.shape("square")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.color("white")
    self.penup()
    self.goto(x,y)

  def go_up(self):
    if (self.ycor() < 250):
      new_y = self.ycor() + 20
      self.goto(self.xcor(), new_y)
  def go_down(self):
    if (self.ycor() > -250):
      new_y = self.ycor() - 20
      self.goto(self.xcor(), new_y)

class Ball(Turtle):
  def __init__(self,):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.move_speed = 0.1
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)
  def x_bounce(self):
    self.x_move = self.x_move * (-1)
    self.move_speed *= 0.9
  def y_bounce(self):
    self.y_move = self.y_move * (-1)
  def reset_position(self):
    self.goto(0,0)
    self.x_bounce()
    self.move_speed = 0.1

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_score()

  def update_score(self):
    self.clear()
    self.goto(-100, 200)
    self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
    self.goto(100, 200)
    self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

  def l_point(self):
    self.l_score += 1
    self.update_score()

  def r_point(self):
    self.r_score += 1
    self.update_score()
  def clear_scoreboard(self,name):
    turtle.clear()
    pencolor("green")
    write(f"{name} гравець переможець", align="center", font=("Courier", 40, "normal"))


scoreBoard = Scoreboard()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball=Ball()
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

def r_paddle_up():
  r_paddle.go_up()
def r_paddle_down():
  r_paddle.go_down()
def l_paddle_up():
  l_paddle.go_up()
def l_paddle_down():
  l_paddle.go_down()

screen.onkeypress(r_paddle_up, "w")
screen.onkeypress(r_paddle_down, "s")
screen.onkeypress(l_paddle_up, "Up")
screen.onkeypress(l_paddle_down, "Down")
screen.listen()
while True:
  sleep(0.01)
  screen.update()
  ball.move()
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.y_bounce()
  if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    ball.x_bounce()
  if ball.xcor() > 380:
    ball.reset_position()
    scoreBoard.l_point()
  if ball.xcor() < -380:
    ball.reset_position()
    scoreBoard.r_point()
  if scoreBoard.l_score == 5:
    scoreBoard.clear_scoreboard("Лівий")
    break
  elif scoreBoard.r_score == 5:
    scoreBoard.clear_scoreboard("Правий")
    break

turtle.exitonclick()

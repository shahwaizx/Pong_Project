import turtle
import time
import winsound
# Displaying Screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(width=800, height=600)
win.title("Pong Game")
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 9
ball.dy = 9

# Pen
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y = y+30
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y = y-30
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y-30
    paddle_b.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y = y+30
    paddle_b.sety(y)

# Keyboard Bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")




# Main loop
while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    time.sleep(0.01677)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy*-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy*-1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx*-1
        score_a = score_a+1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx*-1
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce3.wav", winsound.SND_ASYNC)

    if (ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor()+60 and ball.ycor() > paddle_b.ycor()-60):
        ball.setx(340)
        ball.dx = ball.dx*-1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    if (ball.xcor() <-340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor()+60 and ball.ycor() > paddle_a.ycor()-60):
        ball.setx(-340)
        ball.dx = ball.dx*-1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() <-250:
        paddle_a.sety(-250)
    if paddle_b.ycor()>250:
        paddle_b.sety(250)
    if paddle_b.ycor()<-250:
        paddle_b.sety(-250)
    if score_a==5 or score_b==5:
        break


# Pen 2
pen2 = turtle.Turtle()
pen2.color("Red")
pen2.goto(0, 0)
pen2.hideturtle()
pen2.write("GAME OVER",align="center",font=("Pricedown", 36, "normal"))

while True:
    winsound.PlaySound("gameover3.wav", winsound.SND_ASYNC)
    win.update()
    time.sleep(4)
    break





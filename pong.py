import turtle
import winsound
import os

wn = turtle.Screen()
wn.title("Pong by Jess Erhabor")
wn.bgcolor("black")
wn.setup(width=800, height=600) # Customizes the size of the window
wn.tracer(0) # Stops the window from updating automatically

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Sets the speed of animation to the maximum so there is no lag
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # default is 20px by 20px
paddle_a.penup() # So there are no lines drawn as it moves
paddle_a.goto(-350, 0) # Positioned left side of screen

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) # Positioned right side of screen

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() # So there are no lines drawn as it moves
ball.goto(0, 0) # Positioned in the centre of the screen
ball.dx = 2 # The change (delta) in the x-direction is 2px
ball.dy = -2

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # Every turtle starts from centre of screen so we don't want a pen mark of where it's moved to
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
"""
The following functions control the movement of the paddle.
Here the elements will move 20px up or down depending on the
event. See line 61.
"""
def paddle_a_up():
    y = paddle_a.ycor() # Need to know what the y-coordinate of the paddle is
    y += 20 # Adds 20 pixels to the y-coordinate
    paddle_a.sety(y) # Sets y to the new "y" on line 38

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y) 

# Keyboard binding
"""
This section waits for the user to press the relevant keys 
to activate the required function.
"""
wn.listen() # Listens for keyboard input
wn.onkeypress(paddle_a_up, "w") # When lowercase w is pressed on the keyboard, the paddle_a_up function runs to move paddle_a up 20px
wn.onkeypress(paddle_a_down, "s") # When lowercase s is pressed on the keyboard, the paddle_a_down function runs to move paddle_a down 20px
wn.onkeypress(paddle_b_up, "Up") # Up arrow key
wn.onkeypress(paddle_b_down, "Down") # Down arrow key

# Main game loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: # As ball is 20 x 20px (so 10px from centre) and the window is 600px (so 300px from centre)
        ball.sety(290)
        ball.dy *= -1 # Reverses direction of ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay, bounce.wav&")

    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay, bounce.wav&")

    if ball.xcor() > 390: 
        ball.goto(0, 0) # Ball resets to centre of screen as player loses round
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay, bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay, bounce.wav&")



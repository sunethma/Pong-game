# A simple pong game with Python 3
import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong by @Sunethma")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a=0
score_b=0

game_time = 60  # Game time in seconds
game_over = False

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.1
ball.dy=0.1

#Pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

wn = turtle.Screen()
timer = turtle.Turtle()
timer.speed(0)
timer.color("white")
timer.penup()
timer.hideturtle()
timer.goto(0, 220)
timer.write(f"Time: {game_time}", align="center", font=("Courier", 24, "normal"))


def update_timer():
    global game_time

    timer.clear()
    timer.write(f"Time: {game_time}", align="center", font=("Courier", 24, "normal"))

    if game_time > 0:
        game_time -= 1
        wn.ontimer(update_timer, 1000)  # call again after 1 second
    else:
        timer.clear()
        global game_over
        game_over = True
        if score_a > score_b:
            result = "Player A Wins!"
        elif score_b > score_a:
            result = "Player B Wins!"
        else:
            result = "It's a Draw!"

        timer.goto(0, 170)

        timer.write(
            f"Game Over\n{result}",
            align="center",
            font=("Courier", 24, "normal")
        )

# Start the timer
update_timer()


# paddle movement functions
def paddle_a_up():
    y=paddle_a.ycor()
    if y < 250:      # 300 - 50
        y+=20
        paddle_a.sety(y)


def paddle_a_down():
    y=paddle_a.ycor()
    if y > -250:      # 300 - 50
        y-=20
        paddle_a.sety(y)



def paddle_b_up():
    y=paddle_b.ycor()
    if y < 250:      # 300 - 50
        y+=20
        paddle_b.sety(y)


def paddle_b_down():
    y=paddle_b.ycor()
    if y > -250:      # 300 - 50
        y-=20
        paddle_b.sety(y)    

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




# Main game loop
while True:
    wn.update()

    # Move the ball
    if not game_over:

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)


    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        



    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


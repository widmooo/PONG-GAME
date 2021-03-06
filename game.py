# Pong Game by widmooo
# v1.0
# Turtle Librery: https://docs.python.org/3/library/turtle.html
 
# Main
import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("Pong Game v1.0 (by widmooo)")
wn.bgpic('graphic/bcg.gif')
wn.setup(width=800, height=600)
wn.tracer(0)  # make game moves faster


# Score
score_a = 0
score_b = 0

# Set Score
# set_a = 0
# set_b = 0

# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("#ca3b32")
player_a.shapesize(stretch_wid=6, stretch_len=1)
player_a.penup()
player_a.goto(-360, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("#38393b")
player_b.shapesize(stretch_wid=6, stretch_len=1)
player_b.penup()
player_b.goto(360, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.2  # speed and direction X
ball.dy = 0.2  # speed and direction Y

# Score Menu
score_m = turtle.Turtle()
score_m.speed(0)
score_m.color("White")
score_m.penup()
score_m.hideturtle()
score_m.goto(0, 250)
score_m.write("0    0", align="center", font=("Arial", 20, "normal"))

# Winner A
winner_a = turtle.Turtle()
winner_a.speed(0)
winner_a.color("#ca3b32")
winner_a.penup()
winner_a.hideturtle()
winner_a.goto(-180, 0)
winner_a.write("    ", align="center", font=("Arial", 40, "bold"))

# Winner B
winner_b = turtle.Turtle()
winner_b.speed(0)
winner_b.color("#38393b")
winner_b.penup()
winner_b.hideturtle()
winner_b.goto(180, 0)
winner_b.write("    ", align="center", font=("Arial", 40, "bold"))

# Pause
paused = False
paused_txt = turtle.Turtle()
paused_txt.speed(0)
paused_txt.color("red")
paused_txt.penup()
paused_txt.hideturtle()
paused_txt.goto(0, 0)


# Function
def player_a_up():
    y = player_a.ycor()
    if player_a.ycor() > 220 or paused == True:
        y += 0
        player_a.sety(y)
    else:
        y += 10
        player_a.sety(y)


def player_a_down():
    y = player_a.ycor()
    if player_a.ycor() < -220 or paused == True:
        y += 0
        player_a.sety(y)
    else:
        y -= 10
        player_a.sety(y)


def player_b_up():
    y = player_b.ycor()
    if player_b.ycor() > 220 or paused == True:
        y += 0
        player_b.sety(y)
    else:
        y += 10
        player_b.sety(y)


def player_b_down():
    y = player_b.ycor()
    if player_b.ycor() < -220 or paused == True:
        y += 0
        player_b.sety(y)
    else:
        y -= 10
        player_b.sety(y)


def pause_f():
    global paused
    if paused == True:
        paused = False
        paused_txt.clear()
    else:
        paused = True
        paused_txt.write("PAUSE", align="center", font=("Arial", 70, "bold"))


def win_func():
    if score_a == 2:
        winner_a.write("RED WON!", align="center", font=("Arial", 40, "bold"))
        winsound.PlaySound("sound/win1.wav", winsound.SND_ASYNC)
        time.sleep(3)
        score_a == 0
        score_m.clear()
        score_m.write("0    0", align="center", font=("Arial", 20, "normal"))
        winner_a.clear()
        paused = False

    if score_b == 2:
        winner_b.write("GREEN WON!", align="center",
                       font=("Arial", 40, "bold"))
        winsound.PlaySound("sound/win1.wav", winsound.SND_ASYNC)
        score_b == 0
        score_m.clear()
        score_m.write("0    0", align="center", font=("Arial", 20, "normal"))
        winner_b.clear()
        paused = False


# Bind
wn.listen()
wn.onkeypress(player_a_up, 'w')
wn.onkeypress(player_a_down, 's')
wn.onkeypress(player_b_up, 'Up')
wn.onkeypress(player_b_down, 'Down')
wn.onkeypress(pause_f, 'space')

# Game loop
while True:
    if not paused:
        wn.update()
        win_func()

        # Ball moving
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Court checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            score_m.clear()
            score_m.write("{}    {}".format(score_a, score_b),
                          align="center", font=("Arial", 20, "normal"))
            winsound.PlaySound("sound/point.wav", winsound.SND_ASYNC)

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            score_m.clear()
            score_m.write("{}    {}".format(score_a, score_b),
                          align="center", font=("Arial", 20, "normal"))
            winsound.PlaySound("sound/point.wav", winsound.SND_ASYNC)

        # Ball colisions
        if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < player_b.ycor() + 50 and ball.ycor() > player_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < player_a.ycor() + 50 and ball.ycor() > player_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("sound/bounce.wav", winsound.SND_ASYNC)
            
    else:
        wn.update()  # do nothing else paused is True

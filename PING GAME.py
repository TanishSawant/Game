import turtle

#score
score_a = 0
score_b = 0

wn = turtle.Screen()

wn.title("PING GAME")

wn.bgcolor("black")

wn.setup(width = 800 , height = 600)

wn.tracer(0)

#paddle A

paddle_a = turtle.Turtle()

paddle_a.speed(0)

paddle_a.shape("square")

paddle_a.color("white")

paddle_a.shapesize(stretch_wid = 5 , stretch_len = 1)

paddle_a.penup()

paddle_a.goto(-350 , 0)

#paddle B

paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("square")

paddle_b.color("white")

paddle_b.shapesize(stretch_wid = 5 , stretch_len = 1)

paddle_b.penup()

paddle_b.goto(350 , 0)

#ball

ball = turtle.Turtle()

ball.speed(0)

ball.shape("circle")

ball.color("white")

ball.penup()

ball.goto(0 , 0)

ball.dx = 1

ball.dy = -1

#Function

def paddle_a_up():

    y = paddle_a.ycor()

    y+=20

    paddle_a.sety(y)

#keyboard binnding

wn.listen()

wn.onkeypress(paddle_a_up,"w")

def paddle_a_down():

    y = paddle_a.ycor()

    y-=20

    paddle_a.sety(y)

#keyboard binnding

wn.listen()

wn.onkeypress(paddle_a_down,"s")

def paddle_b_down():

    y = paddle_b.ycor()

    y-=20

    paddle_b.sety(y)

#keyboard binnding

wn.listen()

wn.onkeypress(paddle_b_down,"l")

def paddle_b_up():

    y = paddle_b.ycor()

    y+=20

    paddle_b.sety(y)

#keyboard binnding

wn.listen()

wn.onkeypress(paddle_b_up,"o")

#Pen

pen = turtle.Turtle()

pen.speed(0)

pen.color("white")

pen.penup()

pen.hideturtle()

pen.goto(0 , 260)

pen.write("Player A : 0     Player B : 0" , align = "center" , font=("courier",24,"normal"))






#Main game loop

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290 :
        ball.sety(290)

        ball.dy *= -1

    if ball.ycor() <= -290 :

        ball.sety(-290)

        ball.dy *= -1

    if ball.xcor() >= 390:

        ball.goto(0,0)

        ball.dx *= -1

        score_a += 1

        ball.dy *= -1

        pen.clear()

        pen.write("Player A : {}     Player B : {}".format(score_a , score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor()<=-390:

        ball.goto(0,0)

        ball.dx *= -1

        ball.dy *= -1

        score_b +=1

        pen.clear()

        pen.write("Player A : {}     Player B : {}".format(score_a , score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() == 340 and (ball.ycor() <= paddle_b.ycor() + 50 and ball.ycor() >= paddle_b.ycor() - 50):

        ball.dx *= -1



    if ball.xcor() == -340 and (ball.ycor() <= paddle_a.ycor()+ 50 and ball.ycor() >= paddle_a.ycor() - 50):
        ball.dx *= -1



    if score_a == 20:

        k = turtle.Turtle()

        k.color("red")

        k.write("player A won!" , align = "centre" , font = ("courier",24,"normal"))

        exit(0)

        print("player a won")

    if score_b == 20:
        k = turtle.Turtle()

        k.color("red")

        k.write("player B won!", align="centre", font=("courier", 24, "normal"))

        exit(0)

        print("player b won")



turtle.done()


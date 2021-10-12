#jangan diberantakin bwang (emot batu) -Script by RafaDaffa
import turtle as t
playerAscore=0
playerBscore=0

window=t.Screen()
window.title("Ping-Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Membuat kotak kiri
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#Membuat kotak kanan
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#Membuat bola

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#Membuat kotak score

pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))



#Menggerakan kotak kiri

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)


def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

#Menggerakan kotak kanan

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)


def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

#Menentukan keyboard untuk main

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()

    #Pergerakan bola
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #Mengatur border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

        if ball.xcor()>390:
            ball.goto(0,0)
            ballxdirection=ballxdirection*-1
            playerAscore=playerAscore+1
            pen.clear()
            pen.write("Player A:{}        Player B:{}".format(playerAscore,playerBscore),align='center',font=('Monaco',24,"normal"))



        if (ball.xcor())<-390:
            ball.goto(0,0)
            ballxdirection=ballxdirection*-1
            playerBscore=playerBscore+1
            pen.clear()
            pen.write("Player A:{}        Player B:{}".format(playerAscore,playerBscore),align='center',font=('Monaco',24,"normal"))


    #Menangani tabrakan bola

    if(ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection=ballxdirection*-1

    if(ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1

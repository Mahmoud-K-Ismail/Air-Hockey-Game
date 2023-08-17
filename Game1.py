import turtle
import winsound

#creating a window
wn = turtle.Screen()
wn.title("Pong by Mkassem")
wn.bgcolor("White")
wn.setup(width = 800, height =600)
wn.tracer(0)

#score 
score_a = 0
score_b = 0
#paddle A
paddle_a = turtle.Turtle() #create an object
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len= 1)
paddle_a.color("Red")
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle B
paddle_b = turtle.Turtle() #create an object
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len= 1)
paddle_b.color("Blue")
paddle_b.penup()
paddle_b.goto(350,0)
#ball
ball = turtle.Turtle() #create an object
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B : 0", align = "center", font = ("courier", 24,"normal"))



#Functions
def paddle_a_up():
    y= paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y= paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
#Main game loop
while True:
    wn.update()
    

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boarder checking

    if (paddle_a.ycor()>250):
        paddle_a.sety(250)

    if (paddle_b.ycor()>250):
        paddle_b.sety(250)
        

    if (paddle_a.ycor()<-250):
        paddle_a.sety(-250)

    if (paddle_b.ycor()<-250):
        paddle_b.sety(-250)

    if(ball.ycor()> 290):
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("sound1.wav",winsound.SND_ASYNC)


    if(ball.ycor()< -290):
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("sound1.wav",winsound.SND_ASYNC)


    if (ball.xcor() > 390):
        ball.goto(0,0)
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B : {}".format(score_a,score_b), align = "center", font = ("courier", 24,"normal"))
        
    if (ball.xcor() < -390):
        ball.goto(0,0)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B : {}".format(score_a,score_b), align = "center", font = ("courier", 24,"normal"))

    
    if (ball.xcor()>340 and ball.xcor()<341 and ball.ycor()< paddle_b.ycor()+45 and ball.ycor()> paddle_b.ycor()-45):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)

    elif (ball.xcor() < -340 and ball.xcor()< -341 and ball.ycor()< paddle_a.ycor()+45 and ball.ycor()> paddle_a.ycor()-45):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
    
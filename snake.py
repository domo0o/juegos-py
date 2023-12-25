import turtle
import time
import random

Delay = 0.1
body_segments =  []
score = 0
high_score = 0

windows = turtle.Screen()

# title
windows.title("carpincho vs mandarina (x maximo)")

# windows size
windows.setup(width=600, height=600)

#background color
windows.bgcolor("light blue")

# head settings

# turtle obj
head = turtle.Turtle()
# para que se quede fijo
head.speed(0)
# shape:
head.shape("square")
#head color
head.color("brown")


#food config
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(250, 100)
food.direction = "stop" 

orange = turtle.Turtle()
orange.speed(0)
orange.shape("circle")
orange.color("orange")
orange.penup()
orange.goto(100, 250)
orange.direction = "stop"
#para no dejar ratro de la animacion
head.penup()
# center
head.goto(0, 0)
# para q espere q yo le de otra direcsion
head.direction = "stop"


#score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f"Puntos 0        Record 0", align="center", font=("Maximum Impact", 20))


def move():
    if head.direction == "up":
        #almacenar el valor actual de la cordenada y:
        y =head.ycor()
        head.sety(y + 10)
    if head.direction == "down":
        #almacenar el valor actual de la cordenada y:
        y =head.ycor()
        head.sety(y - 10)
    if head.direction == "right":
        #almacenar el valor actual de la cordenada y:
        y =head.xcor()
        head.setx(y + 10)
    if head.direction == "left":
        #almacenar el valor actual de la cordenada y:
        y =head.xcor()
        head.setx(y - 10) 


def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"


# conectar teclado
windows.listen()
windows.onkeypress(dirUp, "Up")
windows.onkeypress(dirDown, "Down")
windows.onkeypress(dirRight, "Right")
windows.onkeypress(dirLeft, "Left")


while True:
# colisiones sneak vs windows
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
      time.sleep(0.1)
      head.goto(0,0)
      head.direction = "stop"

      #esconder segmentos despues de morir
      for segment in body_segments:
          segment.goto(1000, 1000)

      #clean segments after the game reiniciate
      body_segments.clear()
      score = 0
      text.clear()  
      text.write(f"Puntos {score}        Record {high_score}", align="center", font=("Maximum Impact", 20))

      
 
     

          
    windows.update()
   # colisiones head vs food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("brown")
        new_segment.penup()
        body_segments.append(new_segment)
        score += 1
        if score > high_score:

           high_score = score
        text.clear()  
        text.write(f"Puntos {score}        Record {high_score}", align="center", font=("Maximum Impact", 20))
    
    totalseg =len(body_segments) 
    if head.distance(orange) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        orange.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("brown")
        new_segment.penup()
        body_segments.append(new_segment) 
# new segment config
    
        score += 1
        if score > high_score:

           high_score = score
        text.clear()  
        text.write(f"Puntos {score}        Record {high_score}", align="center", font=("Maximum Impact", 20))
    
    totalseg =len(body_segments)

    for i in range(totalseg -1 , 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalseg > 0:         
        x =head.xcor()
        y =head.ycor()
        body_segments[0].goto(x, y)



        


    move()


    #coliiciones con el cuerpo
    for segment in body_segments:
            if segment.distance(head) < 10:
                time.sleep(1)
                head.goto(0,0)
                head.DEFAULT_ANGLEORIENT
                head.direction = "stop"

#esconder segmentos
                for segment in body_segments:
                    segment.goto(1000, 1000)
                body_segments.clear()

                score = 0
                text.clear()  
                text.write(f"Puntos {score}        Record {high_score}", align="center", font=("Maximum Impact", 20))
    time.sleep(Delay)



turtle.done()


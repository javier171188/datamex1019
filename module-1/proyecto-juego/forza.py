import turtle
import time
import random

delay = 0.1 #seconds
sensivility = 15
speed_car = 40
place_start= 10
crash_check = False
#Set up the screen
wn = turtle.Screen()
wn.title('Forza Hack (pre beta version)')
wn.bgcolor('grey')
wn.setup(width=700, height = 700)
#wn.tracer(0) #turn off the screen updates



#advice
st = turtle.Turtle()
st.speed(0)
st.shape('square')
st.color('white')
st.penup()
st.hideturtle()
st.goto(0,120)


#finish line

finish = turtle.Turtle()
finish.speed(0)
finish.shape('turtle')
finish.color('white')
finish.penup()
finish.hideturtle()
finish.goto(-300,350)
finish.pendown()


#oponent

oluw = turtle.Turtle()
oluw.speed(0)
oluw.shape('circle')
oluw.color('black')
oluw.penup()
oluw.goto(144,-52)
oluw.direction = 'stop'

oruw = turtle.Turtle()
oruw.speed(0)
oruw.shape('circle')
oruw.color('black')
oruw.penup()
oruw.goto(156,-52)
oruw.direction = 'stop'

ordw = turtle.Turtle()
ordw.speed(0)
ordw.shape('circle')
ordw.color('black')
ordw.penup()
ordw.goto(144,-80)
ordw.direction = 'stop'

oldw = turtle.Turtle()
oldw.speed(0)
oldw.shape('circle')
oldw.color('black')
oldw.penup()
oldw.goto(156,-80)
oldw.direction = 'stop'


op = turtle.Turtle()
op.speed(0)
op.color('blue')
op.penup()
op.shape('square')
op.setposition(150,-50)

oc = turtle.Turtle()
oc.speed(0)
oc.color('blue')
oc.penup()
oc.shape('square')
oc.setposition(150,-60)

of = turtle.Turtle()
of.speed(0)
of.color('blue')
of.penup()
of.shape('square')
of.setposition(150,-80)


opponent = [oluw, oruw, oldw, ordw, op, oc, of]


#Grass
grass = turtle.Turtle()
grass.speed(0)
grass.color('green')
grass.penup()
grass.setposition(300,-400)
grass.pendown()
grass.pensize(150)
#for side in range(2):
grass.lt(90)
grass.fd(840)
grass.lt(90)
grass.fd(600)
grass.lt(90)
grass.fd(840)

#Wall
wall = turtle.Turtle()
wall.speed(0)
wall.color('brown')
wall.penup()
wall.setposition(220,-400)
wall.pendown()
wall.pensize(10)
wall.lt(90)
wall.fd(800)
wall.lt(90)
wall.fd(441)
wall.lt(90)
wall.fd(850)


#starter indicator
st = turtle.Turtle()
st.speed(0)
st.shape('square')
st.color('white')
st.penup()
st.hideturtle()
st.goto(0,120)
st.write('Ready', align='center', font = ('Courier', 100, 'normal'))



#car

luw = turtle.Turtle()
luw.speed(0)
luw.shape('circle')
luw.color('black')
luw.penup()
luw.goto(-6,-200)
luw.direction = 'stop'

ruw = turtle.Turtle()
ruw.speed(0)
ruw.shape('circle')
ruw.color('black')
ruw.penup()
ruw.goto(6,-200)
ruw.direction = 'stop'

rdw = turtle.Turtle()
rdw.speed(0)
rdw.shape('circle')
rdw.color('black')
rdw.penup()
rdw.goto(6,-215)
rdw.direction = 'stop'

ldw = turtle.Turtle()
ldw.speed(0)
ldw.shape('circle')
ldw.color('black')
ldw.penup()
ldw.goto(-6,-215)
ldw.direction = 'stop'



car = turtle.Turtle()
car.speed(0)
car.shape('square')
car.color('red')
car.penup()
car.goto(0,-200)
car.direction = 'stop'

fr = turtle.Turtle()
fr.speed(0)
fr.shape('triangle')
fr.color('red')
fr.setheading(90)
fr.penup()
fr.goto(0,-187)
fr.direction = 'stop'

bc = turtle.Turtle()
bc.speed(0)
bc.shape('square')
bc.color('red')
bc.penup()
bc.goto(0,-210)
bc.direction = 'stop'

bcf = turtle.Turtle()
bcf.speed(0)
bcf.shape('square')
bcf.color('red')
bcf.penup()
bcf.goto(0,-215)
bcf.direction = 'stop'


car_parts = [luw, ruw, ldw, rdw, car, fr, bc, bcf]


def start():
        time.sleep(1)
        st.clear()
        st.write('Set', align='center', font = ('Courier', 100, 'normal'))
        time.sleep(1)
        st.clear()
        st.write('GOOO!', align='center', font = ('Courier', 100, 'normal'))




def move():
    if car.direction == 'up':
        y = car.ycor()
        car.sety(y+20)
    if car.direction == 'down':
        y = car.ycor()
        car.sety(y-20)
    if car.direction == 'left':
        if car.xcor() > -200:
            luw.setx(luw.xcor()-sensivility)
            ruw.setx(ruw.xcor()-sensivility)
            ldw.setx(ldw.xcor()-sensivility)
            rdw.setx(rdw.xcor()-sensivility)

            fr.setx(fr.xcor()-sensivility)
            bc.setx(bcf.xcor()-sensivility)
            bcf.setx(bcf.xcor()-sensivility)



            x = car.xcor()
            car.setx(x-sensivility)
            car.direction = 'stop'
    if car.direction == 'right':
        if car.xcor() < 200:

            luw.setx(luw.xcor()+sensivility)
            ruw.setx(ruw.xcor()+sensivility)
            ldw.setx(ldw.xcor()+sensivility)
            rdw.setx(rdw.xcor()+sensivility)


            fr.setx(fr.xcor()+sensivility)
            bc.setx(bcf.xcor()+sensivility)
            bcf.setx(bcf.xcor()+sensivility)

            x = car.xcor()
            car.setx(x+sensivility)
            car.direction = 'stop'


def go_left():
    car.direction = 'left'
def go_right():
    car.direction = 'right'

#Keyboard bindings
wn.listen()
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')


start()


while True:
    wn.update()



    move()

    for e in opponent:
        e.sety(e.ycor()-speed_car)


    if op.ycor()<bcf.ycor() and place_start > 2:
        ran = random.randint(-200, 200)
        for e in opponent:
            e.sety(e.ycor()+780)
        oluw.setx(ran-6)
        oruw.setx(ran+6)
        oldw.setx(ran-6)
        ordw.setx(ran+6)
        op.setx(ran)
        oc.setx(ran)
        of.setx(ran)
        place_start -=1

    if op.ycor()<bcf.ycor() and place_start > 1:
        place_start -=1

    if place_start ==1:
        finish.pensize(10)
        finish.fd(400)
        finish.clear()
        finish.sety(finish.ycor()-speed_car -5)
        finish.setx(-300)
        finish.fd(200)


    st.write(str(place_start), align='right', font = ('Courier', 30, 'normal'))
    #if place_start == 1:
    #    place_start -=1





    time.sleep(delay)
    st.clear()
    if finish.ycor() < -150:

        st.write('You win!!', align='center', font = ('Courier', 100, 'normal'))
        break
    elif crash_check:
        st.write('Crash, you lose :(', align='center', font = ('Courier', 40, 'normal'))
        break



    #colisiones
    for i in car_parts:
        for e in opponent:
            if e.distance(i) < 20:

                crash_check = True




wn.mainloop()

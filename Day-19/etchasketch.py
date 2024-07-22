from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def turn_left():
    new_direction = tim.heading() + 10
    tim.setheading(new_direction)

def turn_right():
    new_direction = tim.heading() - 10
    tim.setheading(new_direction)

def clear():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.setheading(0)
    tim.pendown()
    

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear, "c")

screen.exitonclick()
import turtle

turtle.speed(6)
#turtle.color("read")

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
        
#draw_square(100)
#turtle.exitonclick()

count = 0
while count < 90:
    draw_square(100)
    turtle.right(4)
    count += 1

turtle.exitonclick()
  
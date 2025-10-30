import turtle

turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(600, 600)

polygon = turtle.Turtle()
num_sides = 4
side_length = 50
angle = 90

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
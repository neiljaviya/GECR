#Create following regular polygons (regular means all sides the same lengths, all
#angles the same) using for loop in turtle
#• An equilateral triangle
#• A square
#• A hexagon
#• An octagon

import turtle

t = turtle.Turtle()

n = int(input("Enter the no of the sides of the polygon : "))
l = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n):
	turtle.forward(l)
	turtle.right(360 / n)

turtle.done()
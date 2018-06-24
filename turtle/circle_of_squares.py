import turtle

# Initialize
window = turtle.Screen()
window.bgcolor("#9aceed")
yalla = turtle.Turtle()
yalla.shape("arrow")
yalla.color("white")
yalla.speed(10000)
yalla.width(1.5)

def draw_polygon(tortoise, length, sides):
	for i in range(0, sides):
		tortoise.forward(length)
		tortoise.right(360.0/sides)

def circle_of_polygons(tortoise, length, sides, num):
	for i in range(0, num):
		draw_polygon(tortoise, length, sides)
		tortoise.right(360.0/num)

circle_of_polygons(yalla, 50, 9, 18)

window.exitonclick()
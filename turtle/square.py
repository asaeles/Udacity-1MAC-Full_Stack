import turtle

# Initialize
window = turtle.Screen()
window.bgcolor("#9aceed")
yalla = turtle.Turtle()
yalla.shape("turtle")
yalla.color("white")
yalla.speed(5)
yalla.width(2)

def draw_spiral(start):
	tortoise.color("white")
	for i in [1,2,3,4]:
		tortoise.forward(side)
		tortoise.right(90)

def draw_circle(tortoise, radius):
	tortoise.color("red")
	tortoise.circle(radius)

def draw_triangle(tortoise, side):
	tortoise.color("yellow")
	for i in (1,2,3):
		tortoise.forward(side)
		tortoise.right(120)

draw_square(yalla, 100)
draw_circle(yalla, 100)
yalla.right(120)
draw_triangle(yalla, 100)

window.exitonclick()
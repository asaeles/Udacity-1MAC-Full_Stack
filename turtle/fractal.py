import turtle

# Initialize
window = turtle.Screen(); window.bgcolor("#9aceed"); window.colormode(255)
yalla = turtle.Turtle(); yalla.color((30,78,177),(118,240,19))
yalla.shape("turtle"); yalla.width(1.5); yalla.speed(100)

def slide(tortoise, ang, dist):
	tortoise.penup(); tortoise.left(ang);
	tortoise.forward(dist)
	tortoise.right(ang); tortoise.pendown()

def draw_triangle(tortoise, side):
	tortoise.begin_fill()
	for x in xrange(1,4):
		tortoise.forward(side)
		tortoise.left(120)
	tortoise.end_fill()

def draw_fractal(tortoise, side, level = 1):
	slide(tortoise, 60, side)
	for x in xrange(1,4):
		if level == 1:
			draw_triangle(tortoise, side)
		else:
			draw_fractal(tortoise, side/2, level-1)
		tortoise.forward(side)
		tortoise.right(120)
	slide(tortoise, 240, side)

slide(yalla, 210, 230) # Dead center
draw_fractal(yalla, 200.0, 4)

window.exitonclick()
import turtle

# Initialize
window = turtle.Screen()
window.bgcolor("#9aceed")
yalla = turtle.Turtle()
yalla.speed(100)

def draw_spiral(tortoise, repeat,
	start_col = (1.0,1.0,1.0),
	end_col = (1.0,1.0,1.0)):
	
	tortoise.shape("circle")
	tortoise.width(5)
	tortoise.turtlesize(0.25)
	r1 = start_col[0]
	g1 = start_col[1]
	b1 = start_col[2]
	r2 = end_col[0]
	g2 = end_col[1]
	b2 = end_col[2]
	r = r1
	g = g1
	b = b1
	radius = 0
	for i in range(1, repeat+1):
		tortoise.color(r, g, b)
		radius = radius + 5
		tortoise.circle(radius, 90)
		r = r + (r2-r1)/repeat
		g = g + (g2-g1)/repeat
		b = b + (b2-b1)/repeat

draw_spiral(yalla, 52, (1.0,1.0,0.0), (1.0,0.0,0.0))

window.exitonclick()
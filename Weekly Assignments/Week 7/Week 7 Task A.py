import turtle

t=turtle.Turtle()

#drawing a polygon:
def draw_polygon(side_length, sides):
    angle=(180-(180*(sides-2))/sides)
    for i in range(0, sides-1):
        t.forward(side_length)
        t.right(angle)

    t.forward(side_length)
    print(angle)

draw_polygon(100, 6)

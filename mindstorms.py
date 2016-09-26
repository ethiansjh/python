import turtle

def draw_square(name):
    i = 0
    while i <= 3:
        name.forward(100)
        name.right(90)
        i = i + 1

#def draw_triangle(name):
#    i = 0
#    while i < 3:
#        name.forward(80)
#        name.left(120)
#        i = i + 1

def draw():
    #create background
    window = turtle.Screen()
    window.bgcolor("black")

    #draw square
    jay = turtle.Turtle()
    jay.color("white")
    jay.shape("arrow")
    jay.color("red")
    jay.speed("fastest")

    for i in range(1,37):
            draw_square(jay)
            jay.right(100)
    window.exitonclick()

#   draw circle
#    dj = turtle.Turtle()
#   dj.shape("turtle")
#    dj.color("Yellow")
#    dj.speed("fast")
#    dj.circle(80)
#    dj.width(2)

    #draw triangle
#    andy = turtle.Turtle()
#    andy.shape("circle")
#    andy.color("blue")
#    andy.speed("fast")
#    andy.width(3)
#    draw_triangle(andy)


draw()

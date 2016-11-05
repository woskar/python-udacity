import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    pete = turtle.Turtle()
    pete.shape("circle")
    pete.color("green")

    for j in range(0,3):
        pete.forward(200)
        pete.left(120)

    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)

    for i in range (0,36):
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    
    window.exitonclick()

draw_square()

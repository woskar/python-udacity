import turtle

def art():
    window = turtle.Screen()
    window.bgcolor("cyan")
    
    
    oskar = turtle.Turtle()
    oskar.shape("turtle")
    oskar.color("yellow")
    oskar.speed(15)

    for i in range (0,18):
        oskar.circle(80)
        oskar.right(20)
    oskar.right(90)
    oskar.forward(300)

    window.exitonclick()


art()

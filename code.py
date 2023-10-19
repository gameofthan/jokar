import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Danger Joker Face")
screen.bgcolor("black")

# Create a turtle for drawing
joker_turtle = turtle.Turtle()
joker_turtle.speed(0)  # Set the drawing speed to the fastest
joker_turtle.color("white")

# Draw the joker's face
joker_turtle.penup()
joker_turtle.goto(0, -100)
joker_turtle.pendown()
joker_turtle.circle(100)

# Draw the joker's smile
joker_turtle.penup()
joker_turtle.goto(-60, 20)
joker_turtle.pendown()
joker_turtle.setheading(-60)
joker_turtle.circle(80, 120)

# Draw the joker's menacing eyes
joker_turtle.penup()
joker_turtle.goto(-40, 160)
joker_turtle.pendown()
joker_turtle.circle(10)
joker_turtle.penup()
joker_turtle.goto(40, 160)
joker_turtle.pendown()
joker_turtle.circle(10)

# Add an angry brow
joker_turtle.penup()
joker_turtle.goto(-60, 200)
joker_turtle.pendown()
joker_turtle.setheading(-30)
joker_turtle.circle(60, 70)

joker_turtle.penup()
joker_turtle.goto(60, 200)
joker_turtle.pendown()
joker_turtle.setheading(-150)
joker_turtle.circle(-60, 70)

# Hide the turtle and display the drawing
joker_turtle.hideturtle()
turtle.done()

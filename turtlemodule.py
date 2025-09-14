import turtle
turtle.getscreen()
t = turtle.Turtle()
sides = int(input("How many sides? (enter a number): ")) #asks the user for the number of sides
color = input("What color do you want? (enter a color or hexadecimal): ") #asks the user for the color
length = int(input("How long should each side be? (enter a number): ")) #asks the user for the length of each side
t.color(color)
angle = 360/sides #calculates the angle based on the number of sides
for i in range(sides): #For loop for number of sides
    t.forward(length) #moves the turtle forward by the length specified by the user
    t.right(angle) #turns the turtle right by the angle variable
turtle.done()  # Keeps the window open

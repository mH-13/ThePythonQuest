import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Happy Birthday Surprise!")

# Create turtle objects
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

text = turtle.Turtle()
text.speed(0)
text.hideturtle()

# Function to draw a star
def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Function to draw the cake
def draw_cake():
    # Draw the cake base
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    t.color("#8B4513")  # Brown color for cake
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    # Draw cake frosting
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.color("#FF69B4")  # Pink frosting
    t.begin_fill()
    t.forward(300)
    for _ in range(180):
        t.forward(1)
        t.left(1)
    t.left(180)
    t.forward(300)
    t.end_fill()
    
    # Draw candles
    candle_positions = [-100, -50, 0, 50, 100]
    for x in candle_positions:
        # Draw candle
        t.penup()
        t.goto(x, 0)
        t.pendown()
        t.color("yellow")
        t.begin_fill()
        for _ in range(2):
            t.forward(10)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.end_fill()
        
        # Draw flame
        t.penup()
        t.goto(x + 5, 40)
        t.pendown()
        t.color("orange")
        t.begin_fill()
        t.circle(5)
        t.end_fill()

# Function to display animated text
def write_message():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    message = "Happy Birthday!"
    
    text.penup()
    text.goto(0, 150)
    text.pendown()
    
    for i, char in enumerate(message):
        text.color(colors[i % len(colors)])
        text.write(char, align="center", font=("Arial", 36, "bold"))
        text.penup()
        text.forward(30)
        text.pendown()
        time.sleep(0.1)

# Function to create fireworks effect
def create_fireworks():
    positions = [(-200, 200), (200, 200), (0, 250), (-150, 150), (150, 150)]
    colors = ["red", "gold", "blue", "green", "purple", "pink"]
    
    for pos in positions:
        x, y = pos
        color = random.choice(colors)
        size = random.randint(20, 40)
        
        # Draw the main burst
        for _ in range(8):
            angle = random.randint(0, 360)
            draw_star(t, x, y, size, color)
            x += random.randint(-100, 100)
            y += random.randint(-50, 50)

# Main execution
def birthday_surprise():
    draw_cake()
    write_message()
    
    # Add some confetti
    for _ in range(50):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(5, 15)
        color = random.choice(["red", "yellow", "blue", "green", "purple", "pink"])
        draw_star(t, x, y, size, color)
    
    create_fireworks()
    
    # Add finale text
    text.clear()
    text.penup()
    text.goto(0, 200)
    text.pendown()
    text.color("white")
    text.write("This the last with of the day. Happy Birthday my Love! ", align="center", font=("Comic Sans MS", 24, "bold"))
    
    
    text.penup()
    text.goto(0, -200)
    text.pendown()
    text.color("yellow")
    text.write("Make a wish!", align="center", font=("Arial", 18, "italic"))

# Run the program
birthday_surprise()

# Keep the window open
screen.mainloop()
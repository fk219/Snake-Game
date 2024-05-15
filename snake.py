import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.goto(-290, 290)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.forward(580)
    border_pen.right(90)
border_pen.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body (segments)
segments = []

# Score
score = 0
high_score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 330)  # Position the score display above the square border
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def check_collision():
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        return True
    for segment in segments:
        if segment.distance(head) < 20:
            return True
    return False

def check_food():
    global score, high_score
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

def game_over():
    global score, high_score
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    score_display.clear()
    score_display.write("Game Over! Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    draw_retry_button()

def draw_retry_button():
    retry_button.showturtle()
    retry_button.onclick(retry_game)

def retry_game(x, y):
    global score, high_score
    retry_button.hideturtle()
    score = 0
    score_display.clear()
    score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    game_loop()

# Retry button setup
retry_button = turtle.Turtle()
retry_button.speed(0)
retry_button.shape("square")
retry_button.color("blue")
retry_button.penup()
retry_button.hideturtle()
retry_button.goto(0, 0)  # Set the position for the retry button

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
def game_loop():
    screen.update()

    # Move the snake
    move()

    # Check for collisions
    if check_collision():
        game_over()
        return

    # Check for food
    check_food()

    # Move the snake body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Call game_loop again after a delay
    screen.ontimer(game_loop, 100)

# Start the game loop
game_loop()

# Main event loop
turtle.mainloop()

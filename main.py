from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_prompt = screen.textinput(title= 'TURTLE RACE!!',prompt='Guess who will win?')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos =[-70, -40,- 10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_prompt:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()

            if win_color == user_prompt.lower():
                print(f"You were right!!! {win_color} did win!!")
                is_race_on = False
                break
            else:
                print(f"You lost!! {win_color} is the winner")
                is_race_on = False
                break

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()

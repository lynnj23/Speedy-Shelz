"""Speedy Shelz is a simple racing game in Turtle"""
#Sets up modules and methods
from turtle import Turtle, Screen
from turtle_type import Turtle_Colours, Race
draw = Turtle_Colours
dash = Race

#sets up co-ords for the initial turtle position
point_x = -240
point_y = -100
#turtles = 0
#This is test for bet completion
is_race_on = False
#Sets up the screen and its size
screen = Screen()
screen.setup (width=500,height=400)
#Provides a prompt for the use to make a bet on the winning turtle
user_bet = screen.textinput(title=" Make your bet", prompt="Which turtle will win the race? Enter a colour").lower()

#Calls method to line up turtles on left-hand side of the screen.
for x in range(0,6):
    draw.create_turtle_colour(x, point_x, point_y)
    point_y += 30

#checks tha the user has completed the bet process and stops game starting early
if user_bet:
    is_race_on = True
#this calls a method to test position state and move turtles
while is_race_on:
        dash.finish_line(is_race_on, user_bet)
        is_race_on = dash.finish_line(is_race_on, user_bet)
screen.exitonclick()
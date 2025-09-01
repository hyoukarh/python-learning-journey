def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

for goal in range(6):
    square()

# Code to pass Reborg's World Hurdles Challenge.
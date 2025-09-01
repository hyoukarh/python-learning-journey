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
    
def wall_scale():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        wall_scale()
    else:
        move()

# Code to pass Reborg's World Hurdles Challenge 4.
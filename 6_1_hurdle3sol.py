def tur():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    while wall_on_right() :
        move()
    tur()
    move()
    tur()
    while not wall_in_front():
        move()
    turn_left()

    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    
    
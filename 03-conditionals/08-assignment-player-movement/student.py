def player_movement(position, left_arrow, right_arrow, shift):
    if left_arrow and right_arrow:
        return position
    
    step = 2 if shift else 1

    if left_arrow:
        position -= step
    elif right_arrow:
        position += step
    
    return position
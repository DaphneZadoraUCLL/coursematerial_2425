def pad_right(xs, length, padding):
    current_length = len(xs)
    difference = length - current_length

    if difference == 0:
        return
        
    if difference >= 1:
        xs.extend([padding]*difference)
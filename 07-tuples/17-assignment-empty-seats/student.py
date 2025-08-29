def empty_seats(used_seats):
    if not used_seats:
        return 0
    return used_seats[-1] - used_seats[0] +1 - len(used_seats)
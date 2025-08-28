def invest(amount, rate, goal):
    years = 0
    while amount < goal:
        amount += amount * (rate / 100)
        years += 1
    return years
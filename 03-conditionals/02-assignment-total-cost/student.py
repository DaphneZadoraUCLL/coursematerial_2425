def total_cost(amount):
    if amount < 100:
        return amount + 10
    elif amount >= 200:
        return amount * 0.95
    else:
        return amount
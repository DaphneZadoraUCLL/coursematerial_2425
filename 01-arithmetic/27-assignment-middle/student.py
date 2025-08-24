def middle(a, b, c):
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    middle_val = a + b + c - min_val - max_val

    return middle_val
def subtuple(xs, ys):
    n = len(ys)
    for i in range(len(xs) -n + 1):
        if xs[i:i+n] == ys:
            return True
    return False
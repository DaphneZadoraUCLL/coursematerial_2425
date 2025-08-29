def split_in_two(xs):
    split_index = (len(xs) + 1) // 2


    left = xs[:split_index]
    right = xs[split_index:]

    return (left, right)
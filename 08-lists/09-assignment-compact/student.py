def compact(xs):
    result = []
    
    for x in xs:
        if x is not None:
            result.append(x)
    return result

def compact_in_place(xs):
    write_index = 0

    for x in xs:
        if x is not None:
            xs[write_index] = x
            write_index += 1

    del xs[write_index:]

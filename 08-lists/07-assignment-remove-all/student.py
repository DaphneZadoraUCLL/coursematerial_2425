def remove_all(xs, item_to_remove):
    write_index = 0
    for x in xs:
        if x != item_to_remove:
            xs[write_index] = x
            write_index += 1
    del xs[write_index:]
def remove_duplicate_lines(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        previous_line = None
        for line in src:
            if line != previous_line:
                dest.write(line)
                previous_line = line

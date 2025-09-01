def remove_empty_lines(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        for line in src:
            if line != '\n':
                dest.write(line)

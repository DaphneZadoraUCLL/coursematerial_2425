def is_capitalized(string):
    if string == "":
        return False
    if not string[0].isupper():
        return False
    if len(string) > 1 and not string[1:].islower():
        return False
    return True
def box(string):
    border = '+' + '-' * (len(string)+2) + '+'
    middle = f"| {string} |"
    return f"{border}\n{middle}\n{border}"
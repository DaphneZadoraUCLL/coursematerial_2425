def parse_position_x(string):
    s = string[1:-1]
    comma_index = s.index(",")
    x_str = s[:comma_index]
    return float(x_str)


def parse_position_y(string):
    s = string[1:-1]
    comma_index = s.index(",")
    y_str = s[comma_index+1:]
    return float(y_str)

string = "(12.453, 9.120)"
print(parse_position_x(string))  # 12.453
print(parse_position_y(string))  # 9.12
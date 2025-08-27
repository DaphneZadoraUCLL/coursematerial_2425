def is_digit(char):
    return '0' <= char <= '9'

def is_student_id(string):
    if len(string) != 8:
        return False
    first_char = (string[0])
    if first_char.lower() not in ['r', 's']:
        return False
    for char in string[1:]:
        if not is_digit(char):
            return False
    
    return True
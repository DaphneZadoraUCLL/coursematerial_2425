def matches_pattern(pattern, string):
    if len(pattern) != len(string):
        return False

    letter_combo = {}
    used_letters = set()

    for p_char, s_char in zip(pattern, string):

        if p_char in letter_combo:
            if letter_combo[p_char] != s_char:
                return False
        else:
            if s_char in used_letters:
                return False

            letter_combo[p_char] = s_char
            used_letters.add(s_char)

    return True

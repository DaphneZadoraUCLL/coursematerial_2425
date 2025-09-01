def group_by_first_letter(strings):
    groups = {}

    for word in strings:
        first_letter = word[0].upper()
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups

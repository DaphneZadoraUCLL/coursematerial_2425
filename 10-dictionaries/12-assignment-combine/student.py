def combine(d1, d2):
    result = {}

    for key in d1:
        dutch_word = d1[key]
        if dutch_word in d2:
            result[key] = d2[dutch_word]

    return result

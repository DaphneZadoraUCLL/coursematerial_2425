def inverse_lookup(dictionary, value):
    result = []
    for key in dictionary:
        if dictionary[key] == value:
            result.append(key)
    return result

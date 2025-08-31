def rankings(participants):
    result = {}
    rank = 1
    for participant in participants:
        result[participant] = rank
        rank = rank + 1
    return result

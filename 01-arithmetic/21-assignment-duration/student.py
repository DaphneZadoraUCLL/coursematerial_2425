def hours(duration):
    return duration // 3600

def minutes(duration):
    h = hours(duration)
    remaining_seconds = duration - (3600 * h)
    return remaining_seconds // 60

def seconds(duration):
    h = hours(duration)
    m = minutes(duration)
    remaining_seconds = duration - (3600 * h) - (60 * m)
    return remaining_seconds
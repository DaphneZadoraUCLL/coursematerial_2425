def counts(xs):
    freq = {}
    for x in xs:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

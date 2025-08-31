def find_duplicates(xs):
    seen = set()
    duplicates = set()

    for x in xs:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return list(duplicates)

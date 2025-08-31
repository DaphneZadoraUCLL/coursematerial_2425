def bubblesort(ns):
    n = len(ns)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if ns[j] > ns[j + 1]:
                ns[j], ns[j + 1] = ns[j + 1], ns[j]
                swapped = True
        if not swapped:
            break

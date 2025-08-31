def remove_runs(ns):
    if not ns:
        return []
    
    result = [ns[0]]

    for i in range(1, len(ns)):
        if ns[i] != ns[i-1]:
            result.append(ns[i])
    return result
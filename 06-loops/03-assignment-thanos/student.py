def thanos(queue_size, target_size):
    snaps = 0
    while queue_size > target_size:
        queue_size = queue_size // 2
        snaps += 1
    return snaps

def rpg2(n_sides, goal):
    count_wins = 0
    for die1 in range(1, n_sides+1):
        for die2 in range(1, n_sides+1):
            if die1 + die2 >= goal:
                count_wins += 1
    total_outcome = n_sides * n_sides
    probability = count_wins / total_outcome * 100
    return probability


def rpg3(n_sides, goal):
    count_wins = 0
    for die1 in range(1, n_sides+1):
        for die2 in range(1, n_sides+1):
            for die3 in range(1, n_sides+1):
                if die1 + die2 + die3 >= goal:
                    count_wins += 1
    total_outcome = n_sides * n_sides * n_sides
    probability = count_wins / total_outcome * 100
    return probability
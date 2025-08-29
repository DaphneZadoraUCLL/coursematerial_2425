def election_winner(votes):
    if not votes:
        return None
    
    sorted_votes = sorted(votes)
    current_count = 1
    best_count = 1
    winner = sorted_votes[0]

    for i in range(1, len(sorted_votes)):
        if sorted_votes[i] == sorted_votes[i-1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > best_count:
            best_count = current_count
            winner = sorted_votes[i]

    return winner

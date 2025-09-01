def election_winner(votes):
    if len(votes) == 0:
        return None

    vote_count = {}
    for x in votes:
        if x in vote_count:
            vote_count[x] += 1
        else:
            vote_count[x] = 1

    winner = max(vote_count, key=vote_count.get)
    return winner

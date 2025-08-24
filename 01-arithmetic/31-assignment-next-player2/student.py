def next_player2(player, player_count):
    next_p = player + 1
    if next_p > player_count:
        next_p = 1
    return next_p
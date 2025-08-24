def next_player(player, player_count):
    next_p = player + 1
    if next_p == player_count:
        next_p = 0

    return next_p
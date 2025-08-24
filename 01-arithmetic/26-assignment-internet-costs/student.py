def internet_costs(duration_in_seconds, cost_per_block):
    block_size = 6 * 60
    number_of_blocks = (duration_in_seconds + block_size - 1) // block_size

    return number_of_blocks * cost_per_block
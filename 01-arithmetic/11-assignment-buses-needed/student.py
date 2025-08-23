def buses_needed(people_count, bus_capacity):
    return (people_count + bus_capacity - 1) // bus_capacity

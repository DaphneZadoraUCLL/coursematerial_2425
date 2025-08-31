def orbit_chain(orbits, start):
    chain = [start]
    current = start

    while current in orbits:
        next_body = orbits[current]
        chain.append(next_body)
        current = next_body

    return chain

def desktop(catalog, components):
    total = 0
    for item in components:
        if item in catalog:
            price = catalog[item]
            total = total + price
        else:
            total = total + 0
    return total

def cake(stock, recipe_ingredients):
    max_cakes = float('inf')

    for ingredient, needed_amount in recipe_ingredients.items():
        if ingredient not in stock:
            return 0
        available_amount = stock[ingredient]
        possible_cakes = available_amount // needed_amount
        max_cakes = min(max_cakes, possible_cakes)

    return max_cakes

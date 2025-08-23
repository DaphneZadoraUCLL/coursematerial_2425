def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    cakes_from_eggs = eggs // eggs_per_cake
    cakes_from_flour = flour // flour_per_cake
    cakes_from_butter = butter // butter_per_cake
    cakes_from_sugar = sugar // sugar_per_cake
    
    return min(cakes_from_eggs, cakes_from_flour, cakes_from_butter, cakes_from_sugar)
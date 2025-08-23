def cake3(eggs, flour, butter, sugar):
    cakes_from_eggs = eggs //5
    cakes_from_flour = flour //250
    cakes_from_butter = butter // 200
    cakes_from_sugar =  sugar // 250

    return min(cakes_from_eggs,cakes_from_flour, cakes_from_butter, cakes_from_sugar)
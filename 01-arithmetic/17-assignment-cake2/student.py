def cake2(eggs, flour):
    cakes_from_eggs = eggs //5
    cakes_from_flour = flour //250

    return min(cakes_from_eggs,cakes_from_flour)
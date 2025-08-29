def heatwave(temperatures):
    hot = 0
    really_hot = 0

    for temp in temperatures:
        if temp >= 25:
            hot += 1
            if temp >= 30:
                really_hot += 1
        
        else:
            hot = 0
            really_hot = 0

        if hot >= 5 and really_hot >= 3:
            return True
    
    return False
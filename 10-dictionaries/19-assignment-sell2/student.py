def sell2(stock, model, size):
    if model not in stock:
        return False
    if size not in stock[model]:
        return False

    stock[model][size] -= 1

    if stock[model][size] == 0:
        del stock[model][size]
    if not stock[model]:
        del stock[model]
    return True

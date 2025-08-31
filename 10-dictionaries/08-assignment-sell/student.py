def sell(stock, model):
    stock[model] = stock[model] - 1
    if stock[model] == 0:
        del stock[model]

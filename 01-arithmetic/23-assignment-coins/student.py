def coins(amount):
    coin_five = amount // 5
    amount = amount - coin_five * 5

    coin_two = amount // 2
    amount = amount - coin_two * 2

    coin_one = amount

    return coin_five + coin_two + coin_one
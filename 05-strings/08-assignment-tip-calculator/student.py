def tip_calculator():
    total_price = float(input("Enter total price: "))
    tip_input = input("Enter tip percentage (default=20): ")

    if tip_input == '':
        tip_percentage = 20
    else:
        tip_percentage = float(tip_input)

    total_to_pay = total_price + (total_price * tip_percentage / 100)
    print(f"You have to pay {round(total_to_pay)}")
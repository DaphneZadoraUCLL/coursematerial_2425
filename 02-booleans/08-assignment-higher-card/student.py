def higher_card(card1, card2):
    if card1 == 1 and card2 == 1:
        return False
    if card1 == 1:
        return True
    if card1 > card2 and card2 != 1:
        return True
    
    return False
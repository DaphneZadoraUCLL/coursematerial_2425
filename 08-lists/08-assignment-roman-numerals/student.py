def to_roman(n):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = ['M', 'CM', 'D', 'CD', 'C', 'XC',
               'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    result = ''
    for i in range(len(values)):
        while n >= values[i]:
            n -= values[i]
            result += letters[i]
    return result


def from_roman(s):
    # Maak een woordenboek van Romeins symbool → waarde
    roman_to_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0       # Hier houden we het totaal bij
    i = 0           # Index om door de string te lopen

    while i < len(s):
        # Check of we een subtractive combinatie hebben
        if i + 1 < len(s):
            two_letters = s[i] + s[i + 1]
            if two_letters == 'IV':
                total += 4
                i += 2
                continue
            elif two_letters == 'IX':
                total += 9
                i += 2
                continue
            elif two_letters == 'XL':
                total += 40
                i += 2
                continue
            elif two_letters == 'XC':
                total += 90
                i += 2
                continue
            elif two_letters == 'CD':
                total += 400
                i += 2
                continue
            elif two_letters == 'CM':
                total += 900
                i += 2
                continue
        
        # Als het geen subtractive combinatie is, tel de waarde van 1 letter
        total += roman_to_value[s[i]]
        i += 1

    return total
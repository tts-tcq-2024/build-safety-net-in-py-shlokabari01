def generate_soundex(name):
    if not name:
        return ""

    soundex_mapping = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }

    first_letter = name[0].upper()
    soundex = first_letter

    count = 0
    last_digit = ''

    for char in name[1:].lower():
        if char in "aeiouyhw":
            continue

        digit = soundex_mapping.get(char, '')

        if digit == last_digit:
            continue

        if digit:
            soundex += digit
            last_digit = digit
            count += 1

        if count == 3:
            break

    return soundex.ljust(4, '0')

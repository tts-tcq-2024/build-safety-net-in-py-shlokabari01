def get_soundex_code(c):
    return {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }.get(c.upper(), '0')

def generate_soundex(name):
    if not name:
        return ""
    
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            if len(soundex) == 4:
                break
        prev_code = code

    return soundex.ljust(4, '0')

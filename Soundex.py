def get_soundex_code(input):
    input = input.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(input, '0')  # Default to '0' for non-mapped characters
 
def initialize_soundex(name):
    # Initialize the soundex code with the first letter
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)
 
def should_add_code(char, code, prev_code):
    return code != '0' and code != prev_code
 
def process_characters(name, soundex, prev_code):
    codes = [get_soundex_code(char) for char in name[1:] if should_add_code(char, get_soundex_code(char), prev_code)]
    return (soundex + ''.join(codes)[:3]).ljust(4, '0')
 
def pad_soundex(soundex):
    # Pad with zeros if necessary to ensure length is 4
    return soundex.ljust(4, '0')
 
def generate_soundex(name):
    if not name:
        return ""
 
    soundex, prev_code = initialize_soundex(name)
    soundex = process_characters(name, soundex, prev_code)
    return pad_soundex(soundex)

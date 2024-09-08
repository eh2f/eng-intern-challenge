import sys

alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'cap_follow': '.....O',
    'decimal_follow': '.O...O',
    'number_follow': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'space': '......'
}


def braille_to_english(braille_string):
    ret_str = ''
    cap_flag = False
    num_flag = False
    for index_braille in range(0, len(braille_string), 6):
        current_block = braille_string[index_braille:index_braille+6]
        # print(current_block)
        key_letter = [key for key, value in alphabet.items() if value == current_block]
        # key_letter = list(alphabet.keys())[list(alphabet.values()).index(current_block)]
        if 'space' == key_letter[0]:
            ret_str += ' '
            num_flag = False
        elif 'cap_follow' == key_letter[0]:
            cap_flag = True
        elif cap_flag:
            ret_str += key_letter[0].capitalize()
            cap_flag = False
        elif 'number_follow' == key_letter[0]:
            num_flag = True
        elif num_flag:
            ret_str += key_letter[-1]
        elif 'decimal_follow' == key_letter[0]:
            ret_str += '.'
        else:
            ret_str += key_letter[0]
    return ret_str


def english_to_braille(english_string):
    ret_str = ''
    for letter in english_string:
        # check for capital letter
        if letter.capitalize() == letter:
            ret_str += alphabet['cap_follow'] + alphabet[letter.lower()]
        # check for number
        elif letter.isdigit():
            # check for decimal point
            if len(ret_str) != 0 and ret_str[:-6] == alphabet['.']:
                ret_str[:-6] = alphabet['decimal_follow']
                ret_str += alphabet[letter]
            else:
                ret_str += alphabet['number_follow'] + alphabet[letter]
        else:
            ret_str += alphabet[letter]
    return ret_str


for i in sys.argv[1:]:
    i = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
    full = ''
    placeholder = "".join(set(i))
    if ('.' in placeholder and len(placeholder) == 1) or ('.' in placeholder and 'O' in placeholder):
        print(braille_to_english(i))
        full += braille_to_english(i)
    else:
        full += english_to_braille(i)


'''
Translating read ml text for finding json file with medicine info
'''


cyr_to_lat = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'ye',
    'ё': 'yo',
    'ж': 'zs',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
    ' ': ' '
}

num_to_cyr = {
    '0': 'о',
    '1': 'т',
    '2': '',
    '3': 'з',
    '4': 'ч',
    '5': '',
    '6': 'б',
    '7': 'л',
    '8': 'в',
    '9': ''
}


def number_to_cyrillic(text):
    new_text = ''
    for c in text:
        if '0' <= c <= '9':
            new_text += num_to_cyr[c]
        else:
            new_text += c
    return new_text


def cyrillic_to_latin(text):
    new_text = ''
    for c in text:
        if 'а' <= c <= 'я':
            new_text += cyr_to_lat[c]
        else:
            new_text += c
    return new_text


def create_file_name(text: str):
    text = text.lower()
    text = number_to_cyrillic(text)
    text = cyrillic_to_latin(text)

    text += '.json'

    return text


if __name__ == "__main__":
    s = input('Input a string in russian that needs to be translated: ')
    print(f'cyrillic_to_latin output: {cyrillic_to_latin(s)}')
    print(f'number_to_cyrillic output: {number_to_cyrillic(s)}')
    print(f'create_file_name output: {create_file_name(s)}')
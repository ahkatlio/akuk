akuk_dict = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5',
    'k': '6',
    'c': '7',
    't': '8',
    'p': '9',
    'l': '0',
    'h': '.',
    ' ':' '
}

def akuk_to_num(text):
    
    num = ''
    decimal_point = False
    for char in text:
        if char == '.':
            decimal_point = True
        elif char in akuk_dict:
            num += akuk_dict[char]
            if decimal_point:
                num = num[:-1] + '.' + num[-1:]
                decimal_point = False
        else:
            return 'Invalid character: ' + char
    return num
def num_to_akuk(num):
    num_str = str(num)
    akuk = ''
    for digit in num_str:
        for char, val in akuk_dict.items():
            if val == digit:
                akuk += char
                break
    return akuk

tt = input('text')
print(num_to_akuk(tt)) 
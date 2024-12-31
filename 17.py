map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}


def number_to_word(num):
    num_str = str(num)
    word = ''
    if num == 100:
        word = 'onehundred'
    elif num == 1000:
        word = 'onethousand'
    elif num in map:
        word = map[num]
    elif len(num_str) == 3:
        word = map[int(num_str[0])] + 'hundred'
        if int(num_str[1:]) in map:
            word += 'and' +  map[int(num_str[1:])]
        elif int(num_str[1]) != 0:
            word += 'and' + map[int(num_str[1]) * 10] + map[int(num_str[2])]
    else:
        word = map[int(num_str[0]) * 10] + map[int(num_str[1])]

    return word

count = 0
for i in range(1, 1001):
    count += len(number_to_word(i))

print(count)
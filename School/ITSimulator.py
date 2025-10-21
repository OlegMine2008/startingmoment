# Шифровка
def cyphr(word, ways_vars=3, ways=[2, 3, 4]):
    alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
    new_word = ''
    i = 0
    for let in word:
        if let in alphabet and (ways[i] + alphabet.index(let)) <= len(alphabet) - 1:
            new_word += alphabet[alphabet.index(let) + ways[i]]
        elif let in alphabet and (ways[i] + alphabet.index(let)) > len(alphabet) - 1:
            new_word += alphabet[alphabet.index(let) + ways[i] - len(alphabet)]
        else:
            new_word += let
        if i + 1 > ways_vars - 1:
            i = 0
        else:
            i += 1
    return new_word


# Счёт частотности
def chast(word):
    result = {}
    alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
    for let in word:
        if let in alphabet:
            result[let] = result.get(let, 0) + 1
    return result


# Расшифровка
# def recyphr(hidden, most_letter):
#     meets = {}
#     alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
#     for let in hidden:
#         if let in alphabet:
#             meets[let] = meets.get(let, 0) + 1
    
#     need = max(meets.items(), key=lambda x: x[1])
#     ways = (alphabet.index(most_letter) - alphabet.index(need[0])) % len(alphabet)
#     retranclate = [alphabet[i - ways] if i - ways >= 0 else alphabet[(i - ways) + len(alphabet)] for i in range(len(alphabet))]
#     new_word = ''
#     for let in hidden:
#         if let in alphabet:
#             new_word += alphabet[retranclate.index(let)]
#         else:
#             new_word += let
#     return new_word



# word = input('words: ')
# most_seen = input('lets: ')

answer1 = cyphr(word='но стоит ли ради этого подыматься?')
print(answer1)

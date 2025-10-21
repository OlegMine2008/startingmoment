from ITSimulator import cyphr


with open('D:/MyNewWork/School/test.txt', 'r', encoding='utf-8') as alice:
    answer = ''
    inputed = int(input())
    ways = [int(input()) for _ in range(inputed)]
    for line in alice.readlines():
        result = cyphr(line, ways_vars=inputed)
        answer += result + '\n'
        letters = {}
    numero = 0
    asd = 0
    alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
    for finde in answer:
        for let in finde:
            if let.isalpha():
                asd += 1
            if let.isalpha() and let.lower() in alphabet:
                letters[let.lower()] = letters.get(let.lower(), 0) + 1
                numero += 1


letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
for letter in letters:
    answe = round((letters[letter] / numero) * 100, 2)
    print(letter, '\t', answe, '%')







# with open('D:/MyNewWork/School/alice.txt', 'r', encoding='utf-8') as alice:
#     letters = {}
#     numero = 0
#     asd = 0
#     alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
#     for line in alice.readlines():
#         for let in line:
#             if let.isalpha():
#                 asd += 1
#             if let.isalpha() and let.lower() in alphabet:
#                 letters[let.lower()] = letters.get(let.lower(), 0) + 1
#                 numero += 1

# print(asd)
# print(numero)
# letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
# for letter in letters:
#     answe = round((letters[letter] / numero) * 100, 2)
#     print(letter, '\t', answe, '%')
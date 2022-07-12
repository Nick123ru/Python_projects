'''Программа написана в рамках изучения курса "Поколение Python": курс для начинающих'''

def caesar(lng, txt, n):
    for symbol in txt:
            if not symbol.isalpha():
                print(symbol, end = '')
            elif symbol.isupper():
                s = lng.upper().index(symbol) + n
                if s >= 0:
                    if s > len(lng) - 1:
                        print(lng[s - len(lng)].upper(), end= '')
                    else:
                        print(lng[s].upper(), end = '')
                else:
                    print(lng[s + len(lng)].upper(), end = '')
            elif symbol.islower():
                s = lng.index(symbol) + n
                if s >= 0:
                    if s > len(lng) - 1:
                        print(lng[s - len(lng)], end= '')
                    else:
                        print(lng[s], end= '')
                else:
                    print(lng[s + len(lng)], end= '')
                
language, text, n = int(input('Язык (0 - ru; 1 - en): ')), input('Введите текст: '), input('Для шифрования: n > 0 или len; Для дешифрования: если известен сдвиг n < 0, если нет - n\nСдвиг: ')

if language == 0:
    language = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
elif language == 1:
    language = 'abcdefghijklmnopqrstuvwxyz'

if n.isdigit():
    n = int(n)
    caesar(language, text, n)
elif n == 'n':
    for i in range(len(language) - 1):
        n = i + 1
        caesar(language, text, -n)
        print()
elif n == 'len':
     words = text.split()
     for word in words:
        len_word = word
        if not len_word.isalpha():
            for i in '.,!"':
                len_word = len_word.replace(i, '')
        caesar(language, word, len(len_word))
        print(end = ' ')
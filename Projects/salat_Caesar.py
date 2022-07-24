from string import ascii_lowercase, ascii_uppercase, digits, punctuation

info = ('Для шифрования текста введите число (n > 0) или "len" для шифрования на длину слова.\n'
        'Для дешифрования: если известен сдвиг введите число (n < 0) или "-len", если нет - "n"\n'
        'Важно: если укажите число больше длины алфавита - вернется исходный текст')


def caesar(text: str, step: int) -> str:  # (Де)Шифратор
    rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabets = (ascii_lowercase, ascii_uppercase, rus, rus.upper())

    def shift(alphabet: str) -> str:  # Создание алфавита для сдвига
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)


def encrypting(text: str, mode: str) -> None:
    match mode:  # данная функция проверяет какой режим выбрал пользователь и сама вызывает необходимые функции
        case 'n':
            if all(map(lambda x: x.strip(punctuation + digits).lower()[0] in ascii_lowercase, text.split())):
                [print(caesar(text, i)) for i in range(1, 26)]
            else:
                [print(caesar(text, i)) for i in range(1, 32)]
        case 'len' | '-len':

            def word_len(word: str) -> str:
                return str(len(word.strip(punctuation + digits)))

            print(*map(lambda x: caesar(x, int(mode.strip('len') + word_len(x))), text.split()))
            # for word in text.split():  # не определился как мне больше нравится
            #    print(caesar(word, int(mode.strip('len') + word_len(word))), end=' ')
        case _:
            print(caesar(text, int(mode)))


def main(text: str = None) -> None:
    # text = 'a аа aaa'
    if not text:
        text = str(input('Введите текст: '))
        print(info)
    mode = input('Что будем делать с текстом: ')
    try:
        if mode in ('len', '-len', 'n') or isinstance(int(mode), int):
            encrypting(text, mode)
        else:
            main(text)
    except ValueError as e:
        print(e)
        main(text)


if __name__ == '__main__':
    main()
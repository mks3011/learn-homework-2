"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    with open('referat.txt', 'r', encoding='utf-8') as ref:
        # Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
        referat = ref.read()
        print(referat)
        print(len(referat))

        # Подсчитайте количество слов в тексте
        words = referat.split()
        print(len(words))

        # Замените точки в тексте на восклицательные знаки
        new_referat = referat.replace(".", "!")
        print(new_referat)

        # Сохраните результат в файл referat2.txt
    with open('referat2.txt', 'w', encoding='utf-8') as ref2:
        ref2.write(new_referat)


if __name__ == "__main__":
    main()

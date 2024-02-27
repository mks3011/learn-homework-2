"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    print("Сегодня", today.strftime('%d.%m.%Y'))

    yesterday = today - timedelta(days=1)
    print("Вчера", yesterday.strftime('%d.%m.%Y'))

    days_before_30 = today - timedelta(days=30)
    print("30 дней назад", days_before_30.strftime('%d.%m.%Y'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

personnel_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 38, 'job': 'Programmer'},
        {'name': 'Коля', 'age': 42, 'job': 'Team leader'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('export.csv', 'w', newline='') as raw:
        fields = ['name', 'age', 'job']
        team = csv.DictWriter(raw, fields, delimiter=';')
        team.writeheader()

        for worker in personnel_list:
            team.writerow(worker)


if __name__ == "__main__":
    main()

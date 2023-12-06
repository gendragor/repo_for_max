"""Гипотеза Коллатца"""


def syracuse_sequence(number):
    """Функция возвращает список, представляющий из себя сиракузскую
    последовательность для заданного числа"""

    number = number
    number_list = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
            number_list.append(number)
        else:
            number = number * 3 + 1
            number_list.append(number)
    return number_list


def syracuse_max(number_list):
    """Функция возращает наибольшее число
    в сиракузской последовательности заданного числа"""

    number_max = 0
    for elem_list in number_list:
        if elem_list > number_max:
            number_max = elem_list
    return number_max


while True:
    print('<<<<<<<<<<<<<<<МЕНЮ>>>>>>>>>>>>>>> \n'
          'Введите команду 1: Запуск программы \n'
          'Введите команду 2: Выход из программы \n')
    command = input('Введите команду: ')
    if command == '1':
        while True:
            try:
                number_input = int(input('Введите целое положительное '
                                         'число: '))
                if number_input == 0 or isinstance(number_input, float):
                    raise ValueError
            except ValueError:
                print('\n ОШИБКА \n'
                      'Нужно ввести целое положительное число \n')
                continue
            break
        print('\n'
              'Сиракузская последовательность для заданного числа числа:')
        print(*syracuse_sequence(number_input))
        print(f'Наибольшее число в последовательности: \n \n'
              f'{syracuse_max(syracuse_sequence(number_input))}')
    elif command == '2':
        print('>ВЫ ВЫШЛИ ИЗ ПРОГРАММЫ<')
        break
    else:
        print('\n'
              'Неправильная команда')

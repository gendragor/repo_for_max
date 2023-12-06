"""Гипотеза Коллатца"""


def syracuse_sequence(number):
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


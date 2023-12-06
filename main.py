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


def syracuse_max(number_list):
    number_max = 0
    for elem_list in number_list:
        if elem_list > number_max:
            number_max = elem_list
    return number_max


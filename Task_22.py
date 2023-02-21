# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

def create_number(phrase):
    number = int(input(phrase))
    return number


def create_array(num, a):
    collect = list(range(num))
    for i in range(len(collect)):
        collect[i] = int(input(f"Введите {i + 1} элемент {a}-го множества: "))
    return collect


def find_numbers(col1, col2):
    fir_set = set(col1)
    sec_set = set(col2)
    main_set = fir_set.intersection(sec_set)
    main_list = list(main_set)
    main_list.sort()

    print(main_list)


num_one = int(create_number("Введите колличество элементов 1-го множества: "))
num_two = int(create_number("Введите колличество элементов 2-го множества: "))

collect1 = create_array(num_one, 1)
collect2 = create_array(num_two, 2)

find_numbers(collect1, collect2)

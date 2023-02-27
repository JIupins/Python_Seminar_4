# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
# система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль
# за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу
# для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной
# во входном файле грядки.

from random import randint


def create_number(phrase):
    num2 = int(input(phrase))
    return num2


def create_collect(num3):
    coll2 = list(range(num3))
    for i in range(len(coll2)):
        coll2[i] = randint(1, 10)
    return coll2


def show_quantity_of_berrys(coll3):
    for i in range(len(coll3)):
        print(f"На {i + 1}-м кусте выросло {coll3[i]} ягод.")


def find_quantity_of_berrys(coll4):
    num_bush = int(create_number(f"Введите номер куста (от 1 до {len(coll4)}), перед которым находится собирающий модуль: "))
    while num_bush <= 0 or num_bush > len(coll4):
        num_bush = int(create_number(f"Номер куста указан неверно, введите номер куста (от 1 до {len(coll4)}): "))
    if num_bush == len(coll4):
        sum_berrys = coll4[num_bush - 1] + (coll4[num_bush - 2] + coll4[0])
    else:
        sum_berrys = coll4[num_bush - 1] + (coll4[num_bush - 2] + coll4[num_bush])
    print(f"Находясь перед {num_bush} кустом собирающий модуль соберет {sum_berrys} ягод.")


num1 = int(create_number("Введите колличество кустов, посаженных на круглой грядке: "))

coll1 = create_collect(num1)

show_quantity_of_berrys(coll1)

find_quantity_of_berrys(coll1)

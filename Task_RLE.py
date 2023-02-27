# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где для упрощения в качестве кодируемой\декодитуемой
# информации используются символы). Например: qqwwwerrrrrtt -> 2q3w1e5r2t.

def coding(str1):
    count = 0
    quant = 0
    str2 = ""
    while count < len(str1):
        quant = 1
        while (count + 1) < len(str1) and str1[count] == str1[count + 1]:
            quant += 1
            count += 1
        str2 += str(quant) + str1[count]
        count += 1
    print(f"Исходная строка кодирована (сжата): {str2}")
    return str2


def decoding(str3):
    count = ""
    str4 = ""
    for i in str3:
        if i.isdigit():
            count += i
        else:
            str4 += i * int(count)
            count = ""
    print(f"Исходная строка декодирована (восcтановлена): {str4}")


str_main = input("Введите символы подлежащие кодированию (сжатию): ")
decoding(coding(str_main))

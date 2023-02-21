def zadacha_47(num_columns, num_rows):
    from random import randint

    array = [[randint(-9, 9) for i in range(num_columns)]
             for i in range(num_rows)]

    for i in range(num_rows):
        print(array[i])


def zadacha_50():
    pass


def zadacha_52():
    pass


zadacha_47(3, 5)
zadacha_50()
zadacha_52()
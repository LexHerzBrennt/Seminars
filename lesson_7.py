def zadacha_47(num_columns: int, num_rows: int):
    print('Zadacha 47:')

    from random import randint
    array = [[randint(0, 9) for i in range(num_columns)]
             for i in range(num_rows)]

    for i in range(num_rows):
        print(array[i])


def zadacha_50(array: list, row_index: int, column_index: int):
    print('Zadacha 50:')

    if row_index in range(len(array)) and column_index in range(len(array[0])):
        for i in range(len(array)):
            print(array[i])
        print(f'Element ({row_index}, {column_index}): {array[row_index][column_index]}')
    else:
        raise IndexError


def zadacha_52(array):
    print('Zadacha 52:')

    for i in range(len(array)):
        print(array[i])

    for i in range(len(array)):
        arith_mean = sum(array[i]) / len(array[i])
        print(f'Arithmetic mean of {i + 1} row: {arith_mean}')


from random import randint
array = [[randint(0, 9) for i in range(4)]
         for i in range(4)]

zadacha_47(4, 3)
zadacha_50(array, 3, 2)
zadacha_52(array)
def zadacha_47(num_columns: int, num_rows: int):
    from random import randint

    array = [[randint(1, 9) for i in range(num_columns)]
             for i in range(num_rows)]

    for i in range(num_rows):
        print(array[i])


def zadacha_50(array: list, row_index: int, column_index: int):
    if row_index in range(len(array)) and column_index in range(len(array[0])):
        for i in range(len(array)):
            print(array[i])

        print(array[row_index][column_index])
    else:
        raise IndexError

def zadacha_52():
    pass


from random import randint
array = [[randint(0, 9) for i in range(4)]
         for i in range(4)]

zadacha_47(3, 5)
zadacha_50(array, 3, 2)
zadacha_52()
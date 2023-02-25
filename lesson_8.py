def zadacha_54(columns: int, rows: int):
    print('Zadacha 54:')

    from random import randint
    array = [[randint(0, 9) for i in range(columns)] for i in range(rows)]

    for i in range(rows):
        print(array[i])

    for i in range(rows):
        for j in range(columns - 1):
            for k in range(columns - 1):
                if array[i][k] < array[i][k+1]:
                    array[i][k], array[i][k+1] = array[i][k+1], array[i][k]

    print('Sorted:')
    for i in range(rows):
        print(array[i])


def zadacha_56(columns: int, rows: int):
    print('Zadacha 56:')

    from random import randint
    array = [[randint(0, 9) for i in range(columns)] for i in range(rows)]

    for i in range(rows):
        print(array[i])

    max_sum = 0
    max_row = 0
    for i in range(len(array)):
        if max_sum < sum(array[i]):
            max_sum = sum(array[i])
            max_row = i

    print(f'Result: {max_sum} (index of row: {max_row})')


zadacha_54(5, 4)
zadacha_56(5, 4)
def zadacha_34():
    from random import randint

    array = [randint(100, 999) for i in range(5)]
    count = 0

    for i in array:
        if i % 2 == 0:
            count += 1

    print('Zadacha 34:', array, f'(Even numbers: {count})')

def zadacha_36():
    from random import randint

    array = [randint(1, 99) for i in range(5)]
    sum = 0

    #The loop sums a numbers on even INDEXES
    for i in range(5):
        if i % 2 == 0:
            sum += array[i]

    print('Zadacha 34:', array, f'(Sum: {sum})')

zadacha_34()
zadacha_36()
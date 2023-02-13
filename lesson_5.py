def zadacha_34():
    from random import randint

    array = [randint(100, 999) for i in range(5)]
    count = 0

    for i in array:
        if i % 2 == 0:
            count += 1

    print('Zadacha 34:', array, f'({count} even numbers)')

zadacha_34()
def zadacha_41():
    print('Zadacha 41:')

    count = 0
    for i in range(5):
        num = int(input(f'Enter {i} number: '))
        if num > 0:
            count += 1

    print(f'You\'ve entered {count} numbers greater than 0')

zadacha_41()
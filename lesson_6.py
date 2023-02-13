def zadacha_41():
    print('Zadacha 41:')

    count = 0
    for i in range(5):
        num = int(input(f'Enter {i} number: '))
        if num > 0:
            count += 1

    print(f'You\'ve entered {count} numbers greater than 0')


def zadacha_43():
    print('Zadacha 43:')

    b1 = int(input('b1: '))
    k1 = int(input('k1: '))
    b2 = int(input('b2: '))
    k2 = int(input('k2: '))

    x = (b2 - b1) / (k1 - k2)
    y = k1 * x + b1

    print(f'Coordinates: ({x};{y})')


zadacha_41()
zadacha_43()
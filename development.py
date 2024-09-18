
field = [[" "]*3 for i in range(3)]

def hi():
    print("  Крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print("-------------------")

def print_field():
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        print(f"{i} | {' | '.join(row)} |\n---------------")

def ask():
    while True:
        cords = input('         Ваш ход: ').split()

        if len(cords) != 2:
            print("Введите две координаты !")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа !')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Вне поля !")
            continue

        if field[x][y] != ' ':
            print('Занято !')
            continue

        return x, y

def check_win():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cords:
        symbols = []
        for i in cord:
            symbols.append(field[i[0]][i[1]])
            if symbols == ['X','X','X']:
                print("Выиграл X!!!")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл 0!!!")
                return True
    return False




field = [[" "]*3 for i in range(3)]


def print_field():
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        print(f"{i} | {' | '.join(row)} |\n---------------")



print_field()
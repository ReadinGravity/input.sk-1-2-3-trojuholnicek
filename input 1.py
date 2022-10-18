def obdlznicek(width, sym='x'):
    for i in range(width):
        print(sym, end='')
    print()
    print(sym, end='')
    for a in range(width-2):
        print(' ', end='')
    print(sym)
    for i in range(width):
        print(sym, end='')


obdlznicek(30)

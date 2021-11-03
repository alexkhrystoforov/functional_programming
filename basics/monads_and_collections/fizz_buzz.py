def f1(y: list) -> list:
    return list(map(lambda x: 'fizzbuzz' if isinstance(x, int) and x % 5 == 0 and x % 3 == 0 else x, y))


def f2(y: list) -> list:
    return list(map(lambda x: 'buzz' if isinstance(x, int) and x % 5 == 0 else x, y))


def f3(y: list) -> list:
    return list(map(lambda x: 'fizz' if isinstance(x, int) and x % 3 == 0 else x, y))

# инициализация
# def unit(e):
#     return e

# связующийкод
# def bind(e, f):
#     return None if e is None else f(e)


def pipeline(e, *func):
    for f in func:
        e = f(e)
    return e


if __name__ == '__main__':
    y = [x for x in range(1, 101)]
    print(pipeline(y, f1, f2, f3))
    # print(pipeline(unit(y), f1, f2, f3))
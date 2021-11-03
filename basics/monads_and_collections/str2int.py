def get_ints(y: list) -> list:
    return list(filter(lambda x: x.isdigit(), y))


def str_to_int(y: list) -> list:
    return list(map(int, y))


def pipeline(e, *func):
    for f in func:
        e = f(e)
    return e


if __name__ == '__main__':
    my_list = ['1', '2', 's', '4']
    print(pipeline(my_list, get_ints, str_to_int))
def str2char(x: list) -> list:
    return sum(list(map(lambda y: list(y), x)), [])


if __name__ == '__main__':
    my_list = ['abc', 'def', 'ghj']
    print(str2char(my_list))
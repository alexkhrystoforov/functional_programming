def separate(x: list, sep='\n') -> list:
    # find where the separator is situated
    q = list(map(lambda y: y.find(sep), x))
    u = list(filter(lambda x: x > 0, q))

    te = q.index(u[0])

    return list(map(lambda y: y if y.find(sep) == -1 else y[:y.find(sep)], x[:te+1]))


if __name__ == '__main__':
    my_list = ["Hello", "world!\n", "Test", "asda"]
    my_list1 = ["Hello", "world!\nTest", "asda"]
    print(separate(my_list))
    print(separate(my_list1))
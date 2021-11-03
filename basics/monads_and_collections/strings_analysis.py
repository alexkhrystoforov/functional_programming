def str_analysis(str_seq):
    d = {}
    # not functional approach

    for x in str_seq:
        if x[0] in d:
            d[x[0]].append(x)
        else:
            d[x[0]] = [x]

    d_quantity = dict(zip(d.keys(), map(lambda x: len(x), d.values())))

    return d, d_quantity


if __name__ == '__main__':
    d1, d2 = str_analysis(["ABCA", "BCD", "ABC"])
    print(d1)
    print(d2)
def sum_str(first, second):
    return [(a + b) for a, b in zip(first, second)]


def transform_str(prefix: list, core: list, suffix: list) -> list:
    return sum_str(sum_str(prefix, core), suffix)


if __name__ == '__main__':
    res = transform_str(["over", "extra"], ["size", "large"], ["d", ""])
    print(res)
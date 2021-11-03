from pure_func import pure_check, checking, checked
import random

@pure_check()
def increment(x: int):
    return x + 1


def test_increment1(x):
    with checking():
        return increment(x)


@checked()
def test_increment2(x):
    return increment(x)


if __name__ == '__main__':
    x = increment(5)
    print(x)
    x = test_increment1(5)
    print(x)
    x = test_increment2(5)
    print(x)

    y = random.randint(1,100)
    print(increment(y))
    print(increment(increment(y-1)))
    print(increment(y+1) - 1)

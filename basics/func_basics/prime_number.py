# 1st solution
def prime_num_checker(n, a=2):
    if type(n+a) == int and n > 0 and a > 0:
        if n // 2 < a:
            return True
        elif n % a == 0:
            return False
        return prime_num_checker(n, a + 1)
    else:
        return 'incorrect input'


# 2nd solution
def pr(n):

    def func3(a=2):
        if n % a == 0:
            return False
        else:
            return func2(a+1)

    def func2(a=2):
        if n // 2 < a:
            return True
        else:
            return func3(a)

    if type(n) == int and n > 0:
        return func2()
    else:
        return 'incorrect input'


# 3d solution
func3 = (lambda n, a: False if n % a == 0 else func2(n, a + 1))
func2 = (lambda n, a: True if n // 2 < a else func3(n, a))
func1 = (lambda n, a=2: func2(n, a) if type(n+a) == int and n > 0 else 'incorrect input')


if __name__ == '__main__':
    print(prime_num_checker(97))
    print(func1(97))
    print(pr(97))

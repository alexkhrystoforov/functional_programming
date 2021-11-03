factorial = (lambda x: 1 if x == 0 else x * factorial(x-1))

if __name__ == '__main__':
    print(factorial(5))

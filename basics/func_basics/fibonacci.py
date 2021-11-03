import time
import matplotlib.pyplot as plt


# lambda func

lambda_fibo = (lambda x: 1 if x < 3 else lambda_fibo(x-1) + lambda_fibo(x-2))


def plot_complexity(func):
    pr_time = []
    for i in range(30):
        start = time.process_time()
        func(i)
        stop = time.process_time()
        pr_time.append(stop - start)

    plt.plot([x for x in range(30)], pr_time, 'b')
    plt.xlabel('num of iter')
    plt.ylabel('time')
    plt.title('Complexity')
    plt.show()


# Memoization: create a dict to store caches values for not to re-evaluate the values
fibo_cache = {}

def get_fibo(x: int):
    if x in fibo_cache:
        return fibo_cache[x]

    if x > 0:
        if x < 3:
            fibo_cache[x] = 1
            return 1
        else:
            value = get_fibo(x - 1) + get_fibo(x - 2)
            fibo_cache[x] = value
            return value
    else:
        return 'your input is a string or <=0'


# implement tail recursion fibonacci

def fib(n):
    def fib_help(a, b, n):
        return fib_help(b, a + b, n - 1) if n > 0 else a
    return fib_help(0, 1, n)


if __name__ == '__main__':
    print(get_fibo(7))
    print(fibo_cache)
    print(fib(7))
    plot_complexity(fib)  # tail-recursion - O(n) complexity
    plot_complexity(lambda_fibo)  # looks like O(n^2)
    plot_complexity(get_fibo)  # looks like O(1) due to memoization

import time
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    print(get_fibo(40))
    print(fibo_cache)
    plot_complexity(get_fibo)

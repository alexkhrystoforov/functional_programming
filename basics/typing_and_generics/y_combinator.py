# only for 1 argument
Y = (lambda f: (lambda x: x(x))(lambda x: f(lambda *args: x(x)(*args))))
fact = (lambda f: lambda x:(1 if x == 1 else x * f(x-1)))

if __name__ == '__main__':
    print(Y(fact)(6))
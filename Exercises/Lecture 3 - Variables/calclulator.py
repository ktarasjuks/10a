def add(a, b):
    return a + b


def subs(a, b):
    print(a - b)


def mult(a, b):
    print(a * b)


def div(a, b):
    print(a / b)


if __name__ == '__main__':
    a = 3
    b = 1
    # print(a+b)
    print('The answer is ' + str(add(a, b)))
    subs(a, b)
    mult(a, b)
    div(a, b)

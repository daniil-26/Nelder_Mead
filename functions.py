from math import *


def rastrigin(args):
    return 10 * len(args) + sum([pow(arg, 2) - 10 * cos(2 * pi * arg) for arg in args])


def rosenbrock(args):
    return sum([100 * pow(args[i + 1] - pow(args[i], 2), 2) + pow(1 - args[i], 2) for i in range(len(args) - 1)])


def sphere(args):
    return sum([pow(arg, 2) for arg in args])


def ackley(args):
    x, y = args[0], args[1]
    return \
        -20 * exp(-0.2 * sqrt(0.5 * (pow(x, 2) + pow(y, 2)))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


def both(args):
    x, y = args[0], args[1]
    return pow(x + 2 * y - 7, 2) + pow(2 * x + y - 5, 2)


def levi(args):
    x, y = args[0], args[1]
    return pow(sin(3 * pi * x), 2)\
        + pow(x - 1, 2) * (1 + pow(sin(3 * pi * y), 2)) + pow(y - 1, 2) * (1 + pow(sin(2 * pi * y), 2))


def himmelblau(args):
    x, y = args[0], args[1]
    return pow(pow(x, 2) + y - 11, 2) + pow(x + pow(y, 2) - 7, 2)


def three_hump_camel(args):
    x, y = args[0], args[1]
    return 2 * pow(x, 2) - 1.05 * pow(x, 4) + pow(x, 6) / 6 + x * y + pow(y, 2)

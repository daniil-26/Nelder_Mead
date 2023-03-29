from nelder_mead import *
from functions import *


def main():
    a = NelderMead(function=rosenbrock, dimesion=5)
    a.algoritm(print_steps=True, print_result=True)


if __name__ == '__main__':
    main()

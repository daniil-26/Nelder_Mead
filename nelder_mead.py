import random


class NelderMead:

    def __init__(self,
                 function, dimesion=2, alfa=1, beta=0.5, gamma=2, min_proximity=0.001, max_steps=100000, simplex=None):
        self.function = function
        self.dimension = dimesion
        self.alfa, self.beta, self.gamma = alfa, beta, gamma
        self.min_proximity, self.max_steps = min_proximity, max_steps
        if simplex is None:
            random.seed()
            self.simplex = self.start_simplex()
        else:
            self.simplex = simplex
        self.x_l, self.x_g, self.x_h, self.x_c, self.x_r, self.x_e, self.x_s = [None] * 7
        self.f_l, self.f_g, self.f_h, self.f_r, self.f_e, self.f_s = [None] * 6

    def algoritm(self, print_steps=False, print_result=False):
        for i in range(self.max_steps):
            self.sort_simplex()
            self.x_c = center_of_mass(array=self.simplex[:-1])
            self.reflection()
            self.improvement_score()
            if print_steps:
                print(i, ')     x = ', self.x_l, '     f = ', self.f_l, sep='')
            self.simplex = self.simplex[:-1] + [self.x_h]
            if proximity(array=self.simplex) <= self.min_proximity:
                break
        if print_result:
            print('\nRESULT:     x = ', self.x_l, '     f = ', self.f_l, sep='')
        return self.x_l

    def start_simplex(self):
        return [self.random_point() for _ in range(self.dimension + 1)]

    def random_point(self):
        return [random.random() for _ in range(self.dimension)]

    def sort_simplex(self):
        self.simplex.sort(key=self.function)
        values = self.simplex[-1], self.simplex[-2], self.simplex[0]
        self.x_h, self.x_g, self.x_l = values
        self.f_h, self.f_g, self.f_l = [self.function(x) for x in values]

    def reflection(self):
        self.x_r = list(map(lambda c, h: (1 + self.alfa) * c - self.alfa * h, self.x_c, self.x_h))
        self.f_r = self.function(self.x_r)

    def improvement_score(self):
        if self.f_r < self.f_l:
            self.expansion()
            if self.f_e < self.f_r:
                self.x_h = self.x_e
                return
            if self.f_r < self.f_e:
                self.x_h = self.x_r
                return
        if self.f_l < self.f_r < self.f_g:
            self.x_h = self.x_r
            return
        if self.f_g < self.f_r < self.f_h:
            self.x_r, self.x_h = self.x_h, self.x_r
            self.f_r, self.f_h = self.f_h, self.f_r
        self.contraction()

    def expansion(self):
        self.x_e = list(map(lambda c, r: (1 - self.gamma) * c + self.gamma * r, self.x_c, self.x_r))
        self.f_e = self.function(self.x_e)

    def contraction(self):
        self.x_s = list(map(lambda c, h: (1 - self.beta) * c + self.beta * h, self.x_c, self.x_h))
        self.f_s = self.function(self.x_s)
        if self.f_s < self.f_h:
            self.x_h = self.x_s
        if self.f_h < self.f_s:
            self.global_contraction()

    def global_contraction(self):
        self.simplex = \
            [self.x_l] + \
            [list(map(lambda x, coordinate: x + (coordinate - x) / 2, self.x_l, point)) for point in self.simplex[1:]]


def center_of_mass(array):
    return [sum(x) / len(x) for x in transpose(array=array)]


def transpose(array):
    return [[x[i] for x in array] for i in range(len(array))] if len(array) else []


def proximity(array):
    return sum([l1_distance(a=array[i - 1], b=array[i]) for i in range(len(array))])


def l1_distance(a, b):
    return sum([abs(x - y) for x, y in zip(a, b)])

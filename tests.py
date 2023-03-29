import unittest
from nelder_mead import *
from functions import *


class Test(unittest.TestCase):

    accuracy = 0.001

    def test_rosenbrock(self):
        a = NelderMead(function=rosenbrock, dimesion=5)
        res = a.algoritm()
        self.assertTrue(all([abs(x - 1) < self.accuracy for x in res]))

    def test_sphere(self):
        a = NelderMead(function=sphere, dimesion=10)
        res = a.algoritm()
        self.assertTrue(all([abs(x) < self.accuracy for x in res]))

    def test_rastrigin_simplex(self):
        a = NelderMead(function=rastrigin, dimesion=3,
                       simplex=[[0.23, 0.80, 0.36], [0.09, 0.079, 0.19], [0.20, 0.54, 0.29], [0.69, 0.50, 0.72]])
        res = a.algoritm()
        self.assertTrue(all([abs(x) < self.accuracy for x in res]))

    def test_both(self):
        a = NelderMead(function=both)
        res = a.algoritm()
        self.assertTrue(all([(abs(x - value)) < self.accuracy for x, value in zip(res, [1, 3])]))

    def test_himmelblau(self):
        a = NelderMead(function=himmelblau)
        res = a.algoritm()
        self.assertTrue(abs(himmelblau(res)) < self.accuracy)

    def test_three_hump_camel(self):
        a = NelderMead(function=three_hump_camel)
        res = a.algoritm()
        self.assertTrue(all([abs(x) < self.accuracy for x in res]))

    def test_acley_simplex(self):
        a = NelderMead(function=ackley, simplex=[[0.1, 0.6], [0.3, 0.6], [0.2, 0.5]])
        res = a.algoritm()
        self.assertTrue(all([abs(x) < self.accuracy for x in res]))

    def test_levi_simplex(self):
        a = NelderMead(function=levi, simplex=[[0.94, 0.39], [0.93, 0.92], [0.81, 0.85]])
        res = a.algoritm()
        self.assertTrue(all([abs(x - 1) < self.accuracy for x in res]))

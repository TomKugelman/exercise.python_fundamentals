# Created by Leon Hunter at 9:54 AM 10/23/2020
import math


class Calculator(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if a <= 0 or b <= 0:
            return "ZeroDivisionError"
        return math.divide(a, b, 3)

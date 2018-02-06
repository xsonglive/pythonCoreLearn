# -*- coding: UTF8 -*-

# 计算象棋的安全数量
# https://py.checkio.org/mission/min-max/


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return "{0} / {1}".format(self.num, self.den)

    def __add__(self, other):
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        g = self.gcd(n, d)
        return Fraction(n // g, d // g)

    def __eq__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return n == d

    def gcd(self, m, n):
        if m < n:
            m, n = n, m
        if m % n == 0:
            return n
        return gcd(n, m % n)

if __name__ == '__main__':
    s1 = Fraction(2, 8)
    s2 = Fraction(1, 4)
    print s1 + s2
    print s1 == s2

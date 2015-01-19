__author__ = 'andrei'

import random as rd
import itertools
import numpy.linalg as lg


def generator(s, m, n):
    x = range(-s, s+1)
    z = [0]*n
    xs = list(x)
    y = itertools.product(xs, repeat=n)
    ys1 = [list(x) for x in list(y)]
    rd.shuffle(ys1)
    #rd.shuffle(ys1)
    if m == 1:
        ys = [list(y0) for y0 in ys1]
        #print(m)
        rd.shuffle(ys)
        #print(m, "shuffle\n")
    elif m == 2:
        ys2 = ys1[:]
        rd.shuffle(ys2)
        ys = ([x0, y0] for x0 in ys1 for y0 in ys2 if x0 != z and y0 != z)
        #print(m)
        #rd.shuffle(ys)
        #print(m, "shuffle\n")
    else:
        #print("in else\n")
        zs = generator(s, m-1, n)
        ys = (x0+[y0] for x0 in zs for y0 in ys1 if y0 != z)
        #rd.shuffle(ys)
    return ys


def selection(xs, r1, r2):
    i = 0
    for x in xs:
       #  print(i)
        i += 1
        if r1 <= lg.matrix_rank(x) <= r2 and (x[0] != x[1] != x[2] != x[3]) and (x[3] != x[0] != x[2]):
            print(x)
            yield x

xs0 = selection(generator(2, 4, 5), 2, 3)
xs1 = []
for j in range(10000):
    xs1.append(next(xs0))
print(xs1[:50])
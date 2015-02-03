__author__ = 'andrei'

from pylatex import Document, Table, Math, TikZ, Axis, \
    Plot, Figure, Package
from pylatex.numpy import Matrix
from pylatex.utils import italic, escape_latex

import random as rd
import itertools as it
import numpy.linalg as lg
import numpy as np


def generator(s, m, n):
    x = range(-s, s+1)
    z = [0]*n
    xs = list(x)
    y = it.product(xs, repeat=n)
    ys1 = [list(x) for x in list(y)]
    rd.shuffle(ys1)
    #rd.shuffle(ys1)
    if m == 1:
        ys = [list(y0) for y0 in ys1]
        #print(m)
        #rd.shuffle(ys)
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


def column(a, i):
    y = [lin[i] for lin in a]
    return y


def selection(xs, r1, r2):
    i = 0
    z = [0]*3
    for x in xs:
        bo = True
        for j in range(len(x[0])):
            bo = bo and (column(x, j) != z)
        if r1 <= lg.matrix_rank(x) <= r2 and (x[0] != x[1] != x[2]) and (x[0] != x[2]) and bo:
            print(i)
            i += 1
            #print(x)
            yield x


xs0 = selection(generator(3, 3, 4), 2, 2)
xs=[]
for j in range(100000):
    xs.append(next(xs0))
rd.shuffle(xs)
rd.shuffle(xs)
xs1 = xs[:80]
ys = ["2x_1^2+5x_2^2+2x_3^2-4x_1x_2-2x_1x_3+4x_2x_3", "x_1^2+5x_2^2+x_3^2+2x_1x_2+6x_1x_3+2x_2x_3",
      "x_1^2-2x_2^2+x_3^2+4x_1x_2-10x_1x_3+4x_2x_3"]
yi = it.cycle(ys)
doc = Document(title="Probleme", author=" ", date=" ")
doc.packages.append(Package('nopageno'))
doc.packages.append(Package('fontspec'))
doc.packages.append(Package('amsmath'))
doc.packages.append(Package('amsfonts'))
doc.packages.append(Package('amssymb'))
for x in xs1:
    M = np.matrix(x)
    doc.append(r"\begin{flushright}")
    doc.append("Nume:\_\_\_\_\_\_\_\_\_\_\_\_\_\_")
    doc.append(" ")
    doc.append(" ")
    doc.append("Grupa:\_\_\_\_\_\_\_\_\_\_\_\_\_\_")
    doc.append("\end{flushright}")
    doc.append(r"\begin{center}")
    doc.append(r"\vspace{2cm}")
    doc.append("{\Large Probleme}")
    doc.append(r"\vspace{2cm}")
    doc.append(r"\end{center}")
    doc.append(r"\begin{enumerate}")
    doc.append(r" \item Fie morfismul $f:\mathbb{R}^4 \to \mathbb{R}^3$ a cărui matrice în raport cu bazele canonice este")
    doc.append(Math(data=[Matrix(M)]))
    doc.append(r"\begin{enumerate}")
    doc.append(r"\item Determinați cîte o bază în $Ker(f)$ și $Im(f)$;")
    doc.append(r"\item Fie vectorul $v=(1,3,1,3)$ determinați descompunerea acestuia ca suma dintre un vector din $Ker(f)$ și unul din $(Ker(f))^\perp$;")
    doc.append(r"\item Fie $K$ un corp și fie $L=M_n(K)$. Există $X,Y \in L$ astfel încît $XY-YX=I_n$?  ")
    doc.append("\end{enumerate}")
    doc.append(r"\item Fie forma pătratică:")
    doc.append(Math(data=["Q=", next(yi)]))
    doc.append(r"\begin{enumerate}")
    doc.append("\item Aduceți forma pătratică la forma canonică prin metoda Gauss;")
    doc.append("\item Aduceți forma pătratică la forma canonică prin transformări ortogonale;")
    doc.append(r"\item Fie $\mathfrak{su}(n)=\{ A \in M_n(\mathbb{C}) | A+\bar{A}^t=0\}$. Arătați că $\mathfrak{su}(n)$ este spațiu vectorial real, dar nu complex.")
    doc.append("Determinați $dim_{\mathbb{R}}\mathfrak{su}(n)$.")
    doc.append("\end{enumerate}")
    doc.append("\end{enumerate}")
    doc.append(r"\newpage")
doc.generate_tex()

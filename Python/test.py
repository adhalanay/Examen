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


def selection(xs, r1, r2):
    i = 0
    for x in xs:
       #  print(i)
        i += 1
        if r1 <= lg.matrix_rank(x) <= r2 and (x[0] != x[1] != x[2] != x[3]) and (x[3] != x[0] != x[2]):
            print(x)
            yield x


xs0 = selection(generator(2, 4, 5), 2, 3)
xs=[]
for j in range(100000):
    xs.append(next(xs0))
rd.shuffle(xs)
rd.shuffle(xs)
xs1 = xs[:50]
ys = ["2x_1^2+5x_2^2+2x_3^2-4x_1x_2-2x_1x_3+4x_2x_3", "-x_1^2+x_2^2-5x_3^2+3x_1x_3+4x_2x_3",
      "x_1^2+5x_2^2+x_3^2+2x_1x_2+6X_1x_3+2x_2x_3", "x_1^2-2x_2^2+x_3^2+4x_1x_2-10x_1x_3+4x_2x_3"]
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
    doc.append(r" \item Fie morfismul $f:\mathbb{R}^5 \to \mathbb{R}^4$ al cărui matrice în raport cu bazele canonice este")
    doc.append(Math(data=[Matrix(M)]))
    doc.append(r"\begin{enumerate}")
    doc.append(r"\item Determinați cîte o bază în $Ker(f)$ și $Im(f)$;")
    doc.append(r"\item Fie vectorul $v=(1,3,1,3)$ determinați descompunerea acestuia ca suma dintre un vector din $Im(f)$ și unul din $Im(f)^\perp$;")
    doc.append(r"\item Fie $K$ un corp și fie $L=M_n(K)$. Arătați că pentru orice funcțională $f \in L^*$ există o matrice $A$ astfel încît $f(X)=Tr(AX)$;")
    doc.append("\end{enumerate}")
    doc.append(r"\item Fie forma pătratică:")
    doc.append(Math(data=["Q=", next(yi)]))
    doc.append(r"\begin{enumerate}")
    doc.append("\item Aduceți forma pătratică la forma canonică prin metoda Gauss;")
    doc.append("\item Aduceți forma pătratică la forma canonică prin transformări ortogonale;")
    doc.append("\item Determinați forma biliniară simetrică $B$ asociată lui $Q$ și calculați dimensiunea subspațiului")
    doc.append(Math(data=[r"\{x \in \mathbb{R}^3 | B(x,y)=0,\forall y \in \mathbb{R}^3\}."]))
    doc.append("\end{enumerate}")
    doc.append("\end{enumerate}")
    doc.append(r"\newpage")
doc.generate_tex()
doc.generate_pdf()
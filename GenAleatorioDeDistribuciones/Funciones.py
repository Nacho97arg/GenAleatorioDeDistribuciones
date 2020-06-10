import numpy as np
import Generador as gn
import math as mt

def Uniforme (a, b, x):
    nros = gn.ranGen().randGCL(15, 100)
    for r in nros:
        x.append(a + (b - a) * r)
    
def Exponencial(ex, x):
    nros = gn.ranGen().randGCL(15, 100)
    for r in nros:
        x.append((-ex) * np.log(r))
    
def Gamma(k, a, x):
    for i in range(0, 100):    
        tr = 1.0
        r = gn.ranGen().randGCL(15 + i, k)
        for j in range(0, k):
            tr = tr * r[j]
        x.append(-(np.log(tr))/a)
    
def Normal(ex, stdx, x):
    for i in range(0, 100):
        sum = 0
        r = gn.ranGen().randGCL(15 + i, 12)
        for j in range(0, 12):
            sum = sum + r[j]
        x.append(stdx * (sum - 6) + ex)
    
def Pascal (k, q, x):
    qr = np.log(q)
    for i in range (0, 100):
        r = gn.ranGen().randGCL(15 + i, k)
        for j in range (0, k):
            tr = 1
            tr = tr * r[j]
        nx = np.log(tr) / qr
        x.append(nx)
    
def Binomial(n, p, x):
    for i in range(0, 100):
        cont = 0
        r = gn.ranGen().randGCL(15 + i, n)
        for j in range(0, n):
            if (r[j] > p):
                cont += 1
        x.append(cont)
    
def HiperGeometrica (tn, ns, p, x):
    for i in range(0, 100):
        TN = tn
        cont = 0
        r = gn.ranGen().randGCL(15 + i, ns)
        for j in range(0, ns):
            if (r[j] > p):
                s = 0
            else:
                s = 1
                cont += 1
            p = (TN * p - s) / (TN - 1)
            TN = TN - 1
        x.append(cont)

def Poisson (p, x):
    r = gn.ranGen().randGCL(15, 10000)
    j = 0
    b = mt.exp(-p)
    for i in range(0, 100):
        cont = 0
        tr = 1
        while(tr >= b):
            tr = tr * r[j]
            cont += 1
            j += 1
        j += 1
        x.append(cont)

###Esto todavia no esta testeado

def Markov(p, m, n, i, x):
    r = gn.ranGen().randGCL(15, n)
    for k in range(0, m):
        x.append(0)
    for l in range(0, n):
        for j in range(0, m):
            if ((p[i][j] - r[l]) >= 0):
                i = j
                x[i] = x[i] + 1
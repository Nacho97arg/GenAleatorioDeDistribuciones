import numpy as np
import matplotlib.pylab as pp

class Graficas:
    def grafHist(cls, val, dist,n_bar=75, axis=[-0.0625, 1.0625, 0, 350], autoscale=False, normalized=False, stacked=False):
        pp.hist(val,n_bar,label=['Propia','Numpy'],density=normalized,stacked=stacked)#,facecolor='g')
        pp.grid(True)
        pp.legend()
        pp.xlabel('Valor de la VA')
        pp.ylabel('Repeticiones')
        pp.title('Distribucion '+dist)
        if not autoscale:
            pp.axis(axis)
        pp.show()



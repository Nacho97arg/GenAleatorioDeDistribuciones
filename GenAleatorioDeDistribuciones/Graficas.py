import numpy as np
import matplotlib.pylab as pp

class Graficas:
    def grafHist(cls, val, dist, axis=[-0.0625, 1.0625, 0, 350], autoscale=False, normalized=False, stacked=False):
        pp.hist(val,75,label=['Propia','Numpy'],density=normalized,stacked=stacked)#,facecolor='g')
        pp.grid(True)
        pp.legend()
        pp.xlabel('Valor de la VA')
        pp.ylabel('Repeticiones')
        pp.title('Distribucion '+dist)
        if not autoscale:
            pp.axis(axis)
        pp.show()



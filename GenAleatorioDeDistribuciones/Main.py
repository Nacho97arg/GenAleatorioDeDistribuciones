import Funciones as fn
import Graficas as grf
import numpy.random as ran

dist_uniforme = []
dist_exponencial = []
dist_gamma = []
dist_normal = [] 
dist_pascal = []
dist_binomial = []
dist_hiper_geometrica = []
dist_poisson = []

fn.Uniforme(0, 1, dist_uniforme)
fn.Exponencial(0.12, dist_exponencial)
fn.Gamma(8, 0.05, dist_gamma)
fn.Normal(0, 1, dist_normal)
fn.Pascal(4, 0.01, dist_pascal)
fn.Binomial(100, 0.5, dist_binomial)
fn.HiperGeometrica(500, 100, 0.40, dist_hiper_geometrica)
fn.Poisson(1, dist_poisson)

grf.Graficas.grafHist = classmethod(grf.Graficas.grafHist)

grf.Graficas.grafHist([dist_uniforme,ran.uniform(size=10000)],'Uniforme')
grf.Graficas.grafHist([dist_exponencial,ran.exponential(scale=0.12,size=10000)], 'Exponencial', axis=[-0.0625, 1.0625, 0, 1000])
grf.Graficas.grafHist([dist_normal,ran.normal(loc=0,scale=1,size=10000)], 'Normal', autoscale=True)

grf.Graficas.grafHist([dist_binomial,ran.binomial(n=100,p=0.5,size=10000)], 'Binomial',n_bar=20, autoscale=True)
grf.Graficas.grafHist([dist_poisson,ran.poisson(lam=1,size=1000)], 'Poisson',n_bar=20, autoscale=True)


for i in dist_pascal:
    print(i)
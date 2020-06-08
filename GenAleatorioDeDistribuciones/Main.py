import Funciones as fn

dist_uniforme = []
dist_exponencial = []
dist_gamma = []
dist_normal = [] 
dist_pascal = []
dist_binomial = []
dist_hiper_geometrica = []
dist_poisson = []

fn.Uniforme(0, 1, dist_uniforme)
fn.Exponencial(0.05, dist_exponencial)
fn.Gamma(8, 0.05, dist_gamma)
fn.Normal(0, 1, dist_normal)
fn.Pascal(4, 0.01, dist_pascal)
fn.Binomial(100, 0.5, dist_binomial)
fn.HiperGeometrica(500, 100, 0.40, dist_hiper_geometrica)
fn.Poisson(0.05, dist_poisson)

for i in dist_pascal:
    print(i)
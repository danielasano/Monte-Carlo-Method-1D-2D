from random import*
import numpy as np
from math import*
import pandas as pd
np.random.seed(132)
a = -1
b = 1
n1 = 10
n2 = 100
n3 = 1000
n4 = 10000

l1 = [np.random.uniform(a,b) for i in range (0,n1)]
l2 = [np.random.uniform(a,b) for i in range (0,n2)]
l3 = [np.random.uniform(a,b) for i in range (0,n3)]
l4 = [np.random.uniform(a,b) for i in range (0,n4)]

j = []
k = []
l = []
m = []
def g(x):
    return np.exp((-x**2)/2)/np.sqrt(2*3.14)

j = [g(i) for i in l1]
k = [g(i) for i in l2]
l = [g(i) for i in l3]
m = [g(i) for i in l4]
    
I_n1 = sum(j)/len(j)*(fabs(b-a))
I_n2 = sum(k)/len(k) * (fabs(b-a))
I_n3 = sum(l)/len(l) * (fabs(b-a))
I_n4 = sum(m)/len(m) * (fabs(b-a))
print(f"Integral para {n1} amostras = {I_n1}")
print(f"Integral para {n2} amostras = {I_n2}")
print(f"Integral para {n3} amostras = {I_n3}")
print(f"Integral para {n4} amostras = {I_n4}")

I_v = 0.6827
MC = pd.DataFrame({'n':[n1,n2,n3,n4], 'Integral':[I_n1,I_n2,I_n3,I_n4], 'Erro':[fabs(I_v-I_n1),fabs(I_v-I_n2),fabs(I_v-I_n3),fabs(I_v-I_n4)]})
print(MC)

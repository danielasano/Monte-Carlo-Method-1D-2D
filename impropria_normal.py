from random import*
import numpy as np
from math import*
import pandas as pd
np.random.seed(132)

def g(x):
    return np.exp((-x**2)/2)/np.sqrt(2*3.14)

def h(y):
  return (g(1/y - 1))/y**2

a = 0
b = 1
n1 = 10
n2 = 100
n3 = 1000
n4 = 10000

l1 = [np.random.uniform(a,b) for i in range(0,n1)]
l2 = [np.random.uniform(a,b) for i in range(0,n2)]
l3 = [np.random.uniform(a,b) for i in range(0,n3)]
l4 = [np.random.uniform(a,b) for i in range(0,n4)]

m1 = [h(n) for n in l1]
m2 = [h(n) for n in l2]
m3 = [h(n) for n in l3]
m4 = [h(n) for n in l4]
I_v = 0.5
I_n1 = (sum(m1)/len(m1)) * (fabs(b-a))
I_n2 = (sum(m2)/len(m2)) * (fabs(b-a))
I_n3 = (sum(m3)/len(m3)) * (fabs(b-a))
I_n4 = (sum(m4)/len(m4)) * (fabs(b-a))

MC = pd.DataFrame({"n":[n1,n2,n3,n4],"Integral": [I_n1,I_n2,I_n3,I_n4],"Erro": [fabs(I_v-I_n1),fabs(I_v-I_n2),fabs(I_v-I_n3),fabs(I_v-I_n4)]})
print(MC) 

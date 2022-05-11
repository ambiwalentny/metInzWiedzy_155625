
import numpy as np
import random

a = 0
b = 1
N = 1000
xrand = np.zeros(N)

for i in range(len(xrand)):
    xrand[i]= random.uniform(a,b)

def func(x):
    return x

integral = 0

for i in range(N):
    integral+=func(xrand[i])

wynik = (b-a)/N*integral
print(wynik)
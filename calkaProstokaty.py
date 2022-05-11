import numpy as np

def funkcja(x):
    return x

def metodaProstokatow(low, high, f, N):
    rectangle_edges = np.linspace(low, high, N)
    area= 0
    for r in range(len(rectangle_edges)):
        area += f(low+r*(high-low)/N)*(high-low)/N
    return area

print(metodaProstokatow(0,1,funkcja,10000))
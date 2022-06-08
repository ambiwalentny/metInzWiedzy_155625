import math

def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b)**2
    wynik = math.sqrt(wynik)
    return wynik


print(metryka_euklidesowa_wektory([1,2, 3], [3,4, 6]))
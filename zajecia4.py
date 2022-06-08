#x same jedynki długosc wiersza
# lista par klasa decyzyjna, odleglosc
import math
import numpy

def plikDoListy(plik, lista):
    with open(plik, 'r') as plik:
        for linia in plik:
            zmienna = []
            for wartosc in linia.split():
                zmienna.append(float(wartosc))
            lista.append(zmienna)

australian = []
x0 =[]
plikDoListy("australian.dat", australian)

for el in australian[0]:
    x0.append(1)

def MetrykaEuklidesowa(listaA, listaB):

    dl = len(listaA) - 1
    tmp = 0
    for id in range(dl):
        zm1 = listaA[id]
        zm2 = listaB[id]
        c = zm1 - zm2
        wynik = c ** 2
        tmp += wynik

    result = math.sqrt(tmp)

    return result


def funk(x, lista):
    wynik = []

    for item in lista:
        c = item[-1]
        odl = MetrykaEuklidesowa(x, item)
        wynik.append((c,odl))

    return wynik


zadanie1lista = funk(x0,australian)

#zamieniamy listę par na słownik gdzie klasa decyzyjna kluczem i odleglosci wartoscią

def zadanie2 (lista):

    s = {}

    for n in lista:
        key = n[0]
        value = n[1]
        if key not in s:
            s[key] = []
            s[key].append(value)
        else:
            s[key].append(value)
    return s

zadanie2slownik = zadanie2(zadanie1lista)



###################################################################################
# ZADANIE                                                                         #
# obliczanie metryki euklidesowej korzystając z wektorów i operacji na wektorach  #
###################################################################################

def funkcja3(zadanie):
    tmp=[]
    tmp2 = []
    wynik= []
    for i in zadanie:
        print(i, zadanie[i])
        tmp.append(zadanie[i])
    tmp2 = tmp[len(wynik/2):]



funkcja3(zadanie2slownik)


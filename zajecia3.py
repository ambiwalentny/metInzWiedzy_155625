# odległosc(a,b) == 0 <=> a == b
# odległosc(a,b) == odległosc(b,a
# odległosc(a,b) + odległosc(b,c) >= odległosc(a,c)
# (suma długości dwóch boków trójkąta dłuższa lub równa długości trzeciego boku)
import math

def plikDoListy(plik, lista):
    with open(plik, 'r') as plik:
        for linia in plik:
            zmienna = []
            for wartosc in linia.split():
                zmienna.append(float(wartosc))
            lista.append(zmienna)

q1 = []
plikDoListy("australian.dat", q1)

for x in range(5):
    print(q1[x])


q2 = []
def funkcjaOdProwadzacego(plik, lista):
    with open(plik, 'r') as file:
        for line in file:
            x = line.replace('\n', '').split()
            wynik = list(map(lambda e: float(e), x))
            lista.append(wynik)

print("~~~~~~~~~~")
funkcjaOdProwadzacego("australian.dat", q2)
for x in range(5):
    print(q2[x])




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

# l1 = lB[1]
# l2 = lB[2]
# w = MetrykaEuklidesowa(l1, l2)
# print(w)
l1 = q1[0]
l2 = q1[1]
w = MetrykaEuklidesowa(l1, l2)
print(w)

l1 = q1[0]
l3 = q1[2]
w1 = MetrykaEuklidesowa(l1, l3)
print(w1)

l1 = q1[0]
l4 = q1[3]
w2 = MetrykaEuklidesowa(l1, l4)
print(w2)


#odleglosc(y,x) gdzie x nalezy do x, bez elementu z indeksem 0
# między pierwszy a wszystkim pozostałymi
# slownik
# klucz: klasa decyzyjna x (na ostatnim elemencie)
# wartyość: lista z odleglosciami
# if klucz == 0 to trafić mają y dla jakich {0: ...}, {1: ...}, {2: ...}

def domowa1(lista):
    pkt_kontrolny = lista[0]
    listaWyjściowa = []
    for x in range(len(lista)):
        print(MetrykaEuklidesowa(pkt_kontrolny, lista[x]))
        listaWyjściowa.append(MetrykaEuklidesowa(pkt_kontrolny, lista[x]))
    return listaWyjściowa


listaDomowa1 = domowa1(q1)
print(len(listaDomowa1))

# napisać funckję która będzie liczyła wyznacznik macierzy kwadratowej


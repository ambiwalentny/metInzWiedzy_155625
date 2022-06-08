import math
import numpy as np

def plikDoListy(plik, lista):
    with open(plik, 'r') as plik:
        for linia in plik:
            zmienna = []
            for wartosc in linia.split():
                zmienna.append(float(wartosc))
            lista.append(zmienna)

dane = []
plikDoListy("australian.dat", dane)

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



def domowa1(lista):
    pkt_kontrolny = lista[0]
    listaWyjściowa = []
    for x in range(len(lista)):
        #print(MetrykaEuklidesowa(pkt_kontrolny, lista[x]))
        listaWyjściowa.append(MetrykaEuklidesowa(pkt_kontrolny, lista[x]))
    return listaWyjściowa


listaDomowa1 = domowa1(dane)
#print(len(listaDomowa1))


###domowa 2
def Distance(lista):

    y = lista[0]
    s = {}

    for l in range(len(lista))[1:]:
        tmpl = lista[l]
        ost = len(tmpl) - 1
        key = int(tmpl[ost])
        wynik = MetrykaEuklidesowa(y, lista[l])
        if key not in s:
            s[key] = []
            s[key].append(wynik)
        else:
            s[key].append(wynik)
            # print(f'Odległość listy {l} od y wynosi: {wynik}')
    return s


###domowa 3
def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M
def skopiuj_macierz(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def determinant_recursive(A, total=0):

    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = skopiuj_macierz(A)
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)  # F)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det

    return total


A = [[1,2,3,4],[8,5,6,7],[9,12,10,11],[13,14,16,15]]
wyznacznik = determinant_recursive(A)
wyznaczniknp = np.linalg.det(A)

print("wyznacznik z funkcji: ", wyznacznik)
print("wyznacznik z numpy: ", wyznaczniknp)
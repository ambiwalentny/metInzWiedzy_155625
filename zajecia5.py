import numpy as np
import math

########### zadanie 1 ##############
def metryka_euklidesowa_z5z1(lista1, lista2, want=False):
    if (want):
        v1 = np.array(lista1[:-1])
        v2 = np.array(lista2[:-1])
    else:
        v1 = np.array(lista1)
        v2 = np.array(lista2)

    c = v1 - v2

    skal = np.dot(c, c)
    wynik = math.sqrt(skal)
    return wynik

print(metryka_euklidesowa_z5z1([1,2,3],[3,4,6],True))
print(metryka_euklidesowa_z5z1([1,2],[3,4]))

#10 luty 1:10 h wykładu
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
australianAtIndex0 = australian[0]
australianAtIndex1 = australian[1]
print(australianAtIndex0)
print(australianAtIndex0[:-1])
# podzielenie austaraliana na dwie grupy bez ostatniej kolumny
# pierwsze przbyliżenie, losowe malowanie kropek, niebzyt dokładne
#
# bierzemy pierwszą kropkę, sumujemy odleglości do każdej innej kropki
# potem 2, 3 itd. Kropka z najmniejszą sumą jest poszukiwanym środkiem
#
# sprawdzamy wszystkie kropki (nie patrząc na kolory)
# jeżeli niebieska i bliżej niebieskiej, to nie zmieniamy
# jeżeli niebieska i bliżej czarnej, to zmieniamy
# analogicznie dla czarnych

# program do całkowania
# 1 metoda
# met. monte carlo
# całka, pole pod krzywą, granice całkowania to oznaczenie gdzie zaczyamy i kończymy
# musimy określić maksimum funkcji w przedziale, (możemy przejśc przedział z krokiem
# bierzemy, największy y z obliczonych krokami, (mnożymy 2x dla pewności żeby się wszystko zmieściło)
# d1, d2, długości figury
# met. mon. carl. bierzemy losowy punkt, jak wstawimy x do naszej funckji to otrzymamy jakiś nowy y
# jeśli nowy y jest większy to nie jest pod wykresem
# ---równy --- jest na lini
# -- mniejszy -- pod wykresem
#jeśli będziemy się poruszać równym krokiem
# obliczamy stosunek to co jest pod/na wykresie do wszystkich punktów
# ten stosunek wskazuje jaką cześć prostokąta pod wykresem jest zawarta w całce


# przbliżenie prostokątami Sumy Darboux (chyba xD)
# suma gróna i dolna, górna na wykresem, dolna pod
# jak to podzielimy na małe kawałaki to będzie dokładniejsze


# metoda trapezów
# bierzemy dwie watości na krzywej i robimy z tego trapez
# lepsze przybliżenie niż suma prostokąty bo nie ma sumy górnej




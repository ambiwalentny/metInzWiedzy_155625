import numpy as np
import math
import random

def plikDoListy(plik, lista):
    with open(plik, 'r') as plik:
        for linia in plik:
            zmienna = []
            for wartosc in linia.split():
                zmienna.append(float(wartosc))
            lista.append(zmienna)

australian = []
plikDoListy("australian.dat", australian)


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




def losowanieDecyzyjnej(dane):
    nowa = []
    for x in dane:
        nowa.append(x[:-1])

    for y in nowa:
        y.append(random.randint(0,1))

    return nowa



def dwieGrupy(dane):
    grupa1 = []
    grupa2 = []
    for x in dane:
        if(x[-1]):
            grupa1.append(x)
        else:
            grupa2.append(x)
    return grupa1, grupa2




def odleglosci(dane):
    Listaodleglosci= []
    for x in dane:
        odleglosc = 0
        for y in dane:
            odleglosc += metryka_euklidesowa_z5z1(x, y)
            if y == dane[-1]:
                Listaodleglosci.append(odleglosc)
    return Listaodleglosci


def najmniejszaOdleglosc(dane):
    wynik = dane[0]
    iteracje = 0
    for x in dane[1:]:
        iteracje += 1
        if x < wynik:
            wynik = x


    return wynik



def gdzieJestNajmniejsza(dane, najmniejsza):
    wynik = 999999
    for x in range(len(dane)):
        if dane[x] == najmniejsza:
            wynik = x

    return wynik



def algorytm(zestawDanych):
    iteracja = 0
    liczba_zmian = 2137
    losowyAtrybutDecyzyjny = losowanieDecyzyjnej(zestawDanych)
    grupa0, grupa1 = dwieGrupy(losowyAtrybutDecyzyjny)
    print(len(losowyAtrybutDecyzyjny), "   ", len(grupa0), "    ", len(grupa1))
    while liczba_zmian > 0:
        iteracja += 1
        print("iteracja ", iteracja, ": ")

        liczba_zmian = 0
        odleglosciGrupa0 = odleglosci(grupa0)
        odleglosciGrupa1 = odleglosci(grupa1)
        najkrotszaGrupa0 = najmniejszaOdleglosc(odleglosciGrupa0)
        najkrotszaGrupa1 = najmniejszaOdleglosc(odleglosciGrupa1)

        indexGrupa0 = gdzieJestNajmniejsza(odleglosciGrupa0,najkrotszaGrupa0)
        indexGrupa1 = gdzieJestNajmniejsza(odleglosciGrupa1, najkrotszaGrupa1)

        srodekMasyGrupa0 = grupa0[indexGrupa0]
        srodekMasyGrupa1 = grupa1[indexGrupa1]

        for x in losowyAtrybutDecyzyjny:
            ileDoSrodkaMasyGrupa0 = metryka_euklidesowa_z5z1(x,srodekMasyGrupa0)
            ileDoSrodkaMasyGrupa1 = metryka_euklidesowa_z5z1(x,srodekMasyGrupa1)
            if ileDoSrodkaMasyGrupa1 < ileDoSrodkaMasyGrupa0 and x in grupa0:
                grupa0.remove(x)
                grupa1.append(x)
                liczba_zmian += 1
                print("zmiana ", liczba_zmian, ": z grupy 0 do grupy 1")

            else:
                if ileDoSrodkaMasyGrupa0 < ileDoSrodkaMasyGrupa1 and x in grupa1:
                    grupa1.remove(x)
                    grupa0.append(x)
                    liczba_zmian += 1
                    print("zmiana ", liczba_zmian, ": z grupy 1 do grupy 0")



    print("zakończono po ", iteracja, "iteracjach")
    grupa0.sort()
    grupa1.sort()
    print("klasa decyzyjna 1: ", grupa0)
    print("klasa decyzyjna 2: ", grupa1)
    print(len(grupa0), "   ", len(grupa1))





#algorytm(australian)


    def rectint(f, a, b, rectangles):
        cumulative_area = 0

        a = float(a)
        b = float(b)
        rectangles = float(rectangles)

        i = (b - a) / rectangles

        trailing_x = a
        leading_x = a + i

        while (a <= leading_x <= b) or (a >= leading_x >= b):
            area = f((trailing_x + leading_x) / 2) * i
            cumulative_area += area

            leading_x += i
            trailing_x += i

        return cumulative_area


    def trapint(f, a, b, trapezoids):
        cumulative_area = 0

        a = float(a)
        b = float(b)
        trapezoids = float(trapezoids)

        i = (b - a) / trapezoids

        trailing_x = a
        leading_x = a + i

        while (a <= leading_x <= b) or (a >= leading_x >= b):
            area = (f(trailing_x) + f(leading_x)) * i / 2
            cumulative_area += area

            leading_x += i
            trailing_x += i

        return cumulative_area


    def func(x):
        return x**3 + 1


























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
# jeśli będziemy się poruszać równym krokiem
# obliczamy stosunek to co jest pod/na wykresie do wszystkich punktów
# ten stosunek wskazuje jaką cześć prostokąta pod wykresem jest zawarta w całce


# przbliżenie prostokątami Sumy Darboux (chyba xD)
# suma gróna i dolna, górna na wykresem, dolna pod
# jak to podzielimy na małe kawałaki to będzie dokładniejsze


# metoda trapezów
# bierzemy dwie watości na krzywej i robimy z tego trapez
# lepsze przybliżenie niż suma prostokąty bo nie ma sumy górnej




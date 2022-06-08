panstwa = {
'Rosja': 'Moskwa',
'Litwa': 'Wilno',
'Białoruś': 'Mińsk',
'Ukraina': 'Kijów',
'Słowacja': 'Bratysława',
'Czechy': 'Praga',
'Niemcy': 'Berlin'} #jak to posortować

panstwa.keys() #klucze
panstwa.items() #wartosci

#dodanie do slownika
panstwa['Hiszpania'] = 'Madryt'

#print(panstwa.keys())


#print(bool(''))  # False
#print(bool(' '))  # True
#print(bool(0))  # False
#print(bool(1))  # True
#print(bool('0'))  # True
#print(bool('1'))  # True
#print(bool([]))  # False
#print(bool([","]))  # True

q = "Metody Inżynierii Wiedzy"
#print("i" in q) #sprawdzenie czy coś jest zawarte

#for x in range(21):
#    print(x)


lista = ["szafa", "drzwi", "tablica", "monitor"]
lista_polaczona = "-".join(lista)

#print(lista_polaczona)
lista_rozdzielona = lista_polaczona.split("-")
#print("split: ",lista_rozdzielona)


def nowySplit(napis, dzielnik):
    listawyj = []
    el = ""
    for x in range(len(napis)):
        if napis[x] != dzielnik:
            el += napis[x]
        if napis[x] == dzielnik or x == len(napis)-1:
            listawyj.append(el)
            el = ""

    return listawyj

test = nowySplit(lista_polaczona, "-")
#print("nowa funkcja: ", test)

#10 znaków
#duże małe litery
#czy jest !



def SprawdzanieHasla(haslo):
    male = False
    duze = False
    for litera in haslo:
        if litera.isupper():
            duze = True
        if litera.islower():
            male = True

    if len(haslo)>= 10 and male and duze and "!" in haslo:
        return True

    return False

has1 = "aaaaaaaaaaaaaaaaaaaaaaaa"
has2 = "AAAAAAAAAAAAAAAAAAAAAAAAAA"
has3 = "Aa!"
has4 = "AAAAAAAAAAAAAA!aawaea"


#print("~~~~~~~~~~~~~~~~~~~~")
#print(SprawdzanieHasla(has1)) #False
#print(SprawdzanieHasla(has2)) #False
#print(SprawdzanieHasla(has3)) #False
#print(SprawdzanieHasla(has4)) #True



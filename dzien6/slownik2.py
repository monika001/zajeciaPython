#umieszczenie e4 słowników w jednym słowniku osoby
osoby = {}

rekordy = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]

#stworzenie unikatowych kluczy:
for indeks, rekord in enumerate(rekordy):
    osoby[indeks] = rekord

print(osoby)

#dodajac kolejny rekord, sprawdzamy jaka najwyzsza wartosc ma klucz, i dodajemy kolejny klucz3
#ale trzena uwazac, bo ktores elemny (z kluczem) mogly zostac ususniete
print(len(osoby))


najw_indeks = max(osoby.keys())
#jest to najwiekszy indeks, najwiekszy klucz
print(najw_indeks)

osoby[najw_indeks + 1] = {"imie": "Anna", "nazwisko":"nowak", "wiek":23}

#utworzenie jednego słownika gdzie wartosciami sa listy, sprowadza sie do problemu
#posiadania trzech list i wyszukiwania, jak np mam 100 elementow, chce znalezc
#imię Zbyszek, to muszę przejśc np przze 99 elementów listy

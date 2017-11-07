imie = "Joanna"
nazwisko = "Kowalska"
wiek = 34
#komentarz
print(imie)

print(imie[3:5])

print(3 + 7)
print(3 == 9)
print(5*9)
print(imie.lower())
print(imie.count('a'))

print(imie + ' ' + nazwisko + 'ma' + str(wiek) + 'lata')

#formatowanie stringa od wersji 3.6
#w klamrach wstawiamy zmienne
print(f"{imie} {nazwisko} ma {wiek} lata")

#starsze wersje niz 3.6
print("{0} {1} ma {2} lata.".format(imie, nazwisko, wiek))
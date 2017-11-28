def dodaj_imie(imie, baza=[]):

    imie= imie.upper()
    baza.append(imie)
    return baza


#imiona = ["ANNA", "DAMIAN"]
#dodaj_imie("andrzej", imiona)
#dodaj_imie("kasia", imiona)
#
#print(imiona)


#python tylko raz sprawdzi obiekt baza=[]
#spr, czy argument baza zostal podany, jesli nie, to utworzy
#za drugim razem, drugim wywołaniem juz nie sprawdza obiektu baza
anglicy = dodaj_imie("john")
print(anglicy)
francuzi = dodaj_imie("antoine")
print(francuzi)
rosjanie = dodaj_imie("sasza")
print(rosjanie)
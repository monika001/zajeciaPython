#dwie zmienne w funkcji: imie i duze_imie

imie = "Ola"

#to imie u gory i imie w argumencie funkcji to sa inne imiona, gdzie indziej one istnieja
#glbal imie - wksazujemy ktora zmienna globalna ma byc braan pod uwage jako imie
#ale niezalecane, nalezy unikac, w funkcjach tworzymy zmienne lokalne
def wypisz_imie(imie2="ala"):
    global imie
    duze_imie = imie.upper()
    return duze_imie

print(imie)

print(wypisz_imie())


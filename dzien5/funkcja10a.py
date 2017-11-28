#jak sie ustrzec przed nadpisywaniem imion do tej samej bazy, jesli nie podamy jej w kolejnych wywolaniach
#jelsi bazajest None, to wemy, ze uzytkownik nic nam nie podal
#i wtedy tworzymy nowa baze



def dodaj_imie(imie, baza=None):
    """Dodaje imie do bazy, jesli baza nie
    istnieje, tworzy nowa baze
    (str, [list]) -> list"""

    if baza == None:
        baza = []

    imie= imie.upper()
    baza.append(imie)
    return baza

anglicy = dodaj_imie("john")
print(anglicy)
francuzi = dodaj_imie("antoine")
print(francuzi)
rosjanie = dodaj_imie("sasza")
print(rosjanie)
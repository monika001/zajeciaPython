#co zrobimy z testem, zeby nie wykonywal sie przy imporcie tego modulu

def odwroc_string(zdanie):
    """
    Zwraca odwrócony string. Jeśli argument jest pustym
    stringiem lub None - zwraca None
    :param zdanie: Zdanie do odwrócenia
    :return: Odwrócone zdanie lub None
    """
    if zdanie == '' or zdanie == None:
        return None
    return zdanie[::-1]



#kod testu, ktory wywoluje wewnatrz mdulu, opakowuje
#w funckje main, ktora nie przyjmuje zadnych arg
#po to, zeby przy wywolaniu modulu w innym porgramie, ten kod sie nie wywolywal
#moze sie nazywac dowolnie, ale przyjelo sie, ze nazywamy ja main

def main():
    imie = "Ala"
    odwr_imie = odwroc_string(imie)
    spr_imie = imie[::-1]

    if odwr_imie == spr_imie:
        print(f"Imię {imie} zostało prawidłowo obrócone na {odwr_imie}.")
    else:
        print(f"Nieprawidłowo {imie} != {odwr_imie}")

#dodatkowo na koncu piszę if'a, w ktorym wywoluje funkcje main
#pyhon nadaje swoja wewnetrzna nazwe dla pliku, ktory zostal uruchomiony
#taki plik ma zawsze nazwe main
#nazwe __main__ otrzymuje plik, ktory jest wywolywany
if __name__ == '__main__':
    main()
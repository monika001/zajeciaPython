#odwroc string i porwnaj ze sringiem wejsciowym
#II sposob bez odwracania: porownujemy pierwsza i osttani , druga i przedostatnia
#np KAJAK - sprawdzenie o jedno wiecej niz polowe
#jak w pliku mam kod, ktory chce zaimportowac, to mam modul (taka biblioteka)
#musze powiedziec ska zaimportowac ten modul
#glownym folderem na ktory patrzy python jest zajeciaPython lub ten sam folder, w ktorym piszemy folder
#jesli znajduje sie gdzies indziej, to podajemy sciezke
#wykorzystanie fukcji z modulu: nazwa_modulu.nazwafunkcji

import dzien7.moj_modul.odwracanie_stringa


def czy_palindrom(wyraz):
    """Sprawdza czy podany string jest palindromem
    (str) -> bool
    """
    wyraz = wyraz.upper()
    odwrocony = dzien7.moj_modul.odwracanie_stringa.odwroc_string(wyraz)

    if wyraz == odwrocony:
        return True
    else:
        return False

print(czy_palindrom("kajak"))
#program sprawdza wkorym miejscu jestesmy, czy jestesmy w
# nowej linii

sciezka = "tekst1.txt"

tekst = """To jest mój tekst. To
 jest kolejna linijka tekstu,
        a to kolejna."""

with open(sciezka, 'r+') as plik:

    #print(plik.tell())
    #ide do konca pliku:
    #read - odczytuje cala zawartosci ustawia sie na koncu pliku
    plik.read()

    pozycja = plik.tell()

    #przechodzimy do przedostatniej pozycji (zeby dczytac ostatni znak)
    plik.seek(pozycja - 1)

    ostatni_znak = plik.read()
    print(ostatni_znak)

    #jesli otrzymam znak inny niz nowa (pusta) linia, tzn ze nie jestem w nowej linii

    if ostatni_znak != '\n':
        plik.write("\n" + tekst + '\n')
    else:
        plik.write(tekst + '\n')
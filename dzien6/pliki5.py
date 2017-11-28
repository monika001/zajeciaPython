sciezka = "tekst1.txt"

#oworzenie w trybie w od razu kasuje cala zawartosc
#w trybie w nie  mozna odczytywac plikow

#string """""" zapamietuje formatowanie wewnatrz """"""
tekst = """To jest mój tekst. To
 jest kolejna linijka tekstu,
        a to kolejna."""

#r+ polaczenie trybu r i w
with open(sciezka, 'w', encoding='utf-8') as plik:
    print(plik.tell())
    plik.write(tekst)
    plik.seek(0)
    #plik.read()



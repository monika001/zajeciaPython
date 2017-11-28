sciezka = "tekst1.txt"

#readline odczytuje linijke i przejdzie do nowej i bedzie czekal na kolejne wywolanie
#bedzie czekal w nowej linii
#jesli zrobie potem read - to odczyta caly plik od ursosra, od momentu w ktorym sie znajduje

#nowa linia po readline - print + znak konca linii
#wczytuje tez znaki niedrukowalne
#with open automatycznie zamyka plik

with open(sciezka) as plik:
    linijka = plik.readline()

    #zeby zobaczyc gdzie kursor sie aktualnie znajduje:
    pozycja = plik.tell()
    print(f"Kursor znajduje się w pozycji nr {pozycja}")


    #lub linijka = linijka.strip()
    #print(linijka, end='')
    #print("Kolejna linijka")
    #print(plik.read())

    #seek - idz do pozycji nr 3
    plik.seek(3)
    print(plik.read())
nazwisko = input("Podaj nazwisko:\n")

#usuwamy white spaces z poczatku i konca
nazwisko = nazwisko.strip()


#jeśli w stringu są cyfry, napisać komunikat
#i przerwać program
if not nazwisko.isalpha():
    print("Musza być same litery")
    exit(99)

#print(type(nazwisko))



#lub nadpisujemy stara zmienna
#nazwisko = nazwisko.strip()

#zamieniamy wszystkie litery na duże
nazw_czyste = nazwisko.upper()

print(nazw_czyste)




#endswith jest lepsze, bo jest sprawniejsze, niz slice i mozna dodać więcej znaków na koniec
if nazw_czyste[-1] == 'a':
    print("kobieta")
elif nazw_czyste.endswith("ski") or nazw_czyste.endswith("SKI"):
    print("Prawdopodobnie jestes mężczyzną")

#elif nazw_czyste.isupper():
#    print("Chyba jestes zlosliwa :(")

print("koniec programu")